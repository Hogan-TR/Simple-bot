from pprint import pprint
from cqhttp import CQHttp
import random

bot = CQHttp(api_root='http://127.0.0.1:5700')


@bot.on_message('private')
def handle_msg(ctx):
    pprint(ctx)
    msg = ctx['message']
    echo_cmd = 'echo'
    fod = ['砂锅走起', '清真三楼', '日夜点菜', '穷逼，吃早点--省钱🙃', '一号食堂', '大佬,点外卖--🤑']
    if msg.startswith(echo_cmd + ' '):
        bot.send(ctx, msg[len(echo_cmd + ' '):])
    elif msg == '喵一个':
        bot.send(ctx, '喵')
    elif msg == '随机数':
        bot.send(ctx, str(random.random()))
    elif msg == '今天吃啥':
        bot.send(ctx, random.choice(fod))
    elif msg == '骰子':
        bot.send(ctx, '小主你要的')
        bot.send(ctx, str(random.randint(1, 7)))
    else:
        bot.send(ctx, random.choice(['困😴', '别烦...滚', '干嘛呀😒', '小爷我今天心情好', '不理你😑']))


bot.run('127.0.0.1', 8080)
