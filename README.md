# Helpdesk Professional para Odoo Community 18

Este módulo extiende la gestión de tickets en Odoo 18 con un dashboard analítico, portal web público y todas las validaciones necesarias para un entorno de producción.

## Características principales

- Gestión de tickets con estados, equipos, categorías, servicios y reglas SLA.
    
- Dashboard backend con métricas de “Todos los tickets”, “Abiertos” y “Pendientes”.
    
- Portal público: listado paginado de tickets y formulario web protegido contra CSRF.
    
- Detalle de ticket en portal con campos clave (asignado, equipo, categoría, servicio, SLA, fechas, estado).
    
- Integración de items de menú “Sobre nosotros” y “Contáctanos” en el navbar de tu sitio web.
    
- Secuencias automáticas, constraints de datos y manejo de excepciones para integridad y rollback.
    

## Dependencias

- Odoo Community 18
    
- Módulos base: `base`, `mail`, `website`, `portal`
    

## Instalación

1. Clona este repositorio en tu carpeta de addons:
    
    bash
    
    ```
    git clone https://javiergiraldo/helpdesk.git
    ```
    
2. Añade la ruta a `odoo.conf` en `addons_path`.
    
3. Reinicia el servicio de Odoo y actualiza la lista de apps.
    
4. Instala “Helpdesk Professional” desde el panel de Apps.
    

## Estructura de archivos

text

```
helpdesk/
├── controllers/
│   └── main.py
├── data/
│   ├── cron_jobs.xml
│   ├── helpdesk_service_data.xml
│   └── helpdesk_sla_data.xml
├── models/
│   ├── helpdesk_ticket.py
│   ├── helpdesk_team.py
│   ├── helpdesk_category.py
│   ├── helpdesk_service.py
│   ├── helpdesk_sla_rule.py
│   ├── helpdesk_tag.py
│   └── helpdesk_automation_rule.py
├── security/
│   └── ir.model.access.csv
├── static/
│   ├── description/icon.png
│   └── src/
│       └── js/
│           ├── helpdesk_dependent_service.js
│           └── portal_helpdesk.js
├── views/
│   ├── helpdesk_menu.xml
│   ├── helpdesk_ticket_views.xml
│   ├── helpdesk_sla_views.xml
│   ├── helpdesk_report_views.xml
│   ├── helpdesk_dashboard.xml
│   └── website_helpdesk_portal.xml
└── __manifest__.py
```

## Uso

### Backend

- Accede al menú **Helpdesk** bajo **Services**.
    
- Visualiza métricas en **Dashboard**.
    
- Crea y gestiona tickets con auditoría de cambios.
    

### Portal Público

- Navega a `/helpdesk` para ver el listado de tickets.
    
- Envía nuevos tickets desde `/helpdesk/create`.
    
- Visualiza detalles individuales en `/helpdesk/<ticket_id>`.
    

## Contribuir

1. Crea un _fork_ y un _branch_ para tu cambio.
    
2. Sigue las convenciones de commit (ver sección siguiente).
    
3. Envía un _pull request_ describiendo tu aporte.
    

## Licencia

LGPL-3.0 License

# Convenciones de Commit

Para mantener un historial claro y semántico, utiliza Conventional Commits:

text

```
<type>(<scope>): <descripción breve>

<cuerpo opcional>
<pie opcional>
```

## Tipos comunes

- **feat**: Nueva funcionalidad
    
- **fix**: Corrección de errores
    
- **docs**: Cambios en documentación
    
- **style**: Formateo, punto y coma faltante, sin lógica afectada
    
- **refactor**: Refactorización de código sin agregar ni corregir funciones
    
- **perf**: Mejoras de rendimiento
    
- **test**: Añade o corrige tests
    
- **chore**: Tareas de mantenimiento (scripts, build, deps)
    

## Ámbitos (`scope`)

Define el área afectada, por ejemplo:

- `models`
    
- `views`
    
- `controllers`
    
- `data`
    
- `static`
    
- `manifest`
    

## Ejemplos de commits

1. **Commit principal de lanzamiento**
    
    text
    
    ```
    feat(manifest): inicializa módulo Helpdesk Professional v1.0.0
    ```
    
2. **Corrección de validación en tickets**
    
    text
    
    ```
    fix(models): valida que el usuario pertenezca al equipo en helpdesk_ticket
    ```
    
3. **Mejora de rendimiento en listado web**
    
    text
    
    ```
    perf(controllers): optimiza búsqueda paginada de tickets en portal
    ```
    
4. **Actualización de documentación**
    
    text
    
    ```
    docs(README): agrega sección de instalación y uso
    ```
    
5. **Tarea de mantenimiento**
    
    text
    
    ```
    chore(deps): actualiza versión de dependencias en manifest
    ```
