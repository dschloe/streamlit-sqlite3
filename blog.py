import streamlit as st
import sqlite3

# Connect to SQLite database
def connect_db():
    return sqlite3.connect("data/blog.db")

# Add a new post
def add_post(conn):

    with st.form("my_form", clear_on_submit=True):
        title = st.text_input("Title")
        content = st.text_area("Content")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO posts (title, content) VALUES (?,?)", (title, content))
            conn.commit()
            st.success("Post::'{}' Saved".format(title))


# Edit a post
def edit_post(conn, post_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE id=?", (post_id,))
    post = cursor.fetchone()
    title = st.text_input("Title", post[1])
    content = st.text_area("Content", post[2])
    if st.button("Save"):
        cursor.execute("UPDATE posts SET title=?, content=? WHERE id=?", (title, content, post_id))
        conn.commit()

# Delete a post
def delete_post(conn, post_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM posts WHERE id=?", (post_id,))
    conn.commit()

# View all posts
def view_posts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    for i, post in enumerate(posts):
        st.write("ID: ", post[0])
        st.write("Title: ", post[1])
        st.write("Content: ", post[2])
        st.write("Actions:")
        edit_button = st.button("Edit", key=f"edit_button_{i}")
        if edit_button:
            edit_post(conn, post[0])
        delete_button = st.button("Delete", key=f"delete_button_{i}")
        if delete_button:
            delete_post(conn, post[0])

def blog_main():
    st.title("Simple Blog with Streamlit & SQLite")
    conn = connect_db()
    add_post(conn)
    st.write("")
    st.write("View all posts:")
    view_posts(conn)