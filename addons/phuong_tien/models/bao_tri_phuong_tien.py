from odoo import api, models, fields

class BaoTriPhuongTien(models.Model):
    _name = "bao_tri_phuong_tien"
    _description = "Bảo Trì Phương Tiện"
    _rec_name = "phuong_tien_id"

    phuong_tien_id = fields.Many2one('phuong_tien', string="Phương Tiện", required=True)
    ngay_bao_tri = fields.Date(string="Ngày Bảo Trì", required=True, default=fields.Date.today)
    chi_phi = fields.Float(compute="_compute_total", string="Chi Phí")
    mo_ta = fields.Text(string="Mô Tả Công Việc")
    trang_thai = fields.Selection([
        ('cho', 'Chờ xử lý'),
        ('dang', 'Đang bảo trì'),
        ('hoan_thanh', 'Hoàn thành'),
    ], string="Trạng Thái", default="cho")
    linh_kien_ids = fields.Many2many('linh_kien_bao_tri', string="Linh Kiện")
    # Trường lấy ảnh của phương tiện
    image = fields.Binary(related='phuong_tien_id.image', string="Ảnh Phương Tiện", readonly=True)

    tai_xe_id = fields.Many2one('tai_xe', string="Tài Xế Thực Hiện")

    @api.depends('chi_phi', 'linh_kien_ids')
    def _compute_total(self):
        for record in self:
            record.chi_phi = record.chi_phi + sum(record.linh_kien_ids.mapped('gia'))

