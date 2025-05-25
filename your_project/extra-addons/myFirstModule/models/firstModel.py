from odoo import models, fields, api

class contractorsTbl(models.Model):
    _name = 'contractors_tbl'
    _description = 'Contractors Table'

    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')
    contact_person = fields.Char(string='Contact Person')
    notes = fields.Text(string='Notes')