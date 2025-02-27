from odoo import models, fields, api
from datetime import datetime

class PhuongTien(models.Model):
    _name = "phuong_tien"
    _description = "Quản lý Phương Tiện Giao Thông"
    _rec_name = "bien_so_xe"

    bien_so_xe = fields.Char(string="Biển Số Xe", required=True)
    loai_xe = fields.Selection([
        ('oto', 'Ô tô'),
        ('xemay', 'Xe máy'),
        ('xetai', 'Xe tải'),
        ('xekhach', 'Xe khách')
    ], string="Loại Phương Tiện", required=True)
    hang_san_xuat = fields.Char(string="Hãng Sản Xuất", required=True)
    nam_san_xuat = fields.Integer(string="Năm Sản Xuất", required=True, default=lambda self: datetime.now().year)
    mau_sac = fields.Char(string="Màu Sắc")

    trang_thai = fields.Selection([
        ('hoatdong', 'Hoạt động'),
        ('baotri', 'Bảo trì'),
        ('dung', 'Dừng hoạt động')
    ], string="Trạng Thái", default='hoatdong', compute="_compute_trang_thai", store=True)

    tai_xe_id = fields.Many2many('res.partner', string="Tài Xế Phụ Trách", domain=[('is_driver', '=', True)])
    bao_tri_ids = fields.One2many('bao_tri_phuong_tien', 'phuong_tien_id', string="Lịch sử bảo trì")
    nhien_lieu_ids = fields.One2many('nhien_lieu', 'phuong_tien_id', string="Lịch sử nhiên liệu")

    image = fields.Image(string="Ảnh Phương Tiện")

    @api.depends('bao_tri_ids.trang_thai')
    def _compute_trang_thai(self):
        for record in self:
            if record.bao_tri_ids.filtered(lambda x: x.trang_thai == 'dang'):
                record.trang_thai = 'baotri'
            else:
                record.trang_thai = 'hoatdong'

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_driver = fields.Boolean(string="Là tài xế", default=False)
