# datetime是Python处理日期和时间的标准库。
from datetime import datetime, timedelta  # datetime是一个模块，其中也有一个datetime类
now = datetime.now()
print(now)
print(type(now))
# 指定一个日期时间
dt = datetime(1996, 3, 4, 19, 3)
print(dt)
# 在计算机中，时间实际上是用数字表示的,
# 我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），
# 当前时间就是相对于epoch time的秒数，称为timestamp。

# 把datetime转换为timestamp
# 把一个datetime类型转换为timestamp只需要简单调用datetime对象的timestamp()方法：
print(dt.timestamp())
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，
# 这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

# timestamp转datetime
# 调用datetime类的fromtimestamp方法
print(datetime.fromtimestamp(825937380.0))
# 上述转换是在timestamp和本地时间做转换;我们也可以将其转换为UTC标准时间
print(datetime.utcfromtimestamp(825937380.0))

# str转换为datetime
cday = datetime.strptime('1996-03-04 20:00:00', '%Y-%m-%d %H:%M:%S')
print(cday)
# datetime转str
print(dt.strftime('%Y-%m-%d %H:%M:%S'))

# datetime加减
# 需要引入timedelta类
print(now + timedelta(hours=10))  # 加10个小时
print(now + timedelta(days=10))
print(now - timedelta(days=10))  # 减10天
