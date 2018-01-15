import json
import datetime

msg = dict()
msg["accesstoken"] = "691e922620860107b3cd4e0f200a630b"

msgstr = json.dumps(msg)


print('---1---')
print msgstr
print


message = dict()
message['state'] = 1
message["msg"] = msg

str1 = json.dumps(message)

print('---2---')
print str1
print

message["msg"] = msgstr

str2 = json.dumps(message)

print('---3---')
print str2
print

import uuid
ustr = str(uuid.uuid1())

sra = ustr.replace("-", "")

print('---4---')
print sra
print

dt1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

print('---5---')
print dt1
print

urid = u"70e5ea17ea4b11e7ac1234363b74db9e"

print('---6---')
print urid
print