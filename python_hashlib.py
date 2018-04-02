# MD5
import hashlib
import hmac
md5 = hashlib.md5()
md5.update(r'123456mysalt'.encode('utf-8'))
print(md5.hexdigest())

# SHA1
sha1 = hashlib.sha1()
sha1.update(r'Myfour\'s password'.encode('utf-8'))
print(sha1.hexdigest())

# 模拟登录

db = {
    'alice': '1d5cd27e237ff81c8c7601ba479c33f2',
    'tina': '878ef96e86145580c38c87f0410ad153'
}


def login(usr, pwd):
    if usr not in db.keys():
        return '无该账号'
    md5p = hashlib.md5()
    md5p.update((pwd + 'mysalt').encode('utf-8'))
    if db[usr] == md5p.hexdigest():
        return '登录成功'
    else:
        return '登录失败'


print(login('alice', '123456'))

# hmac加盐
h = hmac.new(
    'mysalt'.encode('utf-8'), '123456'.encode('utf-8'), digestmod='MD5')
print(h.hexdigest())
