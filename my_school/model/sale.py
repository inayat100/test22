from odoo import models , fields,api
from datetime import date

class Sale(models.Model):
    _inherit = "sale.order"
    till_date = fields.Date("Till Date")

    



class SaleLine(models.Model):
    _inherit = "sale.order.line"
    # date = fields.Date("Date",default=date.today())
    till_date = fields.Date("Till Date")


