# -*- coding: utf-8 -*-
from odoo import http
import json


class BookController(http.Controller):

    # Get all books
    @http.route('/api/books', auth='public', type='json', methods=['GET'], csrf=False)
    def get_all(self):
        books = http.request.env['library.book'].sudo().search([])
        results = [{
            'id': book.id,
            'title': book.title,
            'author': book.author_id.name,
            'genre': book.genre,
            'isbn': book.isbn,
            'publication_year': book.publication_year,
            'copies_available': book.copies_available,
            'total_copies': book.total_copies
        } for book in books]      
        return results

    # Get book by Id
    @http.route('/api/books/<int:id>', auth='public', type='json', methods=['GET'], csrf=False)
    def get(self, id):
        book = http.request.env['library.book'].sudo().browse(id)
        if not book.exists():
            return {'error': 'Book not found'}
        result = {
            'id': book.id,
            'title': book.title,
            'author': book.author_id.name,
            'genre': book.genre,
            'isbn': book.isbn,
            'publication_year': book.publication_year,
            'copies_available': book.copies_available,
            'total_copies': book.total_copies
        }
        return result

    # Create book
    @http.route('/api/books', auth='public', type='json', methods=['POST'], csrf=False)
    def create(self):
        args = http.request.httprequest.data.decode()
        data = json.loads(args)
        book = http.request.env['library.book'].sudo().create(data)
        return {'id': book.id, 'message': 'Book created'}

    # Update book
    @http.route('/api/books/<int:id>', auth='public', type='json', methods=['PUT'], csrf=False)
    def update(self, id):
        args = http.request.httprequest.data.decode()
        data = json.loads(args)
        book = http.request.env['library.book'].sudo().browse(id)
        if not book.exists():
            return {'error': 'Book not found'}
        book.write(data)
        return {'message': 'Book updated successfully'}

    # Delete book
    @http.route('/api/books/<int:id>', auth='public', type='json', methods=['DELETE'], csrf=False)
    def delete(self, id):
        book = http.request.env['library.book'].sudo().browse(id)
        if not book.exists():
            return {'error': 'Book not found'}
        book.unlink()
        return {'message': 'Book deleted successfully'}


class AuthorController(http.Controller):

    # Get authors
    @http.route('/api/authors', auth='public', type='json', methods=['GET'], csrf=False)
    def get_all(self):
        authors = http.request.env['library.author'].sudo().search([])
        results = [{
            'id': a.id,
            'name': a.name,
            'birth_year': a.birth_year,
            'nationality': a.nationality
        } for a in authors]
        return results

    # Get author by Id
    @http.route('/api/authors/<int:id>', auth='public', type='json', methods=['GET'], csrf=False)
    def get(self, id):
        author = http.request.env['library.author'].sudo().browse(id)
        if not author.exists():
            return {'error': 'Author not found'}
        result = {
            'id': author.id,
            'name': author.name,
            'birth_year': author.birth_year,
            'nationality': author.nationality
        }
        return result

    # Create author
    @http.route('/api/authors', auth='public', type='json', methods=['POST'], csrf=False)
    def create(self):
        args = http.request.httprequest.data.decode()
        data = json.loads(args)
        author = http.request.env['library.author'].sudo().create(data)
        return {'id': author.id, 'message': 'Author created'}

    # Update author
    @http.route('/api/authors/<int:id>', auth='public', type='json', methods=['PUT'], csrf=False)
    def update(self, id):
        args = http.request.httprequest.data.decode()
        data = json.loads(args)
        author = http.request.env['library.author'].sudo().browse(id)
        if not author.exists():
            return {'error': 'Author not found'}
        author.write(data)
        return {'message': 'Author updated successfully'}
    

    # Delete author
    @http.route('/api/authors/<int:id>', auth='public', type='json', methods=['DELETE'], csrf=False)
    def delete(self, id):
        author = http.request.env['library.author'].sudo().browse(id)
        if not author.exists():
            return {'error': 'Author not found'}
        author.unlink()
        return {'message': 'Author deleted successfully'}
        

class MemberController(http.Controller):

    # Get all members
    @http.route('/api/members', auth='public', type='json', methods=['GET'], csrf=False)
    def get_all(self):
        members = http.request.env['library.member'].sudo().search([])
        results = [{
            'id': m.id,
            'full_name': m.full_name,
            'email': m.email,
            'join_date': m.join_date
        } for m in members]
        return results
    
    # Get member by Id 
    @http.route('/api/members/<int:id>', auth='public', type='json', methods=['GET'], csrf=False)
    def get(self, id):
        member = http.request.env['library.member'].sudo().browse(id)
        if not member.exists():
            return {'error': 'Member not found'}
        result = {
            'id': member.id,
            'full_name': member.full_name,
            'email': member.email,
            'join_date': member.join_date
        }
        return result
    
    # Create member
    @http.route('/api/members', auth='public', type='json', methods=['POST'], csrf=False)
    def create(self):
        args = http.request.httprequest.data.decode()
        data = json.loads(args)
        member = http.request.env['library.member'].sudo().create(data)
        return {'id': member.id, 'message': 'Member created'}
    
    # Update member
    @http.route('/api/members/<int:id>', auth='public', type='json', methods=['PUT'], csrf=False)
    def update(self, id):
        args = http.request.httprequest.data.decode()
        data = json.loads(args)
        member = http.request.env['library.member'].sudo().browse(id)
        if not member.exists():
            return {'error': 'Member not found'}
        member.write(data)
        return {'message': 'Member updated successfully'}

    # Delete member
    @http.route('/api/members/<int:id>', auth='public', type='json', methods=['DELETE'], csrf=False)
    def delete(self, id):
        member = http.request.env['library.member'].sudo().browse(id)
        if not member.exists():
            return {'error': 'Member not found'}
        member.unlink()
        return {'message': 'Member deleted successfully'}


class LoanController(http.Controller):

    # Get all loans
    @http.route('/api/loans', auth='public', type='json', methods=['GET'], csrf=False)
    def get_all(self):
        loans = http.request.env['library.loan'].sudo().search([])
        results =[{
            'id': l.id,
            'book_id': l.book_id,
            'member_id': l.member_id,
            'loan_date': l.loan_date,
            'due_date':l.due_date
        } for l in loans]
        return results
    
    # Get loan by id 
    @http.route('/api/loans/<int:id>', auth='public', type='json', methods=['GET'], csrf=False)
    def get(self, id):
        loan = http.request.env['library.loan'].sudo().browse(id)
        if not loan.exists():
            return {'error': 'Loan not found'}
        result = {
            'id':loan.id,
            'book_id':loan.book_id,
            'member_id':loan.member_id,
            'loan_date': loan.loan_date,
            'due_date':loan.due_date
        }
        return result
    
    # Create loan
    @http.route('/api/loans', auth='public', type='json', methods=['POST'], csrf=False)
    def create(self):
        args = http.request.httprequest.data.decode()
        data = json.loads(args)
        loan = http.request.env['library.loan'].sudo().create(data)
        return {'id':loan.id, 'message':'Loan created'}
    
    # Update loan
    @http.route('/api/loans/<int:id>', auth='public', type='json', methods=['PUT'], csrf=False)
    def update(self, id):
        args = http.request.httprequest.data.decode()
        data = json.loads(args)
        loan = http.request.env['library.loan'].sudo().browse(id)
        if not loan.exists():
            return {'error': 'Loan not found'}
        loan.write(data)
        return {'message': 'Loan updated successfully'}
    
    # Delete loan
    @http.route('/api/loans/<int:id>', auth='public', type='json', methods=['DELETE'], csrf=False)
    def delete(self, id):
        loan = http.request.env['library.loan'].sudo().browse(id)
        if not loan.exists():
            return {'error': 'Loan not found'}
        loan.unlink()
        return {'message': 'Loan deleted successfully'}