from odoo import models, fields

class BaoTriPhuongTien(models.Model):
    _name = "bao_tri_phuong_tien"
    _description = "Bảo Trì Phương Tiện"
    _rec_name = "phuong_tien_id"

    phuong_tien_id = fields.Many2one('phuong_tien', string="Phương Tiện", required=True)
    ngay_bao_tri = fields.Date(string="Ngày Bảo Trì", required=True, default=fields.Date.today)
    chi_phi = fields.Float(string="Chi Phí")
    mo_ta = fields.Text(string="Mô Tả Công Việc")
    trang_thai = fields.Selection([
        ('cho', 'Chờ xử lý'),
        ('dang', 'Đang bảo trì'),
        ('hoan_thanh', 'Hoàn thành'),
    ], string="Trạng Thái", default="cho")  

    # Trường lấy ảnh của phương tiện
    image = fields.Binary(related='phuong_tien_id.image', string="Ảnh Phương Tiện", readonly=True)