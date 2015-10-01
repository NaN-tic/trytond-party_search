#This file is part party_search module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta


__all__ = ['Party']
__metaclass__ = PoolMeta


class Party:
    __name__ = 'party.party'

    @classmethod
    def search_rec_name(cls, name, clause):
        Mechanism = Pool().get('party.contact_mechanism')

        domain = super(Party, cls).search_rec_name(name, clause)
        parties = cls.search(domain)
        if not parties:
            mechanisms = Mechanism.search([
                    ('type', 'in', ('email', 'phone', 'mobile')),
                    (('value',) + tuple(clause[1:])),
            ])
            domain = [('id', 'in',
                [mechanism.party.id for mechanism in mechanisms])]

        return domain
