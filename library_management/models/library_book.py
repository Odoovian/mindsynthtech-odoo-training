from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description ="Library Book information"

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    isbn = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Publication Date')
    pages = fields.Integer(string='Number of Pages')
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    price = fields.Float(string="Price")
    book_category_id = fields.Many2one("library.book.category",string="Category")
    #
    content = fields.Html(string='HTML Content')
    is_available = fields.Boolean(string='Available', default=True)
    last_borrowed = fields.Datetime(string='Last Borrowed')
    cover_image = fields.Binary(string='Cover Image')
    cover_filename = fields.Char(string='Cover Filename')
    #
    state = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost'),
    ], string='Status', default='draft', required=True)

    category = fields.Selection(
        selection='_get_category_selection',
        string='Category'
    )

    # Many2one - A book belongs to one publisher
    publisher_id = fields.Many2one(
        'res.partner',
        string='Publisher',
        ondelete='set null',  # Options: 'cascade', 'restrict', 'set null'
        domain="[('is_company', '=', True)]",
        help='Select the publisher'
    )

    # One2many - A book can have multiple borrowing records
    borrowing_ids = fields.One2many(
        'library.borrowing',
        'book_id',
        string='Borrowing History'
    )

    author_ids = fields.Many2many(
        'library.author',
        'library_book_author_rel',  # relation table name
        'book_id',  # column for this model
        'author_id',  # column for other model
        string='Authors'
    )

    @api.model
    def _get_category_selection(self):
        return [
            ('fiction', 'Fiction'),
            ('non_fiction', 'Non-Fiction'),
            ('science', 'Science'),
            ('history', 'History'),
        ]



