from api.v1.app import app
from redis import Redis

redis_client = Redis(host='localhost', port=6379, db=0)
print(redis_client.get('token'))

if __name__ == '__main__':
    app.run()