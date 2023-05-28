from sqlalchemy import create_engine, select
from sqlalchemy.engine.row import Row as SQLAlchemyRow
from sqlalchemy.orm import Session

from db_tables import s_main, performance, display, camera, energy, physical_parameters

engine = create_engine('postgresql+psycopg2://postgres:534534@localhost:5432/phones')


def month_conv(m: str) -> str:
    month = {
        '01': 'Январь',
        '02': 'Февраль',
        '03': 'Март',
        '04': 'Апрель',
        '05': 'Май',
        '06': 'Июнь',
        '07': 'Июль',
        '08': 'Август',
        '09': 'Сентябрь',
        '10': 'Октябрь',
        '11': 'Ноябрь',
        '12': 'Декабрь'
    }
    return f"{month.get(m.split('-')[1])} {m.split('-')[0]}"


def resolution_conv(r: str) -> str:
    return f"{r.split(' x ')[1]}x{r.split(' x ')[0]}"


def short_desc(model: str) -> dict:
    sample = select(
        s_main.c.title,
        s_main.c.release_date,
        s_main.c.category,
        display.c.d_size,
        display.c.display_type,
        display.c.refresh_rate,
        display.c.resolution,
        energy.c.capacity,
        energy.c.max_charge_power,
        energy.c.fast_charging,
        camera.c.lenses,
        camera.c.megapixels_front,
        performance.c.storage_size,
        performance.c.ram_size,
        performance.c.chipset,
        performance.c.total_score,
        s_main.c.advantage,
        s_main.c.disadvantage
    ).where(
        (s_main.c.title == model) &
        (s_main.c.title == display.c.title) &
        (s_main.c.title == energy.c.title) &
        (s_main.c.title == camera.c.title) &
        (s_main.c.title == performance.c.title)
    )
    res = conn.execute(sample)
    conn.close()
    desc = res.first()
    features = dict()
    features.update(
        {
            'Модель': str(desc[0]),
            'Дата выхода': month_conv(desc[1]),
            'Класс': str(desc[2]),
            'Дисплей': f"{desc[3]}' {desc[4]} {resolution_conv(desc[6])} {desc[5]} Hz",
            'АКБ': f"{desc[7]}, мощность заряда {int(desc[8])} W",
            'Быстрая зарядка': desc[9],
            'Основные камеры': desc[10],
            'Фронтальная камера': f"{int(desc[11])} Мп",
            'Процессор': desc[14],
            'Оценка производительности': desc[15],
            'Преимущества': desc[16],
            'Недостатки': desc[17]
        }
    )
    return features


conn = engine.connect()
response = short_desc('Realme Narzo 50i Prime')
for key, value in response.items():
    print(key, ':', value)

# def get_all_items_list() -> list:
#     l = list()
#     sample = select(s_main.c.title).order_by(s_main.c.title)
#     res = conn.execute(sample)
#     conn.close()
#     for line in res.all():
#         l.append(str(line[0]))
#     return l
#
#
#
# spisok = get_all_items_list()
# for line in spisok:
#     print(line)
