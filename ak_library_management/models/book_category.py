# - * - coding: utf - 8 -*-
from odoo import models, fields

class BookCategory(models.Model):
    """
    :define: Class method for book category including many2one relational field for books
    :returns: None
    """
    _name = 'library.book.category'
    _description = 'Book Category'
    _rec_name = 'name'

    name = fields.Char(string='Category', required=True)
    # relational field for book category to tags
    tag_ids = fields.Many2many('library.book.tag', string='Tags')
