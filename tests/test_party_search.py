#!/usr/bin/env python
#This file is part party_search module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends
from trytond.tests.test_tryton import doctest_setup, doctest_teardown


class PartySearchTestCase(unittest.TestCase):
    '''Test PartySearch module'''

    def setUp(self):
        trytond.tests.test_tryton.install_module('party_search')

    def test0006depends(self):
        '''
        Test depends'''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartySearchTestCase))
    return suite
