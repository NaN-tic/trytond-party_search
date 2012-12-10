#This file is part party_search module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['Party']
__metaclass__ = PoolMeta

class Party:
    'Party'
    __name__ = 'party.party'

    @classmethod
    def search_rec_name(cls, name, clause):
        parties = cls.search([('vat_number',) + tuple(clause[1:])], order=[])
        if not parties:
            parties = cls.search([(('tradename',) + tuple(clause[1:]))])
        if not parties:
            Mechanism = Pool().get('party.contact_mechanism')
            mechanisms = Mechanism.search([
                    ('type','in',('email','phone','mobile')),
                    (('value',) + tuple(clause[1:])),
            ])
            parties = [mechanism.party for mechanism in mechanisms]
        if not parties:
            Address = Pool().get('party.address')
            addresses = Address.search([
                    (('name',) + tuple(clause[1:])),
            ])
            parties = [address.party for address in addresses]
        if parties:
            return [('id', 'in', [party.id for party in parties])]
        return super(Party, cls).search_rec_name(name, clause)
