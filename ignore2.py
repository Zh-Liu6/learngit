import configparser

# 创建 ConfigParser 对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('config.ini')

# 获取配置信息
db_host = config['Database']['host']
db_port = config['Database']['port']
db_username = config['Database']['username']
db_password = config['Database']['password']


print(db_host)
print(db_port)
print(db_password)
print(db_username)

