# coding: utf-8
# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author Julien WESTE
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestAccountFiscalCompany(TransactionCase):
    """Tests for Account Fiscal Company Module"""

    def setUp(self):
        super(TestAccountFiscalCompany, self).setUp()
        self.company_obj = self.env['res.company']
        self.category_obj = self.env['product.category']

        self.mother_company = self.env.ref(
            'base_fiscal_company.company_fiscal_mother')
        #        self.child_company = self.env.ref(
        #            'base_fiscal_company.company_fiscal_child_1')
        self.product_category_all = self.env.ref(
            'product.product_category_all')
        self.account_expense_cae = self.env.ref(
            'account_fiscal_company.account_expense_cae')
        self.account_income_cae = self.env.ref(
            'account_fiscal_company.account_income_cae')

    # Test Section
    def test_01_account_property_propagation_new_company(self):
        """Create a new child company must propagate categories properties"""

        # Create a new Child company
        company = self.company_obj.create({
            'name': 'Your Test Child Company',
            'code': 'CTS',
            'fiscal_type': 'fiscal_child',
            'fiscal_company': self.mother_company.id,
            'parent_id': self.mother_company.id,
        })

        
        # Change current company and load category with the new context
        self.env.user.company_id = company.id
        category = self.category_obj.browse([self.product_category_all.id])

        # Check if properties has been propagated to the new company
        self.assertEqual(
            category.property_account_expense_categ_id.id,
            self.account_expense_cae.id,
            "Create a new child company must set expense account property"
            " of the mother company to the new child company.")

        self.assertEqual(
            category.property_account_income_categ_id.id,
            self.account_income_cae.id,
            "Create a new child company must set income account property"
            " of the mother company to the new child company.")

#    # Test Section
#    def test_02_account_property_propagation_change_value(self):
#        """Change a property of a fiscal company must change the value
#        for all other child company"""

#        cr, uid = self.cr, self.uid
#        # Change current company
#        self.ru_obj.write(cr, uid, [uid], {
#            'company_id': self.mother_company_id,
#        })

#        self.pc_obj.write(cr, uid, [self.product_category_all_id], {
#            'property_account_expense_categ': self.account_income_cis_id,
#            'property_account_income_categ': self.account_expense_cis_id})

#        # Change current company
#        self.ru_obj.write(cr, uid, [uid], {
#            'company_id': self.child_company_id,
#        })

#        pc = self.pc_obj.browse(cr, uid, self.product_category_all_id)

#        # Check if properties has been propagated to the other company
#        self.assertEqual(
#            pc.property_account_expense_categ.id,
#            self.account_income_cis_id,
#            "Change an expense property for a category in a fiscal company"
#            " must change the value for all the other fiscal company.")

#        self.assertEqual(
#            pc.property_account_income_categ.id,
#            self.account_expense_cis_id,
#            "Change an income property for a category in a fiscal company"
#            " must change the value for all the other fiscal company.")
