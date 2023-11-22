import openai

# 设置OpenAI API密钥
openai.api_key = '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'

# 初始化对话历史
conversation_history = []

# 开始对话循环
while True:
    # 接收用户输入
    user_input = input("User: ")

    if user_input == 'bye':
        print('byebye')
        break
    # 将用户输入添加到对话历史中
    conversation_history.append({'role': 'user', 'content': user_input})

    # 发送请求与ChatGPT进行对话
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=conversation_history,
        max_tokens=200,
        n=2,
        stop=None
    )

    # 提取模型的回复
    model_reply = response['choices'][0]['message']['content']

    # 将模型回复打印出来
    print('ChatGPT:', model_reply)

    # 将模型回复添加到对话历史中
    conversation_history.append({'role': 'assistant', 'content': model_reply})
