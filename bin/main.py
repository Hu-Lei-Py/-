import redis

# 虚拟机的ip地址
ip = '121.40.207.159'
# 虚拟机的端口
port = 6379


class Redis:
    def __init__(self, ip, port):
        self.conn = redis.StrictRedis(host=ip, port=port, db=9)


red = Redis(ip, port)
name = "car_777"
# res = red.conn.hset(name,"29",2)
# print(res)

# 购物车添加
r2 = red.conn.hset("car_777", "50", "5")
r2 = red.conn.hgetall(name)
print(type(r2), r2)

r3 = red.conn.hvals("car_777")
print(r3)
# 删除
# res = red.conn.hdel("car_777",9999999)
# print(res)

# num = int(r2) + 1
# print(num)

# 更新29号商品的数量
# res = red.conn.hset(name,"29",num)
# print(res)
