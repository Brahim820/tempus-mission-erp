
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

class Newdipfiliere(osv.osv):
    
    _name = 'inscrits.newdipfiliere' 
    
    _description = 'Effectif des nouveaux inscrits par diplome et par filiere' 

    def _get_inscrits_global(self, cr, uid, ids, fields, args, context=None):
        res = {}

        for course in self.browse(cr, uid, ids, context=context):
            num=0
            for session in course.session_ids:
                num+=len(session.attendee_ids)
            res[course.id] = num
        return res
    
    _columns = {
              'cod_etab':fields.char(string='Code Etab', size=256),
              'lib_etab':fields.text('libelle etablissement'),
              'cod_dip':fields.char(string='Code diplome', size=256),
              'lib_dip':fields.text('libelle diplome'),
              'cod_fil':fields.char(string='Code filiere', size=256),
              'lib_fil':fields.text('libelle filiere'),
              'annee':fields.integer('Annee'),
              'nbr':fields.integer('Effectif des Inscrits'),
                }
    
Newdipfiliere()