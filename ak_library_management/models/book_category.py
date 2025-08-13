# - * - coding: utf - 8 -*-
from odoo import models, fields

class BookCategory(models.Model):
    """
    define: library.book.category
    """
    _name = 'library.book.category'
    _description = 'Book Category'
    _rec_name = 'name'

    name = fields.Char(string='Category', required=True)
    tag_ids = fields.Many2many(comodel_name='library.book.tag', string='Tags')
