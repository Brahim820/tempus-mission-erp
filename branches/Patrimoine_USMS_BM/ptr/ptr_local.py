from openerp.osv import osv, fields
class ptr_local(osv.osv):
    _name = 'ptr.local'
    _description = 'Class of local'
    _columns = {
        'name': fields.char('Name'),
		'etablissement_id':fields.many2one('ptr.establissement','Etablissement'),
		'departement_id':fields.many2one('ptr.departement','Departement'),
		'code': fields.integer('Code'),
		'note': fields.text('Note'),
		'seats': fields.integer('Seats'),
		'equipement_ids': fields.one2many('ptr.equipements','local_id','Equipements'),
		'category_id': fields.many2one('ptr.local.category','Category'),
		
    }
ptr_local()
class ptr_local_category(osv.osv):
    _name = 'ptr.local.category'
    _description = 'Class of local category'
    _columns = {
        'name': fields.char('Name'),
		'description': fields.text('Description'),
		'code': fields.integer('Code'),
    }
ptr_local_category()