# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Category(models.Model):
    _name = 'hrskill.category'

    name=fields.Char(string="Name", required=True)
    description=fields.Text()
    skill_id=fields.One2many('hrskill.skills', 'category_id',string="Skills")

class Skills(models.Model):
    _name ='hrskill.skills'
    name=fields.Char(required=True)
    description=fields.Text()
    category_id=fields.Many2one('hrskill.category',onedelete='cascade',string="Category",required=False)


# class hrskill(models.Model):
#     _name = 'hrskill.hrskill'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
