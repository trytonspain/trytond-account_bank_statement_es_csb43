#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.pool import Pool
from . import statement


def register():
    Pool.register(
        statement.Configuration,
        statement.ConfigurationDefaultAccount,
        statement.ImportStart,
        module='account_bank_statement_es_csb43', type_='model')
    Pool.register(
        statement.Import,
        module='account_bank_statement_es_csb43', type_='wizard')
