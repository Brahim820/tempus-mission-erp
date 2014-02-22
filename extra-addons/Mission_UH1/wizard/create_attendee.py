
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

class CreateAttendeeWizard(osv.osv_memory):
    _name = 'mission.create.attendee.wizard'
    
    def _get_active_session(self, cr, uid, context):
        if context.get('active_model') == 'mission.session':
            return context.get('active_id', False)
        return False


    _columns = {
                'session_id': fields.many2one('mission.session', 'Session',required=True),
                'attendee_ids': fields.one2many('mission.attendee.wizard','wizard_id', 'Attendees'),
                }
    
    _defaults = {
                 'session_id': _get_active_session,
                 }

    def action_add_attendee(self, cr, uid, ids, context=None):
        attendee_model = self.pool.get('mission.attendee')
        wizard = self.browse(cr, uid, ids[0], context=context)
        for attendee in wizard.attendee_ids:
            attendee_model.create(cr, uid, {'partner_id': attendee.partner_id.id,'session_id': wizard.session_id.id,})
        return True

CreateAttendeeWizard()

class AttendeeWizard(osv.osv_memory):
    _name = 'mission.attendee.wizard'
    _columns = {
                'name':fields.char('Name', size=256),
                'partner_id':fields.many2one('res.partner', 'Partner', required=True),
                'wizard_id':fields.many2one('mission.create.attendee.wizard'),
                }
AttendeeWizard()