import redis
from flask import Flask

redis_cache = redis.Redis(host='localhost', port=6379, db=0, password='redis_password')

app = Flask(__name__)

@app.route('/visit/<string:user>')
def visit(user):
    if redis_cache.exists(user):
        value = redis_cache.get(user)
        pass
    else:
        # value = redis_cache.set(user)
        value = redis_cache.hincrby(user)
    return 'OK'

@app.route('/show/<string:user>')
def show(user):
    if redis_cache.exists(user):
        return redis_cache.get(user)
    else:
        return f'{user} is not exists'

app.run('127.0.0.1', port='9111', debug=True)