"""
这个模块用于存放我们编写的命令
"""

import random

import requests

from command import on_command


@on_command('echo')
def echo(bot, ctx, arg):
    return {'reply': arg}


@on_command('喵一个')
def miao(bot, ctx, arg):
    return {'reply': '喵～'}


@on_command('掷骰子')
def _(bot, ctx, arg):
    return {'reply': str(random.randint(1, 6))}


@on_command('计算')
def _(bot, ctx, arg):
    expression = arg.strip()
    print(expression)
    return {'reply': str(eval(expression))}


@on_command('今儿吃啥')
def _(bot, ctx, arg):
    return {'reply': random.choice(['日夜食堂走起', '别想了穷逼，吃早点', '大佬，该点外卖了', '砂锅吃不', '清真食堂来一波'])}


@on_command('我是谁')
def _(bot, ctx, arg):
    return {'reply': str(ctx['sender']['nickname'])}


# @on_command('签到')
# def _(bot, ctx, arg):
#     wh = str(ctx['sender']['nickname'])
#     da +=1
#     return{'reply': '@%s\n🙂签到成功🙂\n你已累计签到%d次' % (wh, da)}


# @on_command('签到')
# def _(bot, ctx, arg):
#     da = '0'
#     red ={}
#     rpl = ['🙂签到成功🙂', '\n', '你已累计签到', '次']
#     wh = ctx['user_id']
#     red[wh] = da
#     print(red)
#     rpl.insert(3, da)
#     return {'reply': str(rpl[0] + rpl[1] + rpl[2] + rpl[3] + rpl[4])}
#     # print(wh)

@on_command('知乎日报')
def _(bot, ctx, arg):
    STORY_URL_FORMAT = 'http://daily.zhihu.com/story/{}'

    resp = requests.get('https://news-at.zhihu.com/api/4/news/latest', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'})

    data = resp.json()
    stories = data.get('stories')

    if not stories:
        bot.send(ctx, '诶呀，找不到了呢')
        return

    reply = ''
    for story in stories:
        url = STORY_URL_FORMAT.format(story['id'])
        title = story.get('title', '未知内容')
        reply += f'\n{title}\n{url}\n'

    bot.send(ctx, reply)
