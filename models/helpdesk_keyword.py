from odoo import models, fields

class HelpdeskKeyword(models.Model):
    _name = "helpdesk.keyword"
    _description = "Palabra Clave para Automatización"

    name = fields.Char("Palabra Clave", required=True)
