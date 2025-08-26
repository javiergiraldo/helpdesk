# -*- coding: utf-8 -*-
{
    "name": "Helpdesk Web Form",
    "version": "1.1",
    "summary": "Formulario web y mesa de servicios con SLA, portal y reportes",
    "description": "Mesa de servicios con adjuntos, SLA automático, portal por token, etiquetas, clasificación y reportes.",
    "author": "kappak",
    "website": "https://help.pcmejia.com",
    "category": "Services/Helpdesk",
    "depends": ["base", "mail", "website", "portal"],
    "data": [
        # seguridad
        "security/helpdesk_web_form_security.xml",
        "security/ir.model.access.csv",
        # datos iniciales
        "data/helpdesk_data.xml",
        "data/helpdesk_sla_data.xml",
        "data/cron_jobs.xml",
        "data/helpdesk_service_data.xml",
        # vistas backend
        "views/helpdesk_menu.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_category_views.xml",
        "views/helpdesk_team_views.xml",
        "views/helpdesk_tag_views.xml",
        "views/helpdesk_sla_views.xml",
        "views/helpdesk_report_views.xml",
        'views/helpdesk_dashboard.xml',
        # portal y frontend
        "views/website_helpdesk_form.xml",
        "views/website_helpdesk_portal.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "helpdesk_web_form/static/src/css/helpdesk_form.css",
            "helpdesk_web_form/static/src/js/helpdesk_upload.js",
            "helpdesk_web_form/static/src/js/helpdesk_dependent_service.js",
        ]
    },
    "installable": True,
    "application": True,
}
