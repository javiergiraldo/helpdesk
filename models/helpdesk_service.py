from odoo import models, fields

class HelpdeskService(models.Model):
    _name = "helpdesk.service"
    _description = "Servicio relacionado a una Categoría"

    name = fields.Char("Servicio", required=True)
    category_id = fields.Many2one(
        comodel_name="helpdesk.category",
        string="Categoría",
        required=True,
        ondelete="cascade",
    )
