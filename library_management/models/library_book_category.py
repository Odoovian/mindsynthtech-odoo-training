from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description ="Library Book category information"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)



