
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
#    along with this program.  If not, see http://www.gnu.org/licenCourse(ses/.
#
##############################################################################
from openerp.osv import osv,fields

class Course(osv.osv):
    
    _name = 'mission.course' 
    
    _description = 'description of course' 
    
    def _get_attendee_count(self, cr, uid, ids, fields, args, context=None):
        res = {}
        for course in self.browse(cr, uid, ids, context=context):
            num=0
            for session in course.session_ids:
                num+=len(session.attendee_ids)
            res[course.id] = num
        return res
    
    _columns = {
              'name':fields.char('Title', size=64, required=True, readonly=False),
              'description':fields.text('Description'), 
              'responsible_id':fields.many2one('res.users', 'Responsible', required=False), 
              'session_ids':fields.one2many('mission.session', 'course_id', 'Sessions', required=False),
              'attendee_count': fields.function(_get_attendee_count,type='integer', string='Attendee Count'),
                }
    
    def _check_name(self, cr, uid, ids,context=None): 

        for course in self.browse(cr,uid,ids,context):
            if course.name == course.description :
                return False
        return True
   
    _constraints = [(_check_name, 'Attention:the course description and the course title are the same', ['name','description']),] 
    
    _sql_constraints = [('name_uniq', 'unique(name)', 'The Name of the Course must be unique !'),]
    
    
    def copy(self, cr, uid, id,vals, context=None):
        
        name_course = self.browse(cr,uid,id,context).name
        
        new_name = name_course+' '+'Copy'
        
        vals['name'] = new_name
        
        return super(Course, self).copy(cr, uid, id,vals, context)
 
    
Course()