from server.core.database_connection import get_db_connection

class ArticleRepository:
    def fetch_headlines_by_day(self, category):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        if category:
            cursor.execute("""SELECT * FROM articles WHERE DATE(published_at) = CURDATE() AND category = %s""", (category,))
        else:
            cursor.execute("SELECT * FROM articles WHERE DATE(published_at) = CURDATE()")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def fetch_headlines_in_range(self, start, end, category):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        if category:
            cursor.execute("""SELECT * FROM articles WHERE published_at BETWEEN %s AND %s AND category = %s""", (start, end, category))
        else:
            cursor.execute("SELECT * FROM articles WHERE published_at BETWEEN %s AND %s", (start, end))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def fetch_saved_articles(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""SELECT na.* FROM saved_article sa JOIN articles na ON sa.article_id = na.article_id WHERE sa.user_id = %s""", (user_id,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def insert_saved_article(self, user_id, article_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO saved_article (user_id, article_id) VALUES (%s, %s)", (user_id, article_id))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Article saved."}

    def remove_saved_article(self, user_id, article_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM saved_article WHERE user_id = %s AND article_id = %s", (user_id, article_id))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Article deleted."}

    def search_articles(self, query, start, end, sort_by):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """SELECT * FROM articles WHERE (title LIKE %s OR description LIKE %s)"""
        params = [f"%{query}%", f"%{query}%"]
        if start and end:
            sql += " AND published_at BETWEEN %s AND %s"
            params += [start, end]
        if sort_by in ["likes", "dislikes"]:
            sql += f" ORDER BY {sort_by} DESC"
        cursor.execute(sql, tuple(params))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


