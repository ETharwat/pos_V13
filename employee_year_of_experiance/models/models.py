
# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime
from dateutil import relativedelta


class Employee(models.Model):
    _inherit = 'hr.employee'

    joining_date = fields.Date('Joining Date')
    year_of_experience = fields.Char('Year of Experience',compute="_compute_year_of_experience",store=True)

    @api.depends('joining_date')
    def _compute_year_of_experience(self):
        for rec in self:
            if rec.joining_date:
                different_dates = relativedelta.relativedelta(datetime.today().date(),rec.joining_date)
                rec.year_of_experience = "%s days, %s months and %s years"%(different_dates.days,different_dates.months,different_dates.years)
