# - * - coding: utf - 8 -*-
from odoo import models, fields

class Book(models.Model):
    """
    Book model stores details of each book.
    Each book belongs to one library

    Class method for book including :
    1) one2many relational field for members
    2) many2many relational field for authors
    """

    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    date_release = fields.Date(string='Publication Date')

    # relational field for book and member
    member_ids = fields.One2many('library.members', 'book_member_id', string='Members')
    # relational field for book and authors
    author_ids = fields.One2many('library.author','book_member_id', string='Authors')
    # relational field for books and category
    category_id = fields.Many2one('library.book.category', string='Category')
    # relational field for books and library
    library_id = fields.Many2one('library.library', string='Library')
    # relational field for books and tags
    tag_ids = fields.Many2many('library.book.tag', related='category_id.tag_ids',string='Tags')

    isbn_number = fields.Char(string='ISBN')
    book_description = fields.Text(string='Book Description')
    book_state = fields.Selection([('borrowed', 'Borrowed'),('available', 'Available')], string='Book Status')
