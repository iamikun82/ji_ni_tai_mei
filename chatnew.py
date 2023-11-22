import openai


openai.api_key = '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'


def save_dialogue(dialogue):
    with open('dialogue.txt', 'a', encoding='utf-8') as file:
        file.write(dialogue + '\n')


def load_dialogue():
    dialogue = []
    with open('dialogue.txt', 'r', encoding='utf-8') as file:
        for line in file:
            dialogue.append(line.strip())
    return ''.join(dialogue)


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response['choices'][0]['message']
# .choices[0].message["content"]
def main():
    print('欢迎来到对话小程序！')
    print('你可以开始和我聊天。输入"退出"可以结束对话。')
    while True:
        prompt = input('你: ')
        if prompt == '退出':
            break
        save_dialogue(f'{prompt}')
        prompt = load_dialogue()
        print(get_completion(prompt))




if __name__ == '__main__':
    main()


