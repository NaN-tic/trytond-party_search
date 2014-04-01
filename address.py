#This file is part party_search module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta


__all__ = ['Address']
__metaclass__ = PoolMeta


class Address:
    __name__ = 'party.address'

    @classmethod
    def search_rec_name(cls, name, clause):
        Mechanism = Pool().get('party.contact_mechanism')

        domain = super(Address, cls).search_rec_name(name, clause)
        mechanisms = Mechanism.search([
                ('type', 'in', ('email', 'phone', 'mobile')),
                (('value',) + tuple(clause[1:])),
                ('address', '!=', None),
        ])
        if mechanisms:
            domain = [('id', 'in',
                [mechanism.address.id for mechanism in mechanisms])]

        return domain
