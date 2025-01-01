{
    'name': 'Hospital Management System',
    'version': '1.0',
    'category': 'Healthcare',
    'author': 'Harsh',
    'depends': ['base','sale'],
    'data': [
        'views/hospital_menu.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_physician_views.xml',
        'security/ir.model.access.csv',
        'views/hospital_specialty_views.xml',
        'views/hospital_treatment.xml',
        'views/hospital_disess.xml',
        'views/hospital_diagnosis.xml',
        'wizard/productwizard.xml',

    ],
    'installable': True,
    'application': True,
}

