# -*- coding: utf-8 -*-
from odoo import models, fields


class MicahModel(models.Model):
    _name = 'mmm'

    name = fields.Char(string='Name')
