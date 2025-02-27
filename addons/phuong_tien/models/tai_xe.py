from odoo import models, fields

class TaiXe(models.Model):
    _name = "tai_xe"
    _description = "Quản lý Tài Xế"
    _rec_name = "ho_ten"

    ho_ten = fields.Char(string="Họ và Tên", required=True)
    so_gplx = fields.Char(string="Số Giấy Phép Lái Xe", required=True)
    ngay_sinh = fields.Date(string="Ngày Sinh")
    so_dien_thoai = fields.Char(string="Số Điện Thoại")
    trang_thai = fields.Selection(
        [
            ('san_sang', 'Sẵn sàng'),
            ('dang_lam_viec', 'Đang làm việc'),
            ('nghi', 'Nghỉ'),
        ],
        string="Trạng Thái", default='san_sang'
    )

    # Quan hệ với phương tiện (một tài xế có thể có nhiều phương tiện)
    phuong_tien_ids = fields.Many2many('phuong_tien', 'tai_xe_id', string="Phương Tiện Được Giao")
    bao_tri_ids = fields.One2many('bao_tri_phuong_tien', 'tai_xe_id', string="Lịch sử bảo trì")

