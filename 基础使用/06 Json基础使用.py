'''
@create_time: 2026/3/10 下午10:09
@Author: GeChao
@File: 06 Json基础使用.py
'''
import json
d = {
    "name": "周杰伦",
    "age": 30,
    "gender": "男"
}
print(d)

s= json.dumps(d, ensure_ascii= False)
print(f"转为json字符串后", s)


json_str = '{"name": "周杰伦", "age": 30,"gender": "男"}'
# 转成字典
res_dict = json.loads(json_str)
print(res_dict, type(res_dict))

