from odoo import models, fields

class HelpdeskTag(models.Model):
    _name = "helpdesk.tag"
    _description = "Etiqueta de Ticket"

    name = fields.Char("Nombre", required=True)
    color = fields.Integer("Color")
