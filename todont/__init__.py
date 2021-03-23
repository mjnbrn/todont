from sqlalchemy import MetaData, Table, Column, Integer, String


# Eventually we will have a fancy way to get our lists and notes and things
# For now, you bet I'm just hard coding it


def create_todonts():
    eng = create_engine('sqlite:///todont2.db3', echo=True)

    meta = MetaData()

    users = Table(
        'users', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String)
    )

    todonts = Table(
        'todonts', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('uid', Integer),
        Column('shortdesc', String),
        Column('longdesc', String),
        Column('created', Integer),
        Column('due', Integer),
        Column('complete', Integer),
    )

    meta.create_all(eng)


if __name__ == '__main__':
    create_todonts()