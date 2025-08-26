from odoo import models, fields

class HelpdeskTeam(models.Model):
    _name = "helpdesk.team"
    _description = "Equipo de Soporte"

    name = fields.Char(string="Nombre del Equipo", required=True)
    member_ids = fields.Many2many('res.users', string="Miembros")
