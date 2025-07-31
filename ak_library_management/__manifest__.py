{
    'name': 'ak_library_management',
    'version': '18.0.1.0.0',
    'author': 'Princi',
    'website': 'https://www.prihhhh.com',
    'category': 'Library',
    'depends': ['base','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_member_views.xml',
        'views/library_menu_action_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
