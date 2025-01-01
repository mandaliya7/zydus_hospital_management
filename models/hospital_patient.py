from odoo import models, fields, api
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherits = {'res.users' : 'user_id'}

    patient_name = fields.Char('Patient Name')
    age = fields.Integer('Age', compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'Gender')
    contact_number = fields.Char('Contact Number')
    email = fields.Char('Email')
    date_of_birth = fields.Date('Date of Birth')
    user_id = fields.Many2one('res.users',string='Releted user')
    # This is a computed field. It will not be manually set.
    # user_count = fields.Integer(string="User Count", compute='_compute_user_count', store=False)

    @api.depends('date_of_birth')  # Recompute the age when date_of_birth changes
    def _compute_age(self):
        """
        Compute the age of the patient based on their date_of_birth.
        """
        today = date.today()
        for record in self:
            if record.date_of_birth:
                birth_date = fields.Date.from_string(record.date_of_birth)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0  # If no date_of_birth is provided, age is 0

    @api.model
    def create(self, vals):
        vals['name'] = vals.get('patient_name')
        vals['login'] = vals.get('email')
        return super(HospitalPatient,self).create(vals)
