from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

#modèle voyage class
class Voyage(models.Model):
    _name = "voyage"
    _description = "Voyage"
    
    #les attributs de la class Voyage 
    name= fields.Char(string="Nom du Voyage")
    dateDepart=fields.Date(string="Date de départ")
    destination=fields.Char(string="Destination")
