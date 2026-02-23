{
    'name': 'Library Management',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Library data',
    'author': 'Ayesha',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        #'views/library_book_category.xml',
        'views/library_book.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}