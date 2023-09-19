from flask import Flask
from flask_redis import Redis

app = Flask(__name__)
redis = Redis(app)

# redis = Redis()

# app = create_app('config.cfg')
# redis.init_app(app)

@app.route('/user/<username>', methods=['GET'])
def show_user_profile(username):
    # показать профиль данного пользователя
    return 'User %s' % username

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1111)