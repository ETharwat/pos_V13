# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeYearOfExperiance(http.Controller):
#     @http.route('/employee_year_of_experiance/employee_year_of_experiance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_year_of_experiance/employee_year_of_experiance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_year_of_experiance.listing', {
#             'root': '/employee_year_of_experiance/employee_year_of_experiance',
#             'objects': http.request.env['employee_year_of_experiance.employee_year_of_experiance'].search([]),
#         })

#     @http.route('/employee_year_of_experiance/employee_year_of_experiance/objects/<model("employee_year_of_experiance.employee_year_of_experiance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_year_of_experiance.object', {
#             'object': obj
#         })
