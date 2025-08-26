from odoo import models, fields

class HelpdeskAutomationRule(models.Model):
    _name = "helpdesk.automation.rule"
    _description = "Regla de Clasificación Automática"

    name = fields.Char("Nombre", required=True)
    keyword_ids = fields.Many2many('helpdesk.keyword', string="Palabras Clave")
    category_id = fields.Many2one('helpdesk.category', "Categoría a Asignar")
    priority = fields.Selection([
        ('0','Baja'),
        ('1','Normal'),
        ('2','Alta'),
        ('3','Urgente'),
    ], string="Prioridad")
    tag_ids = fields.Many2many('helpdesk.tag', string="Etiquetas a Asignar")
