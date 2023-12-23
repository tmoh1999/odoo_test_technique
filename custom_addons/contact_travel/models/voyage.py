from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class Voyage(models.Model):
    _name = "voyage"
    _description = "Voyage"