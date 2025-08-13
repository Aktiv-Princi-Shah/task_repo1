# - * - coding: utf - 8 -*-
from odoo import models, fields, api

class Book(models.Model):
    """
    define: library.book
    """
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    date_release = fields.Date(string='Publication Date')
    member_ids = fields.One2many(comodel_name='library.members', inverse_name='book_member_id', string='Members')
    author_ids = fields.One2many(comodel_name='library.author', inverse_name='book_member_id', string='Authors')
    category_id = fields.Many2one(comodel_name='library.book.category', string='Category')
    library_id = fields.Many2one(comodel_name='library.library', string='Library')
    tag_ids = fields.Many2many(comodel_name='library.book.tag', related='category_id.tag_ids',string='Tags')
    isbn_number = fields.Char(string='ISBN')
    book_description = fields.Text(string='Book Description')
    book_state = fields.Selection([('borrowed', 'Borrowed'),('available', 'Available')], string='Book Status')
    library_location = fields.Char(string='Library Location', related='library_id.location', store=True)
    book_reference = fields.Char(string='Book Reference', store=True)

    @api.onchange('name','author_ids')
    def _onchange_book_reference(self):
        """
        :define: function helps refer the book name and author name to display in the form view of books
        :params: self
        :returns: self
        """
        for record in self:
            if record.name and record.author_ids:
                record.book_reference = f"{record.name} - {record.author_ids.name}"
            else:
                record.book_reference = ''
