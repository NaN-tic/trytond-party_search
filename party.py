#This file is part party_search module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    @classmethod
    def search_rec_name(cls, name, clause):
        domain = super(Party, cls).search_rec_name(name, clause)
        return domain + [
            ('contact_mechanisms.value',) + tuple(clause[1:]),
            ('addresses.building_name',) + tuple(clause[1:]),
            ('addresses.party_name',) + tuple(clause[1:]),
            ('addresses.street',) + tuple(clause[1:]),
            ('addresses.postal_code',) + tuple(clause[1:]),
            ('addresses.city',) + tuple(clause[1:]),
            ]
