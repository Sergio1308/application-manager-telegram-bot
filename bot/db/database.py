from contextlib import contextmanager
from .connection import get_connection
from .models.application import Application

# region ---------------DATABASE QUERIES------------------
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

INSERT_QUERY = """INSERT INTO application (section, section_name, phone_number, location) 
                        VALUES (%s, %s, %s, POINT(%s));"""

SELECT_QUERY = """SELECT id, section, section_name, phone_number FROM application;"""

DELETE_QUERY = """DELETE FROM application WHERE id=%s;"""
# endregion


def create_table():
    with get_connection() as connection:
        with get_cursor(connection) as cursor:
            cursor.execute(CREATE_TABLE)


def add_new_column(applicationModel: Application):
    with get_connection() as connection:
        with get_cursor(connection) as cursor:
            cursor.execute(INSERT_QUERY, (applicationModel.getSection(),
                                          applicationModel.getSectionName(),
                                          applicationModel.getPhoneNumber(),
                                          f'{applicationModel.getLocation().latitude},'
                                          f'{applicationModel.getLocation().longitude}'))


def get_all_columns():
    with get_connection() as connection:
        with get_cursor(connection) as cursor:
            cursor.execute(SELECT_QUERY)
            return cursor.fetchall()


def delete_column(id: int):
    with get_connection() as connection:
        with get_cursor(connection) as cursor:
            cursor.execute(DELETE_QUERY, (id,))


@contextmanager
def get_cursor(connection):
    with connection:
        with connection.cursor() as cursor:
            yield cursor
