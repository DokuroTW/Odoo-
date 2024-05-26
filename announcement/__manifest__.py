# -*- coding: utf-8 -*-
{
    'name': "佈告欄",

    'summary': """
        公告消息""",

    'description': """
        公告需要傳播的消息，所使用的平台
    """,

    'author': "ALLTOP",
    'website': "http://www.alltop.com.tw",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/securtiy.xml',
        'security/ir.model.access.csv',
        'views/bulletin_board_record.xml',
        'views/bulletin_board_type.xml',
        # 'views/inherit_bulletin_board_record.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
