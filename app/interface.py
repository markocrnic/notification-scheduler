import schedule
import time
import threading
from flask import Flask
from flask_cors import CORS
import implementation as implementation

app = Flask(__name__)
CORS(app)


@app.route('/')
def test_thread():
    return implementation.getUsersWithFlowers()


def job():
    with app.app_context():
        implementation.getUsersWithFlowers()


sched = schedule
# sched.every(10).seconds.do(job)
# On docker container time is 2 hours late.
sched.every().day.at("09:30").do(job)


def schedule(sched):
    while 1:
        sched.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    thread = threading.Thread(target=schedule, args=(sched,))
    thread.start()
    app.run(debug=False, port=5000, host='0.0.0.0')
