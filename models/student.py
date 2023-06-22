


from odoo import fields, models


class Student(models.Model):
    _name = 'test.student'
    _description = 'student table'
    name = fields.Char('Name', required=True, translate=True,)
    age = fields.Integer('age', required=True,)
    address = fields.Char('address', required=True,)


    def get_all_student(self):
       data =  self.env['test.student'].search([])
       return  data



    def get_student_by_id(self, id ):
        return self.search([('id','=', id)])

    def update(self, id , student):
        record = self.sudo().search([('id', '=', id)])
        return record.sudo().write(student)
    def create_student(self , student):
        self.sudo().create(student)
        return 1



