from openerp import addons
import logging
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import tools



class grh_administrator(osv.osv):
	def _get_image(self, cr, uid, ids, name, args, context=None):
		result = dict.fromkeys(ids, False)
		for obj in self.browse(cr, uid, ids, context=context):
			result[obj.id] = tools.image_get_resized_images(obj.image)
		return result

	def _set_image(self, cr, uid, id, name, value, args, context=None):
		return self.write(cr, uid, [id], {'image': tools.image_resize_image_big(value)}, context=context)
	
	def _admin_name_get_fnc(self, cr, uid, ids, fields, args, context=None):
			res = {}
			for record in self.browse(cr, uid, ids, context=context):
				res[record.id] = record['name'] +' '+record['lastname']
			return res
			
	def _admin_current_state_get_fnc(self, cr, uid, ids,fields, args, context=None):
			res ={}
			obj = self.pool.get('grh.administrator.job')
			ids = obj.search(cr, uid, [('current_state','=',True)])
			for record in obj.browse(cr, uid, ids, context):
				if args=='job':
					res[record.id]=record[args].name
				else:
					res[record.id]=record[args]
			return res
			
	_name = 'grh.administrator'
	_columns = {
	#image
		'image': fields.binary("Photo"),
			
		'image_medium': fields.function(_get_image, fnct_inv=_set_image,
				string="Medium-sized image", type="binary", multi="_get_image",
				store = {'grh.administrator': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),},
					),
		'image_small': fields.function(_get_image, fnct_inv=_set_image,
				string="Smal-sized image", type="binary", multi="_get_image",
				store = {'grh.administrator': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10), },            
					),	
	
	#tools
		'complete_name': fields.function(_admin_name_get_fnc, type="char", string='Full name',store=True, readonly=True),
	#personnel informations
		'name_ar': fields.char("Arabic name",size=100),
		'lastname_ar': fields.char("Arabic last name",size=100),
		'name': fields.char("Name",size=100),
		'lastname': fields.char("Last name",size=100),
		'cin': fields.char("CIN",size=100),
		'passport': fields.char("Passport",size=100),
		'birthday': fields.date("Birthday"),
		'birth_place': fields.char("Place of birth",size=100),
		'gender': fields.selection([('male', 'Male'),('female', 'Female')], 'Gender'),
        'marital': fields.selection([('single', 'Single'), ('married', 'Married'), ('widower', 'Widower'), ('divorced', 'Divorced')], 'Marital Status'),
        'num_children': fields.integer("Number of children"),
		'phone': fields.char("Phone number",size=100),
		'adress': fields.text("Adress"),
		'city': fields.char("city", size=100),
		'email': fields.char("Email",size=100),
		'notes': fields.text('Notes'),
        
	#work informations
		'department_id': fields.many2one('grh.department','Department'),
		'service_id': fields.many2one('grh.service','Service'),
		'office_localisation': fields.char("Office localisation"),
		'office_station':fields.integer("Number of station"),
		'work_fleet': fields.char("Work phone",size=100),
		'work_email': fields.char("Work e-mail",size=100),
	#job information
		'doti': fields.integer("S.O.M"),
		'pb': fields.integer("Budget item"),
		'recruitment_date':fields.date("Date of recruitment"),
		
	#Current state
		'job': fields.function(_admin_current_state_get_fnc,'job', type="char", string='Job',store=True, readonly=True),
		'grade': fields.function(_admin_current_state_get_fnc,'grade', type="char", string='Grade',store=True, readonly=True),
		'scale': fields.function(_admin_current_state_get_fnc,'scale', type="integer", string='Scale',store=True, readonly=True),
		'echelon': fields.function(_admin_current_state_get_fnc,'echelon', type="integer", string='Echelon',store=True, readonly=True),
		'scale_effect_date': fields.function(_admin_current_state_get_fnc,'scale_effect_date', type="date", string='Date of scale effect',store=True, readonly=True),
		'echelon_effect_date': fields.function(_admin_current_state_get_fnc,'echelon_effect_date', type="date", string='Date of echelon effect',store=True, readonly=True),
		
		#Proposal state
		'job_prop': fields.char("Proposal job "),
		'grade_prop': fields.char("Proposal grade"),
		'category_prop': fields.char("Proposal category"),
		'scale_prop': fields.integer("Proposal scale"),
		'echelon_prop': fields.integer("Proposal echelon"),
		'next_prop_date': fields.date("Date of next proposal"),
		#History
		'job_ids': fields.one2many('grh.administrator.job', 'administrator_id', 'Jobs'),
		#Studies
		'studies_ids': fields.one2many('grh.administrator.diploma', 'administrator_id', 'Diploma'),
			}
	_order = "complete_name"
	_rec_name = "complete_name"
grh_administrator();



