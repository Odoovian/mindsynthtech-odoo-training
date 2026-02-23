from odoo import models, fields

class LibraryBorrowing(models.Model):
    _name = 'library.borrowing'
    _description ="Library Borrowing information"

    book_id = fields.Many2one('library.book',string='Book')
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    borrower_id = fields.Many2one(
        'res.partner',
        string='Borrower',
        ondelete='set null',  # Options: 'cascade', 'restrict', 'set null'
        domain="[('is_company', '=', True)]",
    )
    borrowed_date = fields.Datetime(string='Borrowed Date')
    return_date = fields.Datetime(string='Return Date')



