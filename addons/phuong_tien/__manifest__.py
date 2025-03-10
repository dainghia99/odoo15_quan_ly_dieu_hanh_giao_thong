# -*- coding: utf-8 -*-
{
    'name': "Quản lý Phương Tiện Giao Thông",
    'summary': "Quản lý phương tiện, tài xế và trạng thái hoạt động",
    'description': """
        Module giúp quản lý phương tiện giao thông, tài xế,
        tình trạng hoạt động của phương tiện trong hệ thống Odoo.
    """,
    'author': "Khoàng Đại Nghĩa, Lê Hồng Anh, Trần Khánh Linh",
    'website': "http://www.yourcompany.com",
    'category': 'Fleet Management',
    'version': '1.0',

    # Modules cần thiết để module này hoạt động
    'depends': ['base', 'mail'],

    # Dữ liệu cần tải khi cài đặt module
    'data': [
        'security/ir.model.access.csv',
        'views/nhien_lieu.xml',
        'views/phuong_tien.xml',
        'views/tai_xe.xml',
        'views/bao_tri_phuong_tien.xml',
        'views/hanh_trinh_phuong_tien.xml',
        'views/linh_kien_bao_tri.xml',
        'views/lich_su_nguoi_lai.xml',
        'views/menu.xml',
    ],

    # Dữ liệu demo (chỉ tải khi ở chế độ demo)
    'demo': [
        'demo/demo.xml',
    ],

    # Chạy module ngay sau khi cài đặt
    'installable': True,
    'application': True,
    'auto_install': False,
}
