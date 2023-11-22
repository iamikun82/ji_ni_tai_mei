import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

text_path = input("Please enter the address of text path:")

# r for read, w for write, a 追加模式
try:
    file = open(text_path, "r", encoding="utf-8" )
    text = file.read()
    file.close()

    print("contents of file as follows:")
    print(text)              # 1.open the text file

except FileNotFoundError:
    print(f"文件 '{text_path}' 不存在。")
except Exception as e:
    print(f"发生错误：{str(e)}")


print("----------------------------------------------------------------")
# _______________________________________________________________

#2.open the file of prompt
prompt_path = input("Please enter the address of prompt path:")
try:
    file = open(prompt_path, "r", encoding="utf-8")
    prompt = file.read()
    file.close()

    print("contents of file as follows:")
    print(prompt)
    response = get_completion(prompt)
    print(response)
except FileNotFoundError:
    print(f"文件 '{prompt_path}' 不存在。")
except Exception as e:
    print(f"发生错误：{str(e)}")

# 3.output the result

