import websocket  # pip install websocket-client
import json
import threading
import time
import datetime
import discord
from discord_webhook import DiscordWebhook, DiscordEmbed
from websocket._exceptions import WebSocketConnectionClosedException
import urllib

## webhook-url
# balko
balko_success = 'xxx'
balko_announcement = 'xxx'
balko_update = 'xxx'
# prism
prism_update = 'xxx'
prism_announcement = 'xxx'
prism_success = 'xxx'
# phantom
phantom_update = ''
phantom_announcement =''
phantom_success =''
# wrath
wrath_update = ''
wrath_announcement =''
wrath_success =''
# pd
pd_update = ''
pd_announcement =''
pd_success =''
# sole
sole_update = ''
sole_announcement =''
sole_success =''
# kodai
kodai_update = ''
kodai_announcement =''
kodai_success =''
# wrath
wrath_update = ''
wrath_announcement =''
wrath_success =''

## embed-info
embed_footer = "1024 Rental | Powered by YIM"
embed_icon = 'https://www.whop.io/assets/whop.png'
embed_color = 0x82111f

## channels
general_announcement = '805864705008599070'
other_aio_bots = '771200794615742485'
king_aio_bots = '771200643255500880' # kodai,wrath,ganesh
supreme_bots = '771200619046240256'

balko_success_channel = '771202208616284180'
prism_success_channel = '771202034086707210'
reaio_success_channel = '771202146153660418'
easycop_success_channel = '868025676106694677'  # cloud
mekaio_success_channel = '791113430076489768'
kylin_success_channel = '785656724174143508'
nsb_success_channel = '833730041568297020'    # ad

success_channels = [balko_success_channel, prism_success_channel, reaio_success_channel, easycop_success_channel,
                    mekaio_success_channel, kylin_success_channel, nsb_success_channel]




def send_json_request(ws, request):
    ws.send(json.dumps(request))


def recieve_json_response(ws):
    try:
        response = ws.recv()
    except (WebSocketConnectionClosedException, ConnectionResetError):
        print("Caught Connection Error")
        time.sleep(5)
        return 0
    else:
        if response:
            return json.loads(response)


def heartbeat(interval, ws):
    print('Heartbeat begin')
    while True:
        time.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, heartbeatJSON)
        print(str(datetime.datetime.now()) + ": " + "Heartbeat sent")


def connect():
    temp = 0
    while temp <= 5:
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
        event = recieve_json_response(ws)
        if event == 0:
            temp = temp + 1
        else:
            temp = 6
    heartbeat_interval = event['d']['heartbeat_interval'] / 1000
    threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

    token = 'xxx'
    payload = {
        'op': 2,
        "d": {
            "token": token,
            "properties": {
                "$os": "windows",
                "$browser": "chrome",
                "$device": 'pc'
            }
        }
    }
    send_json_request(ws, payload)
    return ws, event


ws, event = connect()

while True:
    event = recieve_json_response(ws)
    if event == 0:
        print("Connecting...")
        ws, event = connect()

    if event is None:
        continue
    if ('d' in event) and (event['d'] is None):
        continue
    try:
        ## bot-success
        if ('channel_id' in event['d']) and (str(event['d']['channel_id']) in success_channels):
            if ('embeds' in event['d']) and (len(event['d']['embeds']) != 0):
                embed = event['d']['embeds'][0]
                if event['d']['channel_id'] == balko_success_channel:
                    webhook_url = balko_success
                elif event['d']['channel_id'] == prism_success_channel:
                    webhook_url = prism_success
                elif event['d']['channel_id'] == nsb_success_channel:
                    webhook_url = nsb_success
                elif event['d']['channel_id'] == easycop_success_channel:
                    webhook_url = easycop_success
                elif event['d']['channel_id'] == kylin_success_channel:
                    webhook_url = kylin_success
                elif event['d']['channel_id'] == mekaio_success_channel:
                    webhook_url = mekaio_success
                elif event['d']['channel_id'] == reaio_success_channel:
                    webhook_url = reaio_success
                else:
                    webhook_url = 'https://discord.com/api/webhooks/861786508825853993/xxx'

                embed['footer']['text'] = embed_footer
                embed['footer']['icon_url'] = embed_icon
                embed['color'] = embed_color
                # embed.set_footer(text="Thanks for using HR Space", icon_url="https://www.whop.io/assets/whop.png")
                webhook = DiscordWebhook(
                    url=webhook_url)

                webhook.add_embed(embed)
                response = webhook.execute()

                print(str(datetime.datetime.now()) + ": " + "webhook sent")
            else:
                embed = event['d']['content']
                webhook_url = balko_success
                webhook = DiscordWebhook(
                    url=webhook_url, content=embed)

                response = webhook.execute()

                print(str(datetime.datetime.now()) + ": " + "webhook sent")

        ## bot-announcement
        elif ('channel_id' in event['d']) and (str(event['d']['channel_id']) == general_announcement):
            if ('embeds' in event['d']) and (len(event['d']['embeds']) != 0):
                embed = event['d']['embeds'][0]
                print(embed)
                if embed['author']['name'] == 'BALKO':
                    embed['author']['name'] = 'Balko announcement'
                    webhook_url = balko_announcement
                elif embed['author']['name'] == 'PRISM':
                    embed['author']['name'] = 'Prism announcement'
                    webhook_url = prism_announcement
                elif embed['author']['name'] == 'NSB':
                    embed['author']['name'] = 'Nsb announcement'
                    webhook_url = nsb_announcement
                elif embed['author']['name'] == 'EASYCOP':
                    embed['author']['name'] = 'Easycop announcement'
                    webhook_url = easycop_announcement
                elif embed['author']['name'] == 'KYLIN':
                    embed['author']['name'] = 'Kylin announcement'
                    webhook_url = kylin_announcement
                elif embed['author']['name'] == 'MEKAIO':
                    embed['author']['name'] = 'Mekaio announcement'
                    webhook_url = mekaio_announcement
                elif embed['author']['name'] == 'REAIO':
                    embed['author']['name'] = 'Reaio announcement'
                    webhook_url = reaio_announcement
                else:
                    webhook_url = 'https://discord.com/api/webhooks/861786508825853993/xxx'

                embed['footer']['text'] = embed_footer
                embed['footer']['icon_url'] = embed_icon
                embed['color'] = embed_color

                webhook = DiscordWebhook(
                    url=webhook_url)

                webhook.add_embed(embed)
                response = webhook.execute()

                print(str(datetime.datetime.now()) + ": " + "webhook sent")

        ## bot-update
        elif ('channel_id' in event['d']) and (str(event['d']['channel_id']) == other_aio_bots):
            # print(len(event['d']['embeds']))
            if ('embeds' in event['d']) and (len(event['d']['embeds']) != 0):
                embed = event['d']['embeds'][0]
                print(embed)
                if embed['author']['name'] == 'BALKO UPDATE':
                    embed['author']['name'] = 'Balko update'
                    webhook_url = balko_update
                elif embed['author']['name'] == 'REAIO UPDATE':
                    embed['author']['name'] = 'Reaio update'
                    webhook_url = reaio_update
                elif embed['author']['name'] == 'PRISM UPDATE':
                    embed['author']['name'] = 'Prism update'
                    webhook_url = prism_update
                elif embed['author']['name'] == 'MEKAIO UPDATE':
                    embed['author']['name'] = 'Mekaio update'
                    webhook_url = mekaio_update
                elif embed['author']['name'] == 'KYLIN UPDATE':
                    embed['author']['name'] = 'Kylin update'
                    webhook_url = kylin_update
                elif embed['author']['name'] == 'NSB UPDATE':
                    embed['author']['name'] = 'Nsb update'
                    webhook_url = nsb_update
                elif embed['author']['name'] == 'EASYCOP UPDATE':
                    embed['author']['name'] = 'Easycop update'
                    webhook_url = easycop_update
                else:
                    webhook_url = 'https://discord.com/api/webhooks/861786508825853993/xxx'

                embed['footer']['text'] = embed_footer
                embed['footer']['icon_url'] = embed_icon
                embed['color'] = embed_color

                webhook = DiscordWebhook(
                    url=webhook_url)

                webhook.add_embed(embed)
                response = webhook.execute()

                print(str(datetime.datetime.now()) + ": " + "webhook sent")
            else:
                embed = event['d']['content']
                webhook_url = 'https://discord.com/api/webhooks/871216896446447616/xxx'
                webhook = DiscordWebhook(
                    url=webhook_url, content=embed)

                response = webhook.execute()

                print(str(datetime.datetime.now()) + ": " + "webhook sent")
        else:
            pass

        op_code = event['op']
        if op_code == 11:
            print('heartbeat received')
    except:
        pass

