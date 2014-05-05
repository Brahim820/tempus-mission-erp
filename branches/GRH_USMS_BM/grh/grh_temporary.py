from openerp import addons
import logging
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import tools


class grh_temporary(osv.osv):
	_name = 'grh.temporary'
	_columns = {
		'name_ar': fields.char("Arabic name",size=100),
		'lastname_ar': fields.char("Arabic last name",size=100),
		'name': fields.char("Name",size=100),
		'lastname': fields.char("Last name",size=100),
		'cin': fields.char("CIN",size=100),
		'passport': fields.char("Passport",size=100),
		'birthday': fields.date("Birthday"),
		'birth_place': fields.char("Place of birth",size=100),
		'gender': fields.selection([('male', 'Male'),('female', 'Female')], 'Gender'),
        'notes': fields.text('Notes'),
        'phone': fields.char("Phone number",size=100),
		'adress': fields.text("Adress"),
		'city': fields.char("city", size=100),
		'email': fields.char("Email",size=100),
		'photo': fields.binary("Photo"),
		}
grh_temporary();

