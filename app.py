import streamlit as st
import sqlite3

st.title("📊 Demo Dashboard")

def get_connection():
    try:
        conn = sqlite3.connect('demo.db')
        return conn
    except sqlite3.Error as e:
        st.error(f"Database connection failed: {e}")
        return None

def show_user_count():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            st.success(f"✅ Total users in database: {count}")
        except sqlite3.OperationalError:
            st.warning("⚠️ 'users' table not found. Please initialize the database.")
        finally:
            conn.close()

show_user_count()

