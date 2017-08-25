# -*- coding: utf-8 -*-
from odoo import fields, models

class fal_product_template(models.Model):
    _inherit = 'product.template'

    fal_jenis = fields.Selection([
        ('hatchback', "Hatchback"),
        ('sedan', "Sedan"),
        ('suv', "Sport Utility Vehicle (SUV)"),
        ('mpv', "Multi Purpose Vehicle (MPV)"),
    ], string="Jenis")

    fal_mesin = fields.Char(string="Machine")
    fal_seat = fields.Integer(string="Number of seats")
    fal_colour = fields.Char(string="Colour")
    fal_description = fields.Text(string="Description")
