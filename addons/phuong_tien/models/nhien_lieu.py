from odoo import api, models, fields

class NhienLieu(models.Model):
  _name = "nhien_lieu"
  _description = "Quản lý Nhiên Liệu"
  _rec_name = "ten_nhien_lieu"

  ten_nhien_lieu = fields.Char(string="Tên Nhiên Liệu", required=True)
  don_gia = fields.Float(string="Đơn Giá", required=True)
  so_luong = fields.Float(string="Số Lượng", required=True)
  ngay_nhap = fields.Date(string="Ngày Nhập", required=True)
  nha_cung_cap = fields.Char(string="Nhà Cung Cấp")
  phuong_tien_id = fields.Many2one('phuong_tien', string="Phương Tiện", required=True)
  tong_tien = fields.Float(string="Tổng Tiền", compute="_compute_tong_tien", store=True)

  @api.depends('don_gia', 'so_luong')
  def _compute_tong_tien(self):
    for record in self:
      record.tong_tien = record.don_gia * record.so_luong

