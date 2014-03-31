#This file is part party_search module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.pool import Pool
from .party import *
from .address import *


def register():
    Pool.register(
        Party,
        Address,
        module='party_search', type_='model')
