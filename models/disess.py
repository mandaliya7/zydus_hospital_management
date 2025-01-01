from odoo import models, fields

class Hospitaldisess(models.Model):
    _name = 'hospital.disess'
    _description = 'disess'

    name = fields.Char(string="disess Name", required=True)
    code = fields.Char(string="disess Code", required=True, unique=True)
