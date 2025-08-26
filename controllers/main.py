from odoo import http
from odoo.http import request

class WebsiteHelpdesk(http.Controller):

    @http.route(['/helpdesk/submit'], type='http', auth='public', methods=['POST'], website=True)
    def submit_ticket(self, **post):
        partner = request.env['res.partner'].sudo().create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
        })
        ticket = request.env['helpdesk.ticket'].sudo().create({
            'name': post.get('subject'),
            'partner_id': partner.id,
            'category_id': int(post.get('category_id')),
            'service_id': post.get('service_id') and int(post.get('service_id')) or False,
            'priority': post.get('priority'),
            'description': post.get('description'),
        })
        # adjuntos
        files = request.httprequest.files.getlist('attachment')
        for f in files:
            request.env['ir.attachment'].sudo().create({
                'name': f.filename,
                'type': 'binary',
                'datas': f.read().encode('base64'),
                'res_model': 'helpdesk.ticket',
                'res_id': ticket.id,
            })
        return request.render("helpdesk_web_form.thank_you", {'ticket': ticket})

    @http.route(['/helpdesk/portal/<string:token>'], type='http', auth='public', website=True)
    def portal_ticket(self, token, **kw):
        Ticket = request.env['helpdesk.ticket'].sudo()
        ticket = Ticket.search([('access_token','=',token)], limit=1)
        return request.render("helpdesk_web_form.portal_view", {'ticket': ticket})}
    
    @http.route('/helpdesk/services', type='json', auth='public', methods=['POST'], website=True)
    def get_services_by_category(self, category_id, **kw):
        services = request.env['helpdesk.service'].sudo().search([
            ('category_id', '=', int(category_id))
        ])
        return [{"id": s.id, "name": s.name} for s in services]  