{
        "name" : "GRH faculty",
        "version" : "1.0",
        "author" : "SALHI Abderrahim",
		"sequence" : 1,
        "website" : "http://www.fstbm.ac.ma",
        "category" : "RH",
        "description": """ Ce module permet gerer les ressources humaines """,
        "depends" : ['base'],
        "init_xml" : [ ],
        "demo_xml" : [ ],
        "update_xml" : ['grh_professor_view.xml',
						'grh_administrator_view.xml',
						'grh_temporary_view.xml',
						'grh_department_view.xml',
						'grh_job_view.xml',
						'grh_study_view.xml',
						'grh_reports.xml',
						'grh_reports.xml',
						'wizards/reports_view.xml',
							],
		"css": ['static/css/grh.css'],
        "installable": True
}