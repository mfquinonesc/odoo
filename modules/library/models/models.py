# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char()
    author_id = fields.Many2one('library.author', required=True)
    genre = fields.Char()
    isbn = fields.Char()
    publication_year = fields.Integer()
    copies_available = fields.Integer(default=1)
    total_copies = fields.Integer(default=1)
    loan_ids = fields.One2many('library.loan', 'book_id')
    created_at = fields.Datetime(default=fields.Datetime.now)
    updated_at = fields.Datetime(default=fields.Datetime.now)

    loans_count = fields.Integer(compute='_compute_loans_count', store=True)

    _sql_constraints = [
        ('isbn_unique', 'unique(isbn)', 'The ISBN must be unique')
    ]

    @api.depends('loan_ids')
    def _compute_loans_count(self):
        for book in self:
            book.loans_count = len(book.loan_ids)

    @api.onchange('total_copies')
    def _onchange_total_copies(self):
        if self.total_copies and self.copies_available == 0:
            self.copies_available = self.total_copies

    @api.constrains('copies_available', 'total_copies')
    def _check_copies(self):
        for book in self:
            if book.copies_available > book.total_copies:
                raise ValidationError('Available copies cannot be more than total copies.')

    #This decorator is deprecated for newest versions @api.model
    def create(self, vals_list):
        vals_list['created_at'] = fields.Datetime.now()
        vals_list['updated_at'] = fields.Datetime.now()
        return super().create(vals_list)
    
    def write(self, vals):
        vals['updated_at'] = fields.Datetime.now()
        return super().write(vals)
    


class Author(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(required=True)
    birth_year = fields.Integer()
    nationality = fields.Char()
    book_ids = fields.One2many('library.book', 'author_id')



class Member(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    full_name = fields.Char(required=True)
    email = fields.Char(required=True)
    join_date = fields.Date(default=fields.Date.today)
    loan_ids = fields.One2many('library.loan', 'member_id')

    active_loans = fields.Integer(compute="_compute_active_loans")

    _sql_constraints = [
        ('email_unique', 'unique(email)', 'The email must be unique')
    ]

    @api.depends('loan_ids.return_date')
    def _compute_active_loans(self):
        for member in self:
            member.active_loans = len([loan for loan in member.loan_ids if not loan.return_date])
            


class Loan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'

    book_id = fields.Many2one('library.book', required=True)
    member_id = fields.Many2one('library.member', required=True)
    loan_date = fields.Date(default=fields.Date.today)
    return_date = fields.Date()
    due_date = fields.Date(required=True)