from odoo import api, fields, models
from datetime import timedelta

class HelpdeskSLARule(models.Model):
    _name = "helpdesk.sla.rule"
    _description = "Regla SLA"

    name = fields.Char("Nombre", required=True)
    category_id = fields.Many2one('helpdesk.category', string="Categoría")
    priority = fields.Selection([
        ('0','Baja'),
        ('1','Normal'),
        ('2','Alta'),
        ('3','Urgente'),
    ], string="Prioridad")
    hours_deadline = fields.Float("Horas para SLA", required=True)

    @api.model
    def get_sla_for_ticket(self, ticket):
        domain = []
        if ticket.category_id:
            domain.append(('category_id','=',ticket.category_id.id))
        domain.append(('priority','=',ticket.priority))
        rule = self.search(domain, limit=1, order='category_id desc')
        return rule

    @api.model_create_multi
    def create(self, vals_list):
        tickets = super().create(vals_list)
        for ticket in tickets:
            rule = self.env['helpdesk.sla.rule'].get_sla_for_ticket(ticket)
            if rule:
                ticket.sla_deadline = fields.Datetime.now() + timedelta(hours=rule.hours_deadline)
        return tickets
