from openerp.osv import osv, fields
from openerp import tools


class ptr_etablissement(osv.osv):
	def _get_image(self, cr, uid, ids, name, args, context=None):
		result = dict.fromkeys(ids, False)
		for obj in self.browse(cr, uid, ids, context=context):
			result[obj.id] = tools.image_get_resized_images(obj.image)
		return result

	def _set_image(self, cr, uid, id, name, value, args, context=None):
		return self.write(cr, uid, [id], {'image': tools.image_resize_image_big(value)}, context=context)

	_name = 'ptr.establissement'
	_description = "Class of establissement"
	_columns = {
        'name': fields.char('Name'),
		'code': fields.integer('Code'),
		'note': fields.text('Note'),
		'image': fields.binary('image'),
		'local_ids': fields.one2many('ptr.local','etablissement_id','Locals'),
		'dep_ids': fields.one2many('ptr.departement','estabissement_id','Departement'),
		'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="Medium-sized image", type="binary", multi="_get_image",
            store = {
                'ptr.establissement': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Medium-sized photo of the establissement. It is automatically "\
                 "resized as a 128x128px image, with aspect ratio preserved. "\
                 "Use this field in form views or some kanban views."),
		'image_small': fields.function(_get_image, fnct_inv=_set_image,
            string="Smal-sized image", type="binary", multi="_get_image",
            store = {
                'ptr.establissement': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Small-sized photo of the establissement. It is automatically "\
                 "resized as a 64x64px image, with aspect ratio preserved. "\
                 "Use this field anywhere a small image is required."),
					}
ptr_etablissement()