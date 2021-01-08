import pymysql


# 连接数据库
def conn_db():
    """
    连接备忘录的数据库
    :return: db 数据库连接
    """
    db = pymysql.connect('127.0.0.1', 'root', '123456', 'nba')
    return db


def get_team_ability():
    db = conn_db()
    cursor = db.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM team_ab_record ORDER BY id DESC LIMIT 1"

    cursor.execute(sql)
    result = cursor.fetchone()

    cursor.close()
    db.close()
    return result

def delecte_all():
    db = conn_db()
    cursor = db.cursor()

    sql = "DELETE FROM team_ab_record"

    cursor.execute(sql)

    cursor.close()
    db.close()


if __name__ == '__main__':
    print(get_team_ability())