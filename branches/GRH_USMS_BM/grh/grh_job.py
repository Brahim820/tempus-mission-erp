from openerp import addons
import logging
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import tools


class grh_professor_job(osv.osv):
	_name = 'grh.professor.job'
	_columns = {
		'professor_id': fields.many2one("grh.professor","Professor"),
	
		'job': fields.many2one("grh.professor.poste","Job"),
		'grade': fields.char("Grade",size=100),
		'category': fields.char("Category",size=100),
		'scale': fields.integer("Scale"),
		'echelon': fields.integer("Echelon"),
		'scale_effect_date': fields.date("Date of scale effect"),
		'echelon_effect_date': fields.date("Date of scale effect"),
		'support': fields.binary("Support"),
		'current_state':fields.boolean("Current state"),
			}
grh_professor_job()

class grh_professor_poste(osv.osv):
	_name = 'grh.professor.poste'
	_columns = {
		'name': fields.char("Name",size=100),
		'professor_ids': fields.one2many("grh.professor.job","professor_id","Professors"),
		}
grh_professor_poste()

class grh_administrator_job(osv.osv):
	_name = 'grh.administrator.job'
	_columns = {
		'administrator_id': fields.many2one("grh.administrator","Administrator"),
	
		'job': fields.many2one("grh.administrator.poste","Job"),
		'grade': fields.char("Grade",size=100),
		'scale': fields.integer("Scale"),
		'echelon': fields.integer("Echelon"),
		'scale_effect_date': fields.date("Date of scale effect"),
		'echelon_effect_date': fields.date("Date of echelon effect"),
		'support': fields.binary("Support"),
		'current_state':fields.boolean("Current state"),
			}
grh_administrator_job()

class grh_administrator_poste(osv.osv):
	_name = 'grh.administrator.poste'
	_columns = {
		'administrator_ids': fields.one2many("grh.administrator.job","administrator_id","Administrators"),
		'name': fields.char("Name",size=100),
		
			}
grh_administrator_poste()

