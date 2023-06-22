import json

from odoo import http
from odoo.http import request  , route , Response

class StudentController(http.Controller):

    @route('/student', auth='public', type='http')

    def getAll(self):
        students = request.env['test.student'].get_all_student()

        list = []
        for st in students:
            list.append({"id" :st.id, "name":st.name,"age":st.age ,"address":st.address})

        return Response(response=json.dumps(list),status=200)

    @route('/student/<int:id>', type='http', auth='public', Website=True)
    def get_by_id(self, id , **kwargs):
        student = request.env['test.student'].get_student_by_id(id)
        if(not student.id):
            return Response(response="not found" ,status=400)

        data = {"id": student.id,
                "name": student.name,
                "age": student.age,
                "address": student.address}
        return Response(response=json.dumps(data), status=200)


    @route('/student/create', auth='none' , type='json' , csrf=False)
    def create(self  , student):
        students = request.env['test.student'].create_student(student)
        return Response(response=students, status=200)

    @route('/student/update/<int:id>', auth='none', type='json', csrf=False)
    def update(self, id , student , **kwargs):
        students = request.env['test.student'].update(id,student)
        return Response(response=students, status=200)

