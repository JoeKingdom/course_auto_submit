from urllib.parse import urlencode
import requests
import datetime
now_time = datetime.datetime.now()
true_time = time1_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
print("当前时间" + true_time + "请注意报名时间！")
print("------------人文分报名器启动中。。。。------------")
print("------------       启动成功       ------------")
acid = int(input('请输入本次活动的acid：'))
opid = input('请输入您的opid：')
cookies = input("请输入您的cookie：")
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; 16s Pro Build/PKQ1.190616.001; wv) AppleWebKit/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,en-US;q=0.9',
    'Cookie': cookies,
    'Accept': 'application/json, text/javascript, */*',
    'X-Requested-With': 'com.tencent.mm'
}
# dict1 = {'acid': 535, 'opid': 'oJgDww7EjJyNTQ_NVCDdnhviKad0'}
dict1 = {'acid': acid, 'opid': opid}
url = 'http://wlwl.fashion2025.com/activity_mybmajax.htm'
data = urlencode(dict1)
print("------------     开始自动报名       ------------")
#r = requests.post(url, data=data, headers=header)
while 1:
    r = requests.post(url, data=data, headers=header)
    if r.text == "1":
        print("报名成功！")
        break
    else:
        print("报名未成功，正在重试！")
        continue

print("____________by 阿飞")



