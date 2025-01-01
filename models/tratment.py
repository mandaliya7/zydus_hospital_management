from odoo import models, fields, api

class Treatment(models.Model):
    _name = 'hospital.treatment'
    _description = 'Treatment'

    # Existing fields
    patient_id = fields.Many2one(
        'hospital.patient',
        string="Patient",
        required=True   ,
        help="The patient receiving the treatment"
    )
    physician_id = fields.Many2one(
        'hospital.physician',  # Assuming there is a 'hospital.physician' model
        string="Physician",
        required=True,
        help="The physician providing the treatment"
    )
    treatment_date = fields.Date(
        string="Treatment Date",
        required=True,
        default=fields.Date.context_today,  # Correct way to set today's date as default
        help="The date the treatment is given"
    )
    diagnosis_id = fields.One2many('hospital.diagnosis', 'treatment_id')


    # New state field with three states: draft, active, and done
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('done', 'Done'),
    ], string='Status', default='draft', required=True)

    def set_active(self):
        """Changes the state to 'active'."""
        if self.state == 'draft':
            self.write({'state': 'active'})

    def set_done(self):
        """Changes the state to 'done'."""
        if self.state == 'active':
            self.write({'state': 'done'})

    def smart(self):
        pass
