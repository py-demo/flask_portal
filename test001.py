import json

msg = dict()
msg["accesstoken"] = "691e922620860107b3cd4e0f200a630b"

msgstr = json.dumps(msg)


print(msgstr)


message = dict()
message['state'] = 1
message["msg"] = msg

str1 = json.dumps(message)

print(str1)

message["msg"] = msgstr

str2 = json.dumps(message)

print(str2)

import uuid
ustr = str(uuid.uuid1())

sra = ''
sra = ustr.replace("-", "")

print(sra)