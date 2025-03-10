from odoo import models, fields, api

class LichSuNguoiLai(models.Model):
    _name = "lich_su_nguoi_lai"
    _description = "Lịch sử người lái"
    _rec_name = "tai_xe_id"

    tai_xe_id = fields.Many2one('tai_xe', string="Tài xế", required=True)
    phuong_tien_id = fields.Many2one('phuong_tien', string="Phương tiện", required=True)
    thoi_gian_bat_dau = fields.Datetime(string="Thời gian bắt đầu", required=True)
    thoi_gian_ket_thuc = fields.Datetime(string="Thời gian kết thúc")
    trang_thai = fields.Selection([
        ('dang_lai', 'Đang lái'),
        ('da_ket_thuc', 'Đã kết thúc'),
        ('huy', 'Hủy')
    ], string="Trạng thái", default='dang_lai')
    ghi_chu = fields.Text(string="Ghi chú")
