# coding: utf-8
# Copyright (C) 2014-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'CAE - Company Wizard - Account',
    'version': '10.0.1.0.0',
    'category': 'CAE',
    'summary': 'Glue Module between CAE and Company Wizard - Account modules',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'fiscal_company_account',
        'company_wizard_account',
    ],
    'installable': True,
    'auto_install': True,
}
