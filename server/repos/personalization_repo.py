from server.core.database_connection import get_db_connection

class PersonalizationRepo:

    def get_articles_by_preference(self, user_id, preference):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT article_id FROM article_preferences WHERE user_id = %s AND preference = %s",
            (user_id, preference)
        )
        articles = [row["article_id"] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return articles

    def get_saved_articles(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT article_id FROM saved_articles WHERE user_id = %s", (user_id,))
        saved = [row["article_id"] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return saved

    def get_read_history(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT article_id FROM read_history WHERE user_id = %s", (user_id,))
        read = [row["article_id"] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return read

    def get_notification_preferences(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notification_preferences WHERE user_id = %s", (user_id,))
        prefs = cursor.fetchone()
        cursor.close()
        conn.close()
        return prefs or {}