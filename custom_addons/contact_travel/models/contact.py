from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

#Contact Model class inherit from res.partner Model 
class Contact(models.Model):
    _inherit = "res.partner"
	