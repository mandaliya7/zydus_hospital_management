from odoo import models, fields


class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Hospital Diagnosis'

    name = fields.Char(string='Diagnosis Name')
    disess_id = fields.Many2one('hospital.disess', string='Disease', required=True)
    diagnosis_date = fields.Date(string='Diagnosis Date', default=fields.Date.today)
    diagnosis_type = fields.Selection(
        [('high', 'High'), ('medium', 'Medium'), ('low', 'Low')],
        string='Diagnosis Type'
    )
    user_id = fields.Many2one('res.users', string='Responsible User')

    treatment_id = fields.Many2one('hospital.treatment', required=True)

