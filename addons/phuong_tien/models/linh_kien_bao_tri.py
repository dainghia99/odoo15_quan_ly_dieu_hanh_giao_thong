from odoo import api, models, fields

class LinhKienBaoTri(models.Model):
  _name = "linh_kien_bao_tri"
  _description = "Linh Kiện Bảo Trì"
  _rec_name = "ten_linh_kien"

  ten_linh_kien = fields.Char(string="Tên Linh Kiện", required=True)
  ma_linh_kien = fields.Char(string="Mã Linh Kiện", required=True)
  so_luong = fields.Integer(string="Số Lượng", required=True)
  gia = fields.Float(string="Giá", required=True)
  bao_tri_phuong_tien_ids = fields.Many2many("bao_tri_phuong_tien", string="", required=True)
