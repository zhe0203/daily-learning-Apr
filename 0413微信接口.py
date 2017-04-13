# -*- coding: utf-8 -*-
import itchat,time
from itchat.content import *
import requests
import json

# # 普通登陆
# itchat.auto_login(hotReload=True)
# 运行并保持在线状态
# itchat.run()
# # itchat也提供段时间内断线重连功能，只需要添加hotReload=True参数，
# # 其原理是在登陆之后在PC端保存的登陆信息，下次登陆时会直接读取存储的信息
# # itchat.auto_login(hotReload = True)
#
# # 发送消息 可以发送文本、图片、视频、附件等内容
# # 发送一段文字给文件助手
# # 这里的toUserName的值为微信号
# itchat.send('hello,helper',toUserName='filehelper')
# # 同样也可以使用 发送文本函数
# itchat.send_msg('hello,helper',toUserName='filehelper')
#
# # 如果想要恢复发给自己的文本消息，只需要这样
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg['Text']
# itchat.auto_login(hotReload=True)
# itchat.run()

# # 回复发给自己的文本
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg['Text']
# itchat.auto_login(hotReload=True)
# itchat.run()

# 简单的微信机器人

# @itchat.msg_register(TEXT)
# def reply_text(msg):
#     from_text = msg['Text']
#     # 消息带有 ‘#’ 前缀为翻译
#     if from_text[0] == '#':
#         to_text = baidu_trans(from_text[1:])
#         itchat.send(to_text, msg['FromUserName'])
#     else:
#         to_text   = tuling(from_text)
#         itchat.send(to_text,msg['FromUserName'])
#
# def tuling(info):
#     appkey   = "e5ccc9c7c8834ec3b08940e290ff1559"
#     url      = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
#     req      = requests.get(url)
#     content  = req.text
#     data     = json.loads(content)
#     answer   = data['text']
#     return answer
#
# def baidu_trans(info):
#     url = 'http://fanyi.baidu.com/v2transapi'
#     keywords = {
#         'from': 'zh',
#         'to': 'en',
#         'query': info,
#     }
#     req = requests.post(url, keywords)
#     data = req.json()
#     try:
#         result = data['dict_result']['simple_means']['word_means']
#         return ';'.join(result)
#     except:
#         return data['trans_result']['data'][0]['dst']
#
# def main():
#     itchat.auto_login(hotReload=True)
#     itchat.run()
#
# if __name__ == '__main__':
#     main()

# 好友 search_friends
# 获取自己的用户信息，返回自己的属性字典
# print(itchat.search_friends(name='聂伟'))
# 获取特定UserName的用户信息
# itchat.search_friends(userName='@abcdefg1234567')
# 获取任何一项等于name键值的用户
# itchat.search_friends(name='littlecodersh')
# 获取分别对饮相应兼职的用户
# itchat.search_friends(wechatAccount='littlecodersh')

# 公众号  get_mps将返回完整的公众号列表
# print(itchat.get_mps())
# 获取特定UserName的公众号，返回值为一个字典
# print(itchat.search_mps(UserName=''))
# 获取名字中含有特定字符的公众号，返回值为一个字典的列表
# itchat.search_mps(name='LittleCoder')
# 以下方法相当于仅特定了UserName
# itchat.search_mps(userName='@abcdefg1234567', name='LittleCoder')


# 消息的接收
# 注册文本消息，绑定到text_reply处理函数
@itchat.msg_register(TEXT)
def reply_text(msg):
    from_text = msg['Text']
    to_text = tuling(from_text)

def tuling(info):
    appkey   = "e5ccc9c7c8834ec3b08940e290ff1559"
    url      = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    req      = requests.get(url)
    content  = req.text
    data     = json.loads(content)
    answer   = data['text']
    return answer

@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
    itchat.send('%s' % tuling(msg['Text']),msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
#     itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#     if msg['isAt']:
#         itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
itchat.auto_login(hotReload=True)
itchat.run()
