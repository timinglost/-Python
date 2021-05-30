import hashlib
from uuid import uuid4
salt = uuid4().hex
salt = 'my_salt'
def caching(d, address):
    a = hashlib.sha256(address.encode() + salt.encode())
    b = a.hexdigest()
    if b in d:
        return
    else:
        d[f'{b}'] = address
url_hash_table = {}
caching(url_hash_table, 'www.google.com')
caching(url_hash_table, 'www.vk.com')
caching(url_hash_table, 'www.vk.com')
caching(url_hash_table, 'www.github.com')
caching(url_hash_table, 'www.yandex.ru')
caching(url_hash_table, 'www.yandex.ru')
print(url_hash_table)
