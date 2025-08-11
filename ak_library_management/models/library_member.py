# - * - coding: utf - 8 -*-
from odoo import models, fields

class LibraryMember(models.Model):
    """
    :define : class method containing the book borrowed member id using relation to library book model
    """
    _name = 'library.members'
    _description = 'Library Members'

    name = fields.Char(string='Members', required=True)
    book_member_id = fields.Many2one('library.book', string='Book')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    membership_date = fields.Date(string='Membership Date')
