"""
这个模块用于存放我们编写的命令
"""

import random


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


@on_command('签到')
def _(bot, ctx, arg):
    da = '0'
    red ={}
    rpl = ['🙂签到成功🙂', '\n', '你已累计签到', '次']
    wh = ctx['user_id']
    red[wh] = da
    print(red)
    rpl.insert(3, da)
    return {'reply': str(rpl[0] + rpl[1] + rpl[2] + rpl[3] + rpl[4])}
    # print(wh)



    # da = '3'
    # rpl = ['🙂签到成功🙂', '\n', '你已累计签到', '次']
    # rpl.insert(3, da)
    # return {'reply': str(rpl[0]+rpl[1]+rpl[2]+rpl[3]+rpl[4])}
    # # bot.send(ctx, , 'da')
