CREATE_BUYS = """
CREATE TABLE IF NOT EXISTS buys(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    buy TEXT NOT NULL ,
    completed_buy INTEGER DEFAULT 0
    )
"""

SELECT_BUY = "SELECT id , buy , completed_buy FROM buys  "

SELECT_BUY_COMPLETE = "SELECT id, buy, completed_buy FROM buys WHERE completed_buy = 1 "

SELECT_BUY_UNCOMPLETE = " SELECT id, buy, completed_buy FROM buys WHERE completed_buy = 0"

UPDATE_BUY = "UPDATE buys SET buy = ? WHERE id = ? "

DELETE_BUY = "DELETE FROM buys WHERE id = ? "

INSERT_BUY = "INSERT INTO BUYS (buy) VALUES (?) "

UPDATE_BUY_COMPLETED = ("UPDATE buys SET completed_buy = ? WHERE id = ?")