# -*- coding: utf-8 -*-
from odoo import fields, models

class CrmLeadPlus(models.Model):
    _inherit = 'crm.lead'

    is_contract = fields.Boolean(string="Contract signed")
    contract_date = fields.Date(string="Contract date")
    contract_details = fields.Char(string="Contract details")
    planned_income = fields.Float(string="Planned revenue")