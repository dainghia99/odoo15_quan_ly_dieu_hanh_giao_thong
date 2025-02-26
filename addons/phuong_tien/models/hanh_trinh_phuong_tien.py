from odoo import models, fields, api

class HanhTrinhPhuongTien(models.Model):
    _name = "hanh_trinh_phuong_tien"
    _description = "Quản lý Hành Trình Phương Tiện"
    _rec_name = "phuong_tien_id"

    phuong_tien_id = fields.Many2one('phuong_tien', string="Phương Tiện", required=True)
    tai_xe_id = fields.Many2one('res.partner', string="Tài Xế", domain="[('is_driver', '=', True)]")
    ngay_bat_dau = fields.Datetime(string="Ngày Bắt Đầu", required=True, default=fields.Datetime.now)
    ngay_ket_thuc = fields.Datetime(string="Ngày Kết Thúc")
    diem_di = fields.Char(string="Điểm Xuất Phát", required=True)
    diem_den = fields.Char(string="Điểm Đến", required=True)
    quang_duong = fields.Float(string="Quãng Đường (km)")
    trang_thai = fields.Selection([
        ('dang_di', 'Đang di chuyển'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy bỏ'),
    ], string="Trạng Thái", default="dang_di")

    ghi_chu = fields.Text(string="Ghi Chú")

    image = fields.Binary(related='phuong_tien_id.image', string="Ảnh Phương Tiện", readonly=True, store=True)
