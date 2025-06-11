import json
from odoo import http 

class Estate(http.Controller):   
   
     # GET all estate properties
    @http.route('/api/estate', type='json', auth='public', methods=['GET'], csrf=False)
    def get_all(self):
        estates = http.request.env['estate.property'].sudo().search([])
        return [{
            'id': e.id,
            'name': e.name,
            'description': e.description,
            'expected_price': e.expected_price,
        } for e in estates]
    
    
    # GET one estate by id
    @http.route('/api/estate/<int:id>', type='json', auth='public', methods=['GET'], csrf=False)
    def get(self, id):
        estate = http.request.env['estate.property'].sudo().browse(id)
        if not estate.exists():
            return {'error':'Estate not found'}
        return {'id': estate.id, 'name': estate.name, 'description': estate.description, 'expected_price': estate.expected_price }
    

    # CREATE 
    @http.route('/api/estate', auth='public', type='json', methods=['POST'], csrf=False)
    def create(self):
        args = http.request.httprequest.data.decode()
        data = json.loads(args)
        estate = http.request.env['estate.property'].sudo().create(data)
        return { 'id': estate.id, 'message':'Estate created' }
    

    # UPDATE 
    @http.route('/api/estate/<int:id>', auth='public',  type='json', methods=['PUT'], csrf=False)
    def update(self, id):
        args = http.request.httprequest.data.decode()
        data = json.loads(args)
        estate = http.request.env['estate.property'].sudo().browse(id)
        if not estate.exists():
            return {'error':'Estate not found'}
        estate.write(data)
        return {'message': 'Estate updated'}
    
    # DELETE
    @http.route('/api/estate/<int:id>', auth='plubic', type='json', methods=['DELETE'], csrf=False)
    def delete(self, id):
        estate = http.requets.env['estate.property'].sudo().browse(id)
        if not estate.exists():
            return {'error': 'Estate not found'}
        estate.unlink()
        return {'message': 'Estate delete'}