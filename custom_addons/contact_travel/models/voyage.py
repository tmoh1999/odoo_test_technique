from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

#Voyage Model class 
class Voyage(models.Model):
    _name = "voyage"
    _description = "Voyage"
    
    #Voyage Model Class attributes 
    name= fields.Char(string="Nom du Voyage")
    dateDepart=fields.Datetime(string="Date de départ", default=fields.Datetime.now)
    destination=fields.Char(string="Destination")
    
    #Many2one attribute : a link between res.partner Model and Voyage Model 
    #res.partner Contact can have a list of voyages .     
    voyageur_id=fields.Many2one('res.partner', string='Contact')