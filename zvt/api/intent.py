# -*- coding: utf-8 -*-
from typing import List

import pandas as pd

from zvt.api import get_kdata_schema
from zvt.contract.api import decode_entity_id
from zvt.contract.drawer import Drawer
from zvt.domain import Index1dKdata


def compare(entity_ids, props=None):
    entity_type_map_ids = _group_entity_ids(entity_ids=entity_ids)
    # compare kdata
    if props is None:
        dfs = []
        for entity_type in entity_type_map_ids:
            schema = get_kdata_schema(entity_type=entity_type)
            df = schema.query_data(entity_ids=entity_type_map_ids.get(entity_type))
            dfs.append(df)
        all_df = pd.concat(dfs)
        drawer = Drawer(main_df=all_df, sub_df_list=[all_df[['entity_id', 'timestamp', 'turnover']].copy()])
        drawer.draw_kline(show=True)


def _group_entity_ids(entity_ids):
    entity_type_map_ids = {}
    for entity_id in entity_ids:
        entity_type, _, _ = decode_entity_id(entity_id)
        ids: List = entity_type_map_ids.setdefault(entity_type, [])
        ids.append(entity_id)
    return entity_type_map_ids


if __name__ == '__main__':
    #                  id        entity_id  timestamp entity_type exchange    code  name  list_date end_date publisher category  base_point
    # 16  index_sz_399370  index_sz_399370 2002-12-31       index       sz  399370  国证成长 2010-01-04     None   cnindex    style      1000.0
    # 17  index_sz_399371  index_sz_399371 2002-12-31       index       sz  399371  国证价值 2010-01-04     None   cnindex    style      1000.0
    # 18  index_sz_399372  index_sz_399372 2002-12-31       index       sz  399372  大盘成长 2010-01-04     None   cnindex    style      1000.0
    # 19  index_sz_399373  index_sz_399373 2002-12-31       index       sz  399373  大盘价值 2010-01-04     None   cnindex    style      1000.0
    # 20  index_sz_399374  index_sz_399374 2002-12-31       index       sz  399374  中盘成长 2010-01-04     None   cnindex    style      1000.0
    # 21  index_sz_399375  index_sz_399375 2002-12-31       index       sz  399375  中盘价值 2010-01-04     None   cnindex    style      1000.0
    # 22  index_sz_399376  index_sz_399376 2002-12-31       index       sz  399376  小盘成长 2010-01-04     None   cnindex    style      1000.0
    # 23  index_sz_399377  index_sz_399377 2002-12-31       index       sz  399377  小盘价值 2010-01-04     None   cnindex    style      1000.0

    # 成长 大 中 小
    # entity_ids = ['index_sz_399372', 'index_sz_399374', 'index_sz_399376']

    # 价值 大 中 小
    entity_ids = ['index_sz_399373', 'index_sz_399375', 'index_sz_399377']

    Index1dKdata.record_data(entity_ids=entity_ids)
    compare(entity_ids=entity_ids)
