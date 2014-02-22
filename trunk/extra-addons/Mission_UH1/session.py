
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
from openerp.tools.translate import _
import time


class Session(osv.osv):
   
    _name = "mission.session"
    
    
    def _get_taken_set_percent(self,seats,attendee_ids) :
        print seats,len(attendee_ids)
        return seats and ((100*len(attendee_ids))/seats) or 0
    
    def _get_taken_set(self,cr,uid,ids,fields,args,context=None):
        
        result = {}
        
        for session in self.browse(cr,uid,ids,context) :
            result[session.id] = self._get_taken_set_percent(session.seats,session.attendee_ids)
        print "result",result
        return result

    def _get_attendee_count(self,cr,uid,ids,fields,args,context=None):
        
        result = {}
        
        for session in self.browse(cr,uid,ids,context) :
            result[session.id] = len(session.attendee_ids)
        return result

    _columns = {
        'name' : fields.char(string="Name", size=256, required=True),
        'start_date' : fields.date(string="Start date"),
        'duration' : fields.float(string="Duration", digits=(6,2),help="Duration in days"),
        'seats' : fields.integer(string="Number of seats"),
        'course_id':fields.many2one('mission.course', 'Course', required=False), 
        'attendee_ids':fields.one2many('mission.attendee', 'session_id', 'Attenddees', required=False),
        'instructor_id' : fields.many2one('res.partner', string="Instructor"),
        'taken_seats': fields.function(_get_taken_set, type='integer', string='Taken Seats'), 
        'active':fields.boolean('Active', required=False), 
        'attendee_count': fields.function(_get_attendee_count, type='integer', string='Number of Attendee',store=True), 
        'state':fields.selection([('draft','Draft'),('confirmed','Confirmed'),('done','Done'),],'State', readonly=True),
    }
    
    
    _defaults = {  
        'start_date': lambda *a: time.strftime('%Y-%m-%d'),  
        'active':True,
        'state':'draft',
        }
    
    
    def on_change_percent_takens_seats(self,cr,uid,ids,seats,attendee):
        
        vals = {'value':{'taken_seats':self._get_taken_set_percent(seats, attendee)}}
        
        if seats < 0:
            vals['warning'] = {'title':'Warning','message':'attention the number of seats is under zero'}
        
        return vals
    
    def create(self, cr, uid, vals, context=None):
        
        if 'seats' in vals.keys() and vals['seats'] < 0:
            raise osv.except_osv(_('error!'),_("the number of seats is under zero !!!."))        
        
        return super(Session, self).create(cr, uid, vals, context)

    
    def write(self, cr, uid, ids, vals, context=None):
        
        res = super(Session, self).write(cr, uid, ids, vals, context=context)
        
        if 'seats' in vals.keys() :
            val_seat = vals['seats']
        
            if val_seat < 0 :
                raise osv.except_osv(_('error!'),_("the number of seats is under zero !!!."))
        return res
    
    def action_draft(self, cr, uid, ids, context=None):
        # set to "draft" state
        return self.write(cr, uid, ids, {'state': 'draft'}, context=context)
    def action_confirm(self, cr, uid, ids, context=None):
        # set to "confirmed" state
        return self.write(cr, uid, ids, {'state': 'confirmed'}, context=context)
    def action_done(self, cr, uid, ids, context=None):
        # set to "done" state
        return self.write(cr, uid, ids, {'state': 'done'}, context=context)
   
Session()