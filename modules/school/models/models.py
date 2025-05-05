# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'school.student'
    _description = 'Students Table'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")