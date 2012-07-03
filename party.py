#This file is part of Tryton.  The COPYRIGHT file at the top level
#of this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool
from trytond.pyson import Eval, PYSONEncoder, Date
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction

class Party(ModelSQL, ModelView):
    'Party'
    _name = 'party.party'
    _description = __doc__
    tradename = fields.Char('Trade Name')

    def search_rec_name(self, name, clause):
        ids = self.search([('vat_number',) + clause[1:]], order=[])
        if not ids:
            mechanism_obj = Pool().get('party.contact_mechanism')
            mechanism_ids = mechanism_obj.search([
                    ('type','in',('email','phone','mobile')),
                    (('value',) + clause[1:]),
            ])
            ids = [mechanism.party.id for mechanism in \
                   mechanism_obj.browse(mechanism_ids)]
        if not ids:
            address_obj = Pool().get('party.address')
            address_ids = address_obj.search([
                    'OR', 'OR',
                    (('email',) + clause[1:]),
                    (('phone',) + clause[1:]),
                    (('mobile',) + clause[1:]),
            ])
            ids = [address.party.id for address in \
                   address_obj.browse(address_ids)]
        if not ids:
            ids = self.search([(('tradename',) + clause[1:])])
        if ids:
            ids += self.search([('name',) + clause[1:]], order=[])
            return [('id', 'in', ids)]
        return super(Party, self).search_rec_name(name, clause)

Party()
