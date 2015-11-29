# This file is part of the party_search module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class PartySearchTestCase(ModuleTestCase):
    'Test Party Search module'
    module = 'party_search'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartySearchTestCase))
    return suite
