import os
import redis
from flask import Flask

from dotenv import dotenv_values

config = {
    **dotenv_values(".env.shared"),  # load shared development variables
    **dotenv_values(".env.secret"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

print(config['url_redis'])
print(config['url_host'])

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
    return f'{user} is not exists'

if __name__ == '__main__':
    app.run(config['url_host'], config['port'], config['debug'])
