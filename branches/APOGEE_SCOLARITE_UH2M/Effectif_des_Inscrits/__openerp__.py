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

{
    "name": "APOGEE - SCOLARITE",
    "version": "1.0",
    "depends": ["base","report_webkit","board"],
    "author": "SABRI Mouhcine",
    "category": "APOGEE",
    "description": """
        Apogee module for managing Report:
            - Effectif des Inscrits Global
            - Effectif des Nouveaux Inscrits
            - Effectif des Inscrits Par Diplôme - Filiére - Pays ... 
    """,
    "sequence": "1",
    "init_xml": [],
    'update_xml': ['new_view.xml', 'global_view.xml'],
    'data':['security/inscrits.newdipfiliere.csv',
            'security/inscrits.globaldipfiliere.csv',
            'security/inscrits.globalprov.csv',
            'security/inscrits.newprov.csv'],
    'installable': True,
    'active': False,
}
