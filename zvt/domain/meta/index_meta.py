# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Float
from sqlalchemy.orm import declarative_base

from zvt.contract import Portfolio, PortfolioStockHistory
from zvt.contract.register import register_schema, register_entity

'''
declarative_base()是sqlalchemy内部封装的一个方法，通过其构造一个基类
，这个基类和它的子类，可以将Python类和数据库表关联映射起来。
'''
IndexMetaBase = declarative_base()


@register_entity(entity_type='index')
class Index(IndexMetaBase, Portfolio):
    """
    指数，在exchange_index_meta.db中。
    """
    __tablename__ = 'index'

    # 发布商
    publisher = Column(String(length=64))
    # 类别
    # see IndexCategory
    category = Column(String(length=64))
    # 基准点数
    base_point = Column(Float)


class IndexStock(IndexMetaBase, PortfolioStockHistory):
    """
    指数成分股，在exchange_index_meta.db、sina_stock_meta.db以及eastmoney_stock_meta.db中。
    """
    __tablename__ = 'index_stock'


register_schema(providers=['exchange'], db_name='index_meta', schema_base=IndexMetaBase)
# the __all__ is generated
__all__ = ['Index', 'IndexStock']