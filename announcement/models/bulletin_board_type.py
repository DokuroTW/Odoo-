from odoo import fields, models, api, _

class BulletinBoardType(models.Model):
    _name = 'bulletin.board.type'
    _description = '公告類別'

    name = fields.Char(string='公告類別名稱', require=True)
    color = fields.Integer('Color Index')
    child_ids = fields.One2many('bulletin.board.type.child', 'parent_id', string='子類別')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "這個類別已經存在了!"),
    ]

class BulletinBoardTypeChild(models.Model):
    _name = 'bulletin.board.type.child'
    _description = '公告子類別'

    name = fields.Char(string='子類別名稱', require=True)
    parent_id = fields.Many2one('bulletin.board.type', string='父類別')