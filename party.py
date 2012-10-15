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
    tradename = fields.Char('Trade Name')

    @classmethod
    def search_rec_name(cls, name, clause):
        ids = cls.search([('vat_number',) + clause[1:]], order=[])
        if not ids:
            Mechanism = Pool().get('party.contact_mechanism')
            mechanism_ids = Mechanism.search([
                    ('type','in',('email','phone','mobile')),
                    (('value',) + clause[1:]),
            ])
            ids = [mechanism.party.id for mechanism in \
                   Mechanism.browse(mechanism_ids)]
        if not ids:
            Address = Pool().get('party.address')
            address_ids = Address.search([
                    'OR', 'OR',
                    (('email',) + clause[1:]),
                    (('phone',) + clause[1:]),
                    (('mobile',) + clause[1:]),
            ])
            ids = [address.party.id for address in \
                   Address.browse(address_ids)]
        if not ids:
            ids = cls.search([(('tradename',) + clause[1:])])
        if ids:
            ids += cls.search([('name',) + clause[1:]], order=[])
            return [('id', 'in', ids)]
        return super(Party, cls).search_rec_name(name, clause)

