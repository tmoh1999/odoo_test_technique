from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError

#Contact Model class inherit from res.partner Model 
class Contact(models.Model):
    _inherit = "res.partner"

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