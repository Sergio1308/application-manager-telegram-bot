from contextlib import contextmanager
from bot.db.connection import get_connection
from bot.db.models.application import Application


def create_table():
    CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS application
        (
            id SERIAL PRIMARY KEY,
            section VARCHAR(20),
            section_name TEXT,
            phone_number VARCHAR(15),
            location POINT
        );
    """
    with get_connection() as connection:
        with get_cursor(connection) as cursor:
            cursor.execute(CREATE_TABLE)


def add_new_columns(applicationModel: Application):
    """
    Add new values to tables.

    :param applicationModel:
    :return: None
    """
    INSERT_QUERY = """INSERT INTO application (section, section_name, phone_number, location) 
                        VALUES (%s, %s, %s, POINT(%s));"""
    with get_connection() as connection:
        with get_cursor(connection) as cursor:
            cursor.execute(INSERT_QUERY, (applicationModel.getSection(),
                                          applicationModel.getSectionName(),
                                          applicationModel.getPhoneNumber(),
                                          f'{applicationModel.getLocation().latitude},'
                                          f'{applicationModel.getLocation().longitude}'))


@contextmanager
def get_cursor(connection):
    with connection:
        with connection.cursor() as cursor:
            yield cursor
