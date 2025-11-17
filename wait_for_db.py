import time
import socket
import os


def wait_for_db():
    host = os.getenv('DB_HOST', 'db')
    port = int(os.getenv('DB_PORT', 5432))

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((host, port))
                print(f"Database {host}:{port} is ready!")
                return
        except socket.error:
            print(f"Waiting for database {host}:{port}...")
            time.sleep(5)


if __name__ == "__main__":
    wait_for_db()
