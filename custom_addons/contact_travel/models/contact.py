from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

#Contact Model class inherit from res.partner Model 
class Contact(models.Model):
    _inherit = "res.partner"
    
    
    #NOTE:Règles métiers
    ##  if nivrecompense>20000:  le client atteint le niveau Argent
    ##  if nivrecompense>50000:  le client atteint le niveau Or
    ##  if nivrecompense>100000: le client atteint le niveau Platin
        
    nivrecompense = fields.Selection([('argent','Argent'),('or','Or'),('platin','Platin'),],string="Niveaux de récompense")
    
    #Field to display number voyages of the res.partner contact
    vlabel = fields.Char(string="0" ,compute="nbvoyage")
    
    
    
    
    # Method liste_voyages fetchs all voayages of the res.partner contact and the result
    ## is used to create a domain using ids of the voyages.
    # After that it search for the id of the view tree  using the name voyage.tree.
    # Finaly the method returns an action ir.actions.act_window the displays
    ## all of the voyages of the contact in a tree view.
            
    def liste_voyages(self):
        field_ids = self.env['voyage'].search([('voyageur_id','=',self.id)]).ids
        
        domain = [('id','in',field_ids)]

        view_id_tree = self.env['ir.ui.view'].search([('name','=',"voyage.tree")])
        return {
            'name':"Liste des Voyages",
            'type': 'ir.actions.act_window',
            'res_model': 'voyage',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'views': [(view_id_tree[0].id, 'tree'),(False,'form')],
            'view_id ref="contact_travel.tree_view"': '',
            'target': 'current',
            'domain': domain,
        }
    
    #Method nbvoyage search for all voyages related to the res.partner Contact
    #the result of the search is list of ids of the voyages
    #this result is used to change the value of the vlabel field to the lenght of the result.       
    def nbvoyage(self):
        field_ids = self.env['voyage'].search([('voyageur_id','=',self.id)]).ids
        self.vlabel=str(len(field_ids)) 
        