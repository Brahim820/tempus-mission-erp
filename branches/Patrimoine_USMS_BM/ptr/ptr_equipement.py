from openerp.osv import osv, fields
from openerp import tools

class ptr_equipement(osv.osv):
	def _get_image(self, cr, uid, ids, name, args, context=None):
		result = dict.fromkeys(ids, False)
		for obj in self.browse(cr, uid, ids, context=context):
			result[obj.id] = tools.image_get_resized_images(obj.image)
		return result

	def _set_image(self, cr, uid, id, name, value, args, context=None):
		return self.write(cr, uid, [id], {'image': tools.image_resize_image_big(value)}, context=context)
	
	_name = 'ptr.equipement'
	_description = 'Class of Equipement'
	_columns = {
		'name': fields.char('Name'),
		'code': fields.integer('Code'),
		'note': fields.text('Note'),
		'image': fields.binary('Image'),
		'category_id': fields.many2one('ptr.equipement.category','Category'),
		'image_medium': fields.function(_get_image, fnct_inv=_set_image,string="Medium-sized image", type="binary", multi="_get_image",	store = {
											'ptr.equipement': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),},
											),
		'image_small': fields.function(_get_image, fnct_inv=_set_image,string="Smal-sized image", type="binary", multi="_get_image",store = {
											'ptr.equipement': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),},
											),
				}
	
ptr_equipement()
class ptr_equipement_category(osv.osv):
		
    _name = 'ptr.equipement.category'
    _description = 'Class of equipement category'
    _columns = {
        'name': fields.char('Name'),
		'description': fields.text('Description'),
		'code': fields.integer('Code'),
		
    }
ptr_equipement_category()

class ptr_equipement_code(osv.osv):
    _name = 'ptr.equipement.code'
    _description = 'Class of equipement codes'
    _columns = {
		'code': fields.integer('Code'),
		'equipement_id': fields.many2one('ptr.equipement','Equipement'),
	 }
ptr_equipement_code()

class ptr_equipements(osv.osv):
    _name = 'ptr.equipements'
    _description = 'Class of equipements'
    _columns = {
		'equipements_id': fields.many2one('ptr.equipement','Equipements'),
		#'code_ids': fields.one2many('ptr.equipement.code','equipement_id','Codes'),
		'local_id':fields.many2one('ptr.local','Local'),
		'quantity': fields.integer('Quantity'),
		
    }
ptr_equipements()
