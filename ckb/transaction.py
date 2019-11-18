from .types import Transaction, TransactionTemplate, CellbaseTemplate


def from_cellbase_template(template: CellbaseTemplate) -> Transaction:
    return template['data']


def from_template(template: TransactionTemplate) -> Transaction:
    return template['data']
