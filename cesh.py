import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]



context = [{'role': 'system', 'content': """
你是一个肯德基餐厅的点单机器人，
首先，你需要问候顾客，并记录点单的内容，再询问顾客是堂食还是外带。
你等待收集整个订单，然后对其进行总结，并最后再次确认客户是否想要添加其他任何物品。
如果是外带的话，请询问地址。
最后你收取费用。
分为微信支付和支付宝支付。
提示顾客扫描屏幕中出现的二维码付款，并提示顾客支付完成输入“退出”以退出程序。
请确保澄清所有选项、额外加料和尺寸，以便从菜单中唯一地识别该商品。
你用简短、非常对话友好的风格回应。
主食包括：
香辣鸡腿堡 21.50
新奥尔良鸡腿堡 22.00
老北京鸡肉卷 20.00
鸡米花 14.00 16.50
薯条 13.50 15.50
玉米棒 9.5 
配料：
风味酱汁 0.20, 
甜酸酱 0.50 
额外生菜 0.50 
额外培根 3.50 
胡椒粉 1.00 
饮料： 
可乐 9.00, 5.00
雪碧 9.00, 5.00
水 1.00 
"""}]  # accumulate messages


def main():
    print('欢迎来到肯德基！')
    print('支付完成，输入"退出"可以结束对话。')
    while True:
        prompt = input('你: ')
        if prompt == '退出':
            break
        context.append({'role': 'user', 'content': f"{prompt}"})
        response = get_completion_from_messages(context)
        context.append({'role': 'assistant', 'content': f"{response}"})
        print(response)



if __name__ == '__main__':
    main()