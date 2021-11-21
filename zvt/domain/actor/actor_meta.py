# -*- coding: utf-8 -*-

from sqlalchemy.orm import declarative_base

from zvt.contract.register import register_schema
from zvt.contract.schema import ActorEntity

ActorMetaBase = declarative_base()


class ActorMeta(ActorMetaBase, ActorEntity):
    """
    市场参与者，比如股票的机构投资者，股票的前十大流通股东等。
    """
    __tablename__ = 'actor_meta'


register_schema(providers=['em'], db_name='actor_meta', schema_base=ActorMetaBase)
# the __all__ is generated
__all__ = ['ActorMeta']