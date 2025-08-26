odoo.define('helpdesk_web_form.dependent_service', function (require) {
    'use strict';
    const domReady = require('web.dom_ready');

    domReady(function () {
        const catSel = document.getElementById('category_id');
        const svcSel = document.getElementById('service_id');
        if (!catSel || !svcSel) return;

        function loadServices() {
            svcSel.innerHTML = '<option value="">Seleccione Servicio</option>';
            if (!catSel.value) return;
            fetch('/helpdesk/services', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({category_id: catSel.value})
            })
            .then(r => r.json())
            .then(data => {
                data.forEach(s => {
                    const opt = document.createElement('option');
                    opt.value = s.id;
                    opt.text = s.name;
                    svcSel.appendChild(opt);
                });
            });
        }

        catSel.addEventListener('change', loadServices);
        loadServices();
    });
});
