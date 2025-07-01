from server.core.database_connection import get_db_connection
from server.repos.category_repo import CategoryRepo

category_repo = CategoryRepo()
class NotificationRepo:

    def insert_preference(self, user_id, preference_data):
        category_id = category_repo.get_category_by_name(preference_data.category)["category_id"]
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            INSERT INTO notification_preferences (user_id, category_id, keyword)
            VALUES (%s, %s, %s)
        """, (user_id, category_id, preference_data.keyword))
        conn.commit()
        preference_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {
            "Notification added successfully"
        }

    def get_preferences_by_user(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
                SELECT 
                    np.id, 
                    np.user_id, 
                    c.category_name AS category, 
                    np.is_enabled, 
                    np.keyword
                FROM notification_preferences np
                JOIN category c ON np.category_id = c.category_id
                WHERE np.user_id = %s
            """, (user_id,))
        preferences = cursor.fetchall()
        cursor.close()
        conn.close()
        return preferences

    def update_preference(self, user_id, pref_id, data):
        category_id = category_repo.get_category_by_name(data.category)["category_id"]
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            UPDATE notification_preferences 
            SET category_id = %s, is_enabled = %s, keyword = %s
            WHERE id = %s AND user_id = %s
        """, (category_id, data.is_enabled, data.keyword, pref_id, user_id))
        conn.commit()
        cursor.close()
        conn.close()
        return {
           "Prefrence updated successfully"
        }

    def delete_preference(self, user_id, pref_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notification_preferences WHERE id = %s AND user_id = %s", (pref_id, user_id))
        conn.commit()
        cursor.close()
        conn.close()
        return {"detail": "Preference deleted"}

    def insert_notifications_for_new_articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT IGNORE INTO notifications (user_id, article_id, message)
            SELECT t1.user_id, t3.article_id, t3.title
            FROM notification_preferences t1
            JOIN article_category_mapping t2 ON t1.category_id = t2.category_id
            JOIN articles t3 ON t3.article_id = t2.article_id
            WHERE 
                (t1.keyword IS NULL OR 
                CONCAT_WS(' ', t3.title, t3.description, t3.content) LIKE CONCAT('%', t1.keyword, '%'))
                AND t3.fetched_at >= NOW() - INTERVAL 4 HOUR;
        """)
        conn.commit()
        cursor.close()
        conn.close()

    def get_unread_notifications_grouped_by_user(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT u.email, u.user_id, 
                GROUP_CONCAT(CONCAT('Title - ', n.message, '\nURL   - ', a.url, '\n') SEPARATOR '\n') AS messages
        FROM notifications n
        JOIN users u ON u.user_id = n.user_id
        JOIN articles a ON a.article_id = n.article_id
        WHERE n.is_read = 0
        GROUP BY u.user_id
        """)
        results = cursor.fetchall()

        cursor.close()
        conn.close()
        return results

    # def mark_all_notifications_as_read(self):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     cursor.execute("UPDATE notification SET is_read = 1 WHERE is_read = 0")
    #     conn.commit()
    #     cursor.close()
    #     conn.close()