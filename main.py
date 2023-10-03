import redis
from flask import Flask

from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
print(config['url_redis'])
print(config['url_host'])

# redis_cache = redis.Redis(host='localhost', port=6379, db=0)
redis_cache = redis.from_url(str(config['url_redis']))

app = Flask(__name__)

@app.route('/visit/<string:user>')
def visit(user):
    value = redis_cache.incr(user)
    return 'OK'

@app.route('/show/<string:user>')
def show(user):
    if redis_cache.exists(user):
        return redis_cache.get(user)
    else:
        return f'{user} is not exists'

if __name__ == '__main__':
    # app.run('127.0.0.1', port='9111', debug=True)
    app.run(config['url_host'], config['port'], config['debug'])