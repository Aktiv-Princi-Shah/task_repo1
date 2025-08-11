# - * - coding: utf - 8 -*-

from odoo import models, fields

class LibraryBookTag(models.Model):
    """
    :define: Class method for book category tags including many2many relational field for categories to display it on books list
    :returns: None
    """
    _name = 'library.book.tag'
    _description = 'Library Book Tag'

    name = fields.Char(required=True)
