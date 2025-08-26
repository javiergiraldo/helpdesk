from odoo import models, fields

class HelpdeskCategory(models.Model):
    _name = "helpdesk.category"
    _description = "Categoría de Ticket"

    name = fields.Char(string="Nombre", required=True)
    parent_id = fields.Many2one('helpdesk.category', string="Categoría Padre")
