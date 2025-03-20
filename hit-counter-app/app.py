import redis 
import time 
from flask import Flask


app = Flask(__name__)
cashe = redis.Redis(host = "redis", port = 6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cashe.incr('hits')
        except redis.expceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
            
            
@app.route('/')
def hello():
    count = get_hit_count()
    return f"Whats up Deep Divers!!!! You've visited me {count} times abkreeem bymsee"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) 