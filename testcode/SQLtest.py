import pymysql
from pymysql import cursors
from maincode.config import core

try:
    connection = pymysql.connect(
        host = core.get("Host"),
        port = core.get("Port"),
        user = core.get("User"),
        password = core.get("password"),
        database = core.get("database"),
        cursorclass = pymysql.cursors.DictCursor
    )
    print("Всё сработало")
    try:
        with connection.cursor() as cursors:
            insert_query = "INSERT INTO new_table (ThreatName,Threat,LevelThreat) VALUES ('Вирус','Незнайка','1');"
            cursors.execute(insert_query)
            connection.commit()
    finally:
        connection.close()


except Exception as ex:
    print("Всё хуёво")
    print(ex)
