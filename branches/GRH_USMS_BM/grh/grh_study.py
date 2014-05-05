from openerp import addons
import logging
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import tools


class grh_professor_diploma(osv.osv):
	_name = 'grh.professor.diploma'
	_columns = {
		'professor_id': fields.many2one("grh.professor","Professor"),
		'diploma': fields.char("Diploma"),
		'graduation_date': fields.date("Date of graduation"),
		'establishment': fields.char("Establishment"),
		'city': fields.char("City"),
		'support': fields.binary("Support"),
			}
grh_professor_diploma()

class grh_administrator_dip(osv.osv):
	_name = 'grh.administrator.diploma'
	_columns = {
		'administrator_id': fields.many2one("grh.administrator","Administrator"),
		'diploma': fields.char("Diploma"),
		'graduation_date': fields.date("Date of graduation"),
		'establishment': fields.char("Establishment"),
		'city': fields.char("City"),
		'support': fields.binary("Support"),
			}
grh_administrator_dip()