import sqlite3

def label_to_query(label, type=None):
    query = 'SELECT DISTINCT * FROM videos '
    query += f'WHERE {label} > 0 '
    if not (type is None):
        query += f'AND type="{type}" '
    query += f'ORDER BY {label} DESC;'
    return query

def query_for_videos(label, type=None):
    query = label_to_query(label, type)

    con = sqlite3.connect('video.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    con.close()
    return rows
