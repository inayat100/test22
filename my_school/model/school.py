from odoo import models ,fields

class School(models.Model):
    _name = "schoolm"

    name = fields.Char("School Name")
    code = fields.Char("school Code")
    student_id = fields.Many2one("studentm","Student Id")
    booking_date = fields.Date("Date For Booking")
