# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.orm import declarative_base

from zvt.contract.register import register_schema
from zvt.domain.quotes import StockKdataCommon

KdataBase = declarative_base()


class Stock1dKdata(KdataBase, StockKdataCommon):
    """
    股票日K线前复权数据。
    """
    __tablename__ = 'stock_1d_kdata'


register_schema(providers=['joinquant', 'em'], db_name='stock_1d_kdata', schema_base=KdataBase, entity_type='stock')

# the __all__ is generated
__all__ = ['Stock1dKdata']