from server.core.database_connection import get_db_connection

class ArticleRepository:
    def get_top_headlines(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM articles ORDER BY published_at DESC LIMIT 10")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def search_by_keyword(self, keyword: str):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM articles WHERE title LIKE %s OR description LIKE %s"
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
