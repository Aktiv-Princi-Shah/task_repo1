from odoo import models, fields

class Book(models.Model):

    _name = 'book'
    _description = 'Book Details'

    name = fields.Char(string='Book Title', required=True)
    author = fields.Char(string='Author')
    isbn = fields.Char(string='ISBN Number')
    publication_date = fields.Date(string='Publication Date')
    category_id = fields.Many2one('book', string='Category')
    state = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ], string='Status', default='available')
    description = fields.Char(string='Description')