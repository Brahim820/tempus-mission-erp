# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name' : 'Patrimoin',
    'version' : '1.1',
    'author' : 'I.BADI',
    'category' : '',
    'description' : """
Module de gestion du patrimoin de l'USMS.
=============================================

ce module couvre les éléments suivants:
--------------------------------------------
    * Gestion des locaux
    * Gestion des équipements
   """,
    'website': 'http://www.usms.ma',
    'images' : [],
    'depends' : ['base'],
    'data': [],
    'update_xml': ['ptr_etablissement_view.xml',
	               'ptr_local_view.xml',
				   'ptr_equipement_view.xml',
						],
    'js': [],
    'qweb' : [],
    'css':['static/css/ptr_establissement.css'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
