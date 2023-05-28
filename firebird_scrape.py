import fdb
from sqlalchemy import create_engine, insert

from db_tables import aval

fdb_connection = fdb.connect(
    dsn='C:/ClientShopDatabase/TASK2.FDB',
    user='SYSDBA',
    password='masterkey'
)


def brand_choice(s: str) -> str:
    brands = {
        'Redmi': 'Xiaomi',
        'Poco': 'Xiaomi',
    }
    response = brands.get(s)
    if response:
        return response
    else:
        return s


def goods_list(*args):
    cur = fdb_connection.cursor()
    cur.execute(
        f"SELECT SQ.CODE, SQ.NAME, Sum(QUANTITY), SQ.PRICE_ FROM ("
        f"SELECT dg.CODE, dg.NAME, dst.QUANTITY, dg.PRICE_ "
        f"FROM DIR_GOODS dg, DOC_SESSION_TABLE dst "
        f"WHERE dg.CODE = dst.GOOD AND dg.PARENT BETWEEN {args[0]} AND {args[1]} "
        f"UNION ALL "
        f"SELECT dg.CODE, dg.NAME, -dst2.QUANTITY, dg.PRICE_ "
        f"FROM DIR_GOODS dg, DOC_SALE_TABLE dst2 "
        f"WHERE dg.CODE = dst2.GOOD AND dg.PARENT BETWEEN {args[0]} AND {args[1]} "
        f"UNION ALL "
        f"SELECT dg.CODE, dg.NAME, -dbt.QUANTITY, dg.PRICE_ "
        f"FROM DIR_GOODS dg, DOC_BALANCE_TABLE dbt "
        f"WHERE dg.CODE = dbt.GOOD AND dg.PARENT BETWEEN {args[0]} AND {args[1]} "
        f"UNION ALL "
        f"SELECT dg.CODE, dg.NAME, +drt.QUANTITY, dg.PRICE_ "
        f"FROM DIR_GOODS dg, DOC_RETURN_TABLE drt "
        f"WHERE dg.CODE = drt.GOOD AND dg.PARENT BETWEEN {args[0]} AND {args[1]} "
        f"UNION ALL "
        f"SELECT dg.CODE, dg.NAME, -det.QUANTITY, dg.PRICE_ "
        f"FROM DIR_GOODS dg, DOC_EXPSESSION_TABLE det "
        f"WHERE dg.CODE = det.GOOD AND dg.PARENT BETWEEN {args[0]} AND {args[1]}) SQ "
        f"GROUP BY SQ.CODE, SQ.NAME, SQ.PRICE_ "
        f"HAVING SUM(SQ.QUANTITY) >= 1 "
        f"ORDER BY SQ.PRICE_")
    temp_list = list()
    for line in cur.fetchall():
        temp_list.append(
            [
                line[1].split(' ')[0],
                line[1].split(' ')[1],
                line[0],
                line[1].split(' ', maxsplit=1)[1],
                int(line[2]),
                int(line[3])
            ]
        )
    return temp_list


def write_to_postgres(temp_list: list) -> None:
    insert_list = list()
    for line in temp_list:
        insert_list.append(
            {
                'type_': line[0],
                'brand': brand_choice(line[1]),
                'code': int(line[2]),
                'product': line[3],
                'quantity': int(line[4]),
                'price': int(line[5])
            }
        )
    engine = create_engine('postgresql+psycopg2://postgres:534534@localhost:5432/day_interaction',
                           echo=True)
    with engine.connect() as conn:
        conn.execute(insert(aval), insert_list)
        conn.commit()


sp = goods_list(*[80, 84])
write_to_postgres(sp)
