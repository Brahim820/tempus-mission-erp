
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from openerp.osv import osv,fields
import logging
_logger = logging.getLogger(__name__)
class grh_professor_report_wizard(osv.osv_memory):
   
    
	_name = 'grh.professor.report.wizard'
	_columns = {
			'professor_id': fields.many2one('grh.professor', 'Professor'),
			'reason': fields.char("reason"),
			'address': fields.text("address"),
					}
	_defaults = {
			 'address': 'Address',
					}
	def print_report_test(self, cr, uid, ids, context=None):
			id=[record['professor_id'].id for record in self.browse(cr,uid,ids,context)]
			datas = {
				'ids': id,
				'model': 'grh.professor.report.wizard',
				'form': self.read(cr, uid, ids)[0]
			}
			print datas
			return {'type': 'ir.actions.report.xml', 
			'report_name': 'grh.professor.prof_certification_quittement_territory', 
			'datas': datas}

grh_professor_report_wizard()