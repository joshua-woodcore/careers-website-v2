import pymysql
from dotenv import load_dotenv
import os

load_dotenv()



timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db=os.getenv("DB_NAME"),
    host=os.getenv("DB_HOST"),
    password=os.getenv("DB_PASSWORD"),
    read_timeout=timeout,
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    write_timeout=timeout,
)




def fetch_all_jobs():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM jobs"
        cursor.execute(sql)
        result = cursor.fetchall()
    return result

def fetch_jobs(job_id=None):
    with connection.cursor() as cursor:
        if job_id is not None:
            if isinstance(job_id, (list, tuple)):
                # Multiple IDs
                format_strings = ','.join(['%s'] * len(job_id))
                sql = f"SELECT * FROM jobs WHERE id IN ({format_strings})"
                cursor.execute(sql, tuple(job_id))
                result = cursor.fetchall()
            else:
                # Single ID
                sql = "SELECT * FROM jobs WHERE id = %s"
                cursor.execute(sql, (job_id,))
                result = cursor.fetchone()
        else:
            sql = "SELECT * FROM jobs"
            cursor.execute(sql)
            result = cursor.fetchall()
    return result

def insert_application(job_id, application):
    with connection.cursor() as cursor:
        sql = "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (job_id,
                             application['full_name'],
                             application['email'],
                             application['linkedin_url'],
                             application['education'],
                             application['experience'],
                             application['resume_url']))
        # Commit the transaction
        connection.commit()
        return cursor.lastrowid