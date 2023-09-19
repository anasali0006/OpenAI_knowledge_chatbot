import redis

redis_client = redis.Redis(host='localhost', port = 6379, decode_responses=True)

if not redis_client.ping():
    raise Exception("Redis Client could not connect to redis stack")