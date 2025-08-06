# - * - coding: utf - 8 -*-
from odoo import models, fields

class Library(models.Model):

    """
    Library model holds information about a physical library.
    One library can have multiple books
    """

    _name = 'library.library'
    _description = 'Different Libraries'

    name = fields.Char('Library Name', required=True)
    location = fields.Char('Library Location', required=True)
    capacity = fields.Integer('Library Capacity', required=True)
    notes = fields.Text('Library Notes')

    # relational field for library and books
    book_ids = fields.One2many('library.book', 'library_id', string='Books in Library')
