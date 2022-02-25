# -*- coding: utf-8 -*-

#from typing_extensions import Required
#from unicodedata import name
from os import times
from time import time
from odoo import models, fields, api

class Course(models.Model):
    _name='open_academy.course'
    _description='course'
    name=fields.Char(string='Title',required=True)
    description=fields.Text()
    
 