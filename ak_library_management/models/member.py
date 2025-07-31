from odoo import models, fields

class Member(models.Model):
    _name = 'member'
    _description = 'Members Details'

    name = fields.Char(string='Member Name', required=True)
    email = fields.Char(string='Member Email', required=True)
    phone = fields.Char(string='Member Phone', required=True)
    membership_date = fields.Date(string='Membership Date', required=True)
    location = fields.Char(string='Location')