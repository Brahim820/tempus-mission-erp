
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

class Globalprov(osv.osv):
    
    _name = 'inscrits.globalprov' 
    
    _description = 'Effectif global des inscrits par province' 

    _columns = {
              'cod_etab':fields.char(string='Code Etab', size=256),
              'lib_etab':fields.text('libelle etablissement'),
              'cod_prov':fields.char(string='Code province', size=256),
              'lib_prov':fields.text('libelle province'),
              'annee':fields.integer('Annee'),
              'nbr':fields.integer('Effectif des Inscrits'),
                }
    
Globalprov()