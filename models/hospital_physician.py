from odoo import models, fields

class HospitalPhysician(models.Model):
    _name = 'hospital.physician'
    _description = 'Hospital Physician'

    name = fields.Char(string="Physician Name", required=True)
    specialization = fields.Selection(
        [('cardiology', 'Cardiology'),
         ('neurology', 'Neurology'),
         ('orthopedics', 'Orthopedics'),
         ('pediatrics', 'Pediatrics'),
         ('general_medicine', 'General Medicine')],
        string="Specialization",
        required=True
    )
    contact_number = fields.Char(string="Contact Number")
    email = fields.Char(string="Email")
    hospital_id = fields.Many2one('res.partner', string="Hospital")
    specialization_ids = fields.Many2many('hospital.specialty', string="Specialties")
