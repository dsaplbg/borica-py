{
    'name': 'Borica Payment Provider',
    'version': '16.0.1.0.0',
    'summary': 'Integrate Borica Payment Gateway (CGI Interface) with Odoo 16',
    'description': """
        Allows customers to pay via Borica's secure payment gateway using the CGI Interface.
        Supports Sale and Pre-authorization flows.
        Requires configuration of Terminal ID, Merchant Private Key, and Borica Public Key/Certificate.

        **Note:** Requires the 'cryptography' Python library.
        Install using: pip install cryptography
    """,
    'category': 'Accounting/Payment Providers',
    'author': 'DSAPLBG', # Replace with your details
    'depends': ['payment'], # Correct dependency for Odoo 16
    'data': [
        'security/ir.model.access.csv',
        'views/payment_borica_templates.xml',
        'views/payment_provider_views.xml',
        'views/borica_redirect_page.xml',
        'data/payment_provider_data.xml',
        # Add security rules if storing keys needs specific access
    ],
    # --- Assets ---
    # Register frontend assets (JavaScript/CSS)
    'assets': {
        'web.assets_frontend': [
            # Path to the JavaScript file relative to the module root
            'payment_borica/static/src/js/borica_payment_form.js',
        ],
        # Add backend assets here if needed (e.g., custom CSS for config view)
        # 'web.assets_backend': [
        #     'payment_borica/static/src/scss/backend_styles.scss',
        # ],
    },
    'external_dependencies': {
        'python': ['cryptography'], # Declare external Python dependency
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}