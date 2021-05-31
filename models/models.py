# -*- coding: utf-8 -*-
from odoo import fields, models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_contract = fields.Boolean(string="Contract signed")
    contract_date = fields.Date(string="Contract date")
    contract_details = fields.Char(string="Contract details")
    planned_income = fields.Float(string="Planned revenue")
    add_install = fields.One2many(string="Instalacja", comodel_name="crm.install", inverse_name="lead_id")


class CrmInstall(models.Model):
    _name = 'crm.install'

    lead_id = fields.Many2one(comodel_name='crm.lead', string='Szansa')
    name = fields.Char(string="Nazwa")
    data = fields.Date(string="Data montazu")
    qty = fields.Integer(string="Wielkosc")
    vol = fields.Float(string="Zysk")



