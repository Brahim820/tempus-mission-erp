from openerp import addons
import logging
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import tools

def _get_department_prof_count(self,cr,uid,ids,fields,args,context=None):
	res = {}
	for record in self.browse(cr,uid,ids,context) :
		res[record.id] = len(record.professor_ids)
	return res
def _get_department_admin_count(self,cr,uid,ids,fields,args,context=None):
	res = {}
	for record in self.browse(cr,uid,ids,context) :
		res[record.id] = len(record.administrator_ids)
	return res
def _get_service_prof_count(self,cr,uid,ids,fields,args,context=None):
	res = {}
	for record in self.browse(cr,uid,ids,context) :
		res[record.id] = len(record.professor_ids)
	return res
def _get_service_admin_count(self,cr,uid,ids,fields,args,context=None):
	res = {}
	for record in self.browse(cr,uid,ids,context) :
		res[record.id] = len(record.administrator_ids)
	return res



class grh_department(osv.osv):
	_name = 'grh.department'
	_columns = {
		'name': fields.char("Nom",size=100),
		'leader_id':fields.many2one('grh.professor', 'Leader'),
		'secretary_id':fields.many2one('grh.administrator',string='Secretary'),
		'professor_ids': fields.one2many('grh.professor','department_id',string='Professors'),
		'professor_count':fields.function(_get_department_prof_count, type='integer', string='Professors count',store=True),
		'administrator_ids': fields.one2many('grh.administrator','department_id',string='Administrators'),
		'administrator_count':fields.function(_get_department_admin_count, type='integer', string='Administrators count',store=True),
		'logo': fields.binary("Logo of department"),
		'notes': fields.text('Notes')
		}
grh_department()

class grh_service(osv.osv):
	_name = 'grh.service'
	_columns = {
		'name': fields.char("Nom",size=100),
		'responsible_id':fields.many2one('grh.administrator', 'Responsible'),
		'department_id':fields.many2one('grh.department',string='Department'),
		'professor_ids': fields.one2many('grh.professor','service_id',string='Professors'),
		'professor_count':fields.function(_get_service_prof_count, type='integer', string='Professors count',store=True),
		'administrator_ids': fields.one2many('grh.administrator','service_id',string='Administrators'),
		'administrator_count':fields.function(_get_service_admin_count, type='integer', string='Administrators count',store=True),
		'notes': fields.text('Notes'),
			}
grh_service()


