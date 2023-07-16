from redis import Redis

redis_client = Redis(host='localhost', port=6379, db=0)

# set a key-value pair in Redis
redis_client.set('test_key', 'test_value')

# retrieve the value of the key from Redis
value = redis_client.get('test_key')

# print the value
print(value)