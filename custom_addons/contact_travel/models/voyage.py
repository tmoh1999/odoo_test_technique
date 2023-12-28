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
    montant=fields.Float(string="Montant Voyage")
    
    #Many2one attribute : a link between res.partner Model and Voyage Model 
    #res.partner Contact can have a list of voyages .     
    voyageur_id=fields.Many2one('res.partner', string='Contact')
    


    @api.model
    def create(self, vals):
        self.caclNivRecompense(vals)
        res=super(Voyage,self).create(vals)
        return res

    def caclNivRecompense(self,vals):
        field_voy_contact = self.env['voyage'].search([('voyageur_id','=',vals["voyageur_id"])])
        
        mont_glob=vals["montant"]
        for vg in field_voy_contact:
            mont_glob+=vg.montant
            
        recomp=""
        if mont_glob>=100000:
            recomp= "platin"
        elif mont_glob>=50000:   
            recomp= "or"
        elif mont_glob>=20000:
            recomp= "argent"
            
        self.env['res.partner'].search([('id','=',vals["voyageur_id"])]).nivrecompense=recomp
        
            
    