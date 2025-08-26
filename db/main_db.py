import sqlite3
from db import queries 
from config import db_path

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_BUYS)
    print("База данных сохранена ")
    conn.commit()
    conn.close() 

def get_buys(filter_type="all"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if filter_type == "completed_buy":
        cursor.execute(queries.SELECT_BUY_COMPLETE)
    elif filter_type == "uncompleted_buy":
        cursor.execute(queries.SELECT_BUY_UNCOMPLETE)
    else: 
        cursor.execute(queries.SELECT_BUY)

    buys = cursor.fetchall()
    conn.close()
    return buys 

def add_buy(buy):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_BUY, (buy,))
    conn.commit()
    buy_id = cursor.lastrowid
    conn.close()
    return buy_id


def delete_buy(buy_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_BUY, (buy_id,))
    conn.commit()
    conn.close()

def update_buy(buy_id, new_buy=None, completed_buy = None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor() 

    if new_buy is not None:
        cursor.execute(queries.UPDATE_BUY, (new_buy, buy_id))

    if completed_buy is not None:
        cursor.execute(queries.UPDATE_BUY_COMPLETED, (completed_buy, buy_id))

    conn.commit()
    conn.close()



