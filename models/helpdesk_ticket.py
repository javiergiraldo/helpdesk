from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import uuid

class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Ticket de Soporte"

    # campos existentes…
    tag_ids = fields.Many2many('helpdesk.tag', string="Etiquetas")
    access_token = fields.Char("Token de Acceso", readonly=True, copy=False,
        default=lambda self: uuid.uuid4().hex)
    sla_deadline = fields.Datetime(string="Fecha Límite SLA", tracking=True)
    next_activity_id = fields.Many2one('mail.activity', readonly=True)

    @api.model
    def create(self, vals):
        ticket = super().create(vals)
        # Clasificación automática
        rules = self.env['helpdesk.automation.rule'].search([])
        for r in rules:
            if any(kw.lower() in (ticket.name+ticket.description or '').lower() for kw in r.keyword_ids.mapped('name')):
                ticket.category_id = r.category_id.id or ticket.category_id.id
                service_id = fields.Many2one(
        'helpdesk.service',
        string="Servicio",
        domain="[('category_id','=',category_id)]",
        help="Servicios disponibles para la categoría seleccionada",
        tracking=True,    )
                ticket.priority = r.priority or ticket.priority
                ticket.tag_ids = [(4, t.id) for t in r.tag_ids]
        # SLA calculado por regla (sobreescribe si ya existe)
        rule = self.env['helpdesk.sla.rule'].get_sla_for_ticket(ticket)
        if rule:
            ticket.sla_deadline = fields.Datetime.now() + fields.Date.to_timedelta(rule.hours_deadline, unit='h')
        return ticket

    @api.constrains('sla_deadline')
    def _check_sla_deadline(self):
        for rec in self:
            if rec.sla_deadline and rec.sla_deadline < fields.Datetime.now():
                raise ValidationError(_("La fecha límite SLA no puede ser anterior a ahora."))
    def _sla_send_reminders(self):
        activity_type = self.env.ref('mail.mail_activity_data_todo')
        for ticket in self:
            if not ticket.next_activity_id:
                act = self.env['mail.activity'].create({
                    'res_model_id': self.env['ir.model']._get('helpdesk.ticket').id,
                    'res_id': ticket.id,
                    'activity_type_id': activity_type.id,
                    'summary': 'Recordatorio SLA: resolver antes de %s' % ticket.sla_deadline,
                    'date_deadline': ticket.sla_deadline,
                })
                ticket.next_activity_id = act.id
    def action_set_done(self):
        for rec in self:
            rec.stage_id = 'done'

    def action_escalate(self):
        for rec in self:
            rec.priority = '3'
            rec.sla_deadline = fields.Datetime.now() + fields.Date.to_timedelta(1,'h')
