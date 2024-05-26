from odoo import fields, models, api, _
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
class BulletinBoardRecord(models.Model):
    _name = 'bulletin.board.record'
    _description = '佈告欄'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order ='top desc ,create_date desc'

    def _default_user(self):
        return self.env.user.id

    name = fields.Char(string='主旨', required=True, tracking=True)
    type = fields.Many2many('bulletin.board.type', string='公告類別', required=True)
    is_type_child = fields.Boolean('是否有子類別', compute='compute_is_type_child')
    child_type = fields.Many2one('bulletin.board.type.child', string='子類別', domain="[('parent_id', 'in', type)]")
    top = fields.Boolean('置頂', default=False)
    recorder = fields.Many2one('res.users', string="公告人", default=_default_user, required=True, index=True)
    start_date = fields.Datetime('公告時間', required=True, default=fields.Datetime.now)

    content = fields.Text('公告內容', required=True, tracking=True)
    other = fields.Many2many('ir.attachment', string='附件')
    is_myself = fields.Boolean(string='',compute='compute_is_myself')
    viewer_ids = fields.Many2many('res.users', string='已看過', compute='compute_viewer_ids')
    viewer_ids_store = fields.Many2many('res.users', string='檢視者紀錄')

    check_out = fields.Char(string='請輸入主旨內容確認刪除')

    def compute_viewer_ids(self):
        for rec in self:
            arr = rec.viewer_ids_store.ids
            if self.env.user.id in arr:
                pass
            else:
                arr.append(self.env.user.id)
            rec.sudo().viewer_ids = arr
            rec.sudo().viewer_ids_store = arr
    def compute_is_type_child(self):
        for rec in self:
            rec.is_type_child = False
            for tmp in rec.type:
                if tmp.child_ids:
                    rec.is_type_child = True


    def edit(self):
        view_id = self.env['ir.ui.view'].sudo().search([('name', '=', 'bulletin.board.record.from')], limit=1)
        return {
            'type': 'ir.actions.act_window',
            'name': _('編輯公告'),
            'view_mode': 'form',
            'view_id': view_id.id,
            'res_model': 'bulletin.board.record',
            'target': 'new',
            'res_id': self.id,
        }
    def delelte_check(self):
        view_id = self.env['ir.ui.view'].sudo().search([('name', '=', 'bulletin.board.record.form.check')], limit=1)
        return {
            'type': 'ir.actions.act_window',
            'name': _('刪除公告'),
            'view_mode': 'form',
            'view_id': view_id.id,
            'res_model': 'bulletin.board.record',
            'target': 'new',
            'res_id': self.id,
        }
    def delete(self):
        if self.name == self.check_out:
            self.unlink()
        else:
            raise UserError('您輸入的主旨內容並不正確!')

    def compute_is_myself(self):
        for rec in self:
            rec.is_myself = False
            if (rec.recorder.id == self.env.user.id) if self.env.user.id else False:
                rec.is_myself = True



