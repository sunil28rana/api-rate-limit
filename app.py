from functools import wraps

from flask import Flask, request
from redis import Redis

app = Flask(__name__)

r = Redis.from_url('redis://localhost:6379')


def limit_api_calls(func):
    @wraps(func)
    def wrapper_func():
        ip = request.remote_addr
        times_hit = int(r.incr(ip))
        print('{} has hit {} times'.format(ip, r.get(ip)))
        if times_hit > 5:
            return 'You\'ve exhausted your limits', 429
        r.expire(ip, 5)
        return func()
    return wrapper_func


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/post', methods=['POST'])
@limit_api_calls
def post():
    return 'This API can only be called limited number of times!', 200


if __name__ == '__main__':
    app.run()

