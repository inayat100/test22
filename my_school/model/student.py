from odoo import models ,fields,api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = "studentm"

    # @api.onchange('Number')
    # def _onchange_(self):
    #     ("++++++++++++++++++++++++++++++++++++++++++++",self.Number)
    #     l = self.Number
    #     if int(l)>12:
    #         raise ValidationError("Number digits is more then 12")
    
    def all_show(self):
       br = self.browse([3])
       print(br)

    def join_hospital(self):
        data = {
            'image':self.image,
            'name':self.name,
            'last_name':self.l_name,
            'age':self.age,
            'gender':self.gender,
            'email':self.email,
            'city':self.city,
            'state':self.state,
            'country':self.country
        }
        self.env['selectstudent'].create(data)
        sr = self.env['selectstudent'].search([])
        for i in sr:
            print(i.id)

        



        # sr = self.env['studentm'].search(['|',('gender','=','male'),('name','=','saba')])
        # sr = self.env['studentm'].search([])
        # print(sr)
        # for i in sr:
        #     if i.id == 6:
        #         print("---------------deleted--------------------",i)
        #         i.unlink()
        #         continue
        #     print("Name -------------------",i.name,i.gender)
        
    @api.onchange('age')
    def _onchange_(self):
        ag = int(self.age)
        print("##################---------------####################",self.age)
        if ag >= 18:
            print("##################---------------####################",type(self.age),type(ag))
            self.result = "You Can Drive"
        else:
            self.result = "Sorrry You Can't Drive"
            
    @api.depends('sem1','sem2')
    def compute_total(self):
        print("=================================")
        t = self.sem1+self.sem2
        self.update({'total':t})



    image = fields.Binary("Image")
    name = fields.Char(string="First Name")
    l_name = fields.Char(string="last Name")
    age = fields.Char(string="age")
    gender = fields.Selection([("male","MALE"),("female","FEMALE")],"Gender")
    Number = fields.Char(string="Number")
    email = fields.Char(string="E-mail")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    country = fields.Char("Country")
    result = fields.Char("Eligibility")
    sem1 = fields.Integer("Sem1")
    sem2 = fields.Integer("Sem2")
    total = fields.Integer("Total No",compute="compute_total",store=True)
    choice_hospital = fields.Many2one("hospital","Choice Hospital")
    


    # booking_date = fields.Date("Date For Leave")
    # leave_day = fields.One2many("student.leave","leaves","Leave Day")

# class Leave(models.Model):
#     _name = "student.leave"

#     leaves = fields.Many2one("studentm","Leave") #pppp
#     booking_date = fields.Date("Date For Leave") #bbb




