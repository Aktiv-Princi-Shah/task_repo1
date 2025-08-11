# - * - coding: utf - 8 -*-
from odoo import models, fields, api

class Book(models.Model):

    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    date_release = fields.Date(string='Publication Date')
    # relational field for book and member
    member_ids = fields.One2many(comodle_name='library.members', inverse_name='book_member_id', string='Members')
    # relational field for book and authors
    author_ids = fields.One2many(comodle_name='library.author', inverse_name='book_member_id', string='Authors')
    # relational field for books and category
    category_id = fields.Many2one(comodle_name='library.book.category', string='Category')
    # relational field for books and library
    library_id = fields.Many2one(comodle_name='library.library', string='Library')
    # relational field for books and tags
    tag_ids = fields.Many2many(comodle_name='library.book.tag', related='category_id.tag_ids',string='Tags')
    isbn_number = fields.Char(string='ISBN')
    book_description = fields.Text(string='Book Description')
    book_state = fields.Selection([('available', 'Available'),('borrowed', 'Borrowed'),('reserved', 'Reserved')],
                                  string='Book Status',
                                  default='available',
                                  compute='_compute_book_state',
                                  store=True)
    library_location = fields.Char(string='Library Location', related='library_id.location', store=True)
    book_reference = fields.Char(string='Book Reference', store=True)

    @api.depends('member_ids')
    def _compute_book_state(self):
        """
        define: method to compute book state
        :param: self
        :return: self
        """
        for record in self:
            if record.member_ids:
                record.book_state = 'borrowed'
            else:
                record.book_state = 'available'

    @api.onchange('name', 'author_ids')
    def _onchange_book_reference(self):
        """
        define: method to onchange book reference
        :param: self
        :return: self
        """
        for record in self:
            if record.name and record.author_ids:
                authors = ', '.join(record.author_ids.mapped('name'))
                record.book_reference = f"{record.name} - {authors}"
            else:
                record.book_reference = ''

    def action_mark_borrowed(self):
        """
        define: method to mark book borrowed
        :param: self
        :return: self
        """
        for record in self:
            record.book_state = 'borrowed'

    def action_mark_available(self):
        """
        define: method to mark book available
        :param: self
        :return: self
        """
        for record in self:
            record.book_state = 'available'

    def action_return_book(self):
        """
        define: method to return book details
        :param: self
        :return: self
        """
        for record in self:
            record.book_state = 'available'
