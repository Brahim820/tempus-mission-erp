
{
    'name' : 'Patrimoin',
    'version' : '1.1',
    'author' : 'I.BADI',
    'category' : 'Patrimoin',
	'sequence' :1,
    'description' : """
	
Module de gestion du patrimoin de l'USMS.
======================================================

Ce module couvre les éléments suivants:
------------------------------------------------------
    * Gestion des locaux
    * Gestion des équipements
   """,
    'website': 'http://www.usms.ma',
    'images' : ['static/images/fst_logo.png'],
    'depends' : ['base'],
    'data': [],
    'update_xml': ['ptr_etablissement_view.xml',
	               'ptr_local_view.xml',
				   'ptr_equipement_view.xml',
				   'ptr_departement_view.xml',
						],
    'js': [],
    'qweb' : [],
    'css':['static/css/ptr_establissement.css'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
