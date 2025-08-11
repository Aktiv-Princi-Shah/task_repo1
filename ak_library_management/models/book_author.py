# - * - coding: utf - 8 -*-
from odoo import models, fields

class BookAuthor(models.Model):
    """
    :define: Class method for author details including Many2one relational field for books
    :returns: None
    """
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string='Author', required=True)
    # relational field for book and author
    book_member_id = fields.Many2one(comodel_name='library.book', string='Book')
