from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description ="Library Author information"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)



