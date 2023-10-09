import requests
import readline
import os
group_id = os.getenv('GROUP_ID')
api_key =  os.getenv('API_KEY')

url = f'https://api.minimax.chat/v1/text/chatcompletion?GroupId={group_id}'
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

#prefix, user_name, bot_name = choose_prefix()
#tokens_to_generate可自行修改
request_body = {
        "model":"abab5-chat",
        "tokens_to_generate": 512,
        'messages': []
}
#添加循环完成多轮交互
while True:
    #下面的输入获取是基于python终端环境，请根据您的场景替换成对应的用户输入获取代码
    line = input("发言:")
    # 将当次输入内容作为用户的一轮对话添加到messages
    request_body['messages'].append({"sender_type": "USER","text": line})
    response = requests.post(url, headers=headers, json=request_body)
    reply = response.json()['reply']
    print(f"reply: {reply}")
    #  将当次的ai回复内容加入messages
    request_body['messages'].append({"sender_type": "BOT","text": reply})
