#This file is part party_search module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
{
    'name': 'Party Search',
    'name_ca_ES': 'Cerca de tercers',
    'name_es_ES': 'Búsqueda de terceros',
    'version': '2.4.1',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''Party Search:
  * Adds "Trade Name" field at party.
  * Search partner by VAT, email, telephone, trade_name fields.
''',
    'description_ca_ES': '''Cerca de tercers:
  * Afegeix el camp "Nom comercial"" al tercer.
  * Cerca de tercers pels camps CIF, email, telèfon i nom comercial.
''',
    'description_es_ES': '''Búsqueda de terceros:
  * Añade el campo "Nombre comercial" al tercero.
  * Búsqueda de terceros por los campos CIF, email, teléfono y nombre comercial.
''',
    'depends': [
        'ir',
        'res',
        'party_communication',
    ],
    'xml': [
        'party.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ]
}
