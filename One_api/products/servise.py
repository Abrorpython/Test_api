from contextlib import closing
from django.db import connection
import json
from django.utils import timezone


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_all_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM product_category")
        categories = dictfetchall(cursor)
    return categories


def get_category_by_id(category_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM product_category WHERE id = %s", [category_id])
        category = dictfetchone(cursor)
    return category