
{
    "name": "Fake Store",
    "version": "17.0.1.0.0",
    "summary": "Integración de productos con Fake Store API",
    "author": "Aura martinez",
    "depends": [
        'base', 'product', 'website'
    ],
    "data": [
        "views/res_company_inh.xml",
        "security/ir.model.access.csv",
        "data/fake_store_cron.xml",
        "views/producto_inh.xml",
        "views/boton_web.xml",
    ],
    "installable": True,
    "auto_install": False,
}
