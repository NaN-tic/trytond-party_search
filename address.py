#This file is part party_search module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta


__all__ = ['Address']


class Address:
    __metaclass__ = PoolMeta
    __name__ = 'party.address'

    @classmethod
    def search_rec_name(cls, name, clause):
        domain = super(Address, cls).search_rec_name(name, clause)
        if clause[1].startswith('!') or clause[1].startswith('not '):
            bool_op = 'AND'
        else:
            bool_op = 'OR'
        return [bool_op,
            domain,
            ('contact_mechanisms.value',) + tuple(clause[1:]),
            ]
