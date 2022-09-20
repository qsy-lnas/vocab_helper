import json
import datetime
import os
import sys

def write_word(word_dict):
    if word_dict == None: return 
    # 判断词库文件是否为空
    if not os.path.getsize("words.json"):
        word_list = []
    else:    
        with open("words.json", 'r', encoding = "utf-8") as f:
            word_list = json.load(f)
    # 不判断单词是否重复
    word_list.append(word_dict)
    with open("words.json", 'w', encoding = "utf-8") as f:
        f.write(json.dumps(word_list, ensure_ascii = False, indent = 2))

def add_word(word):
    # 通过命令行输入方式添加新词
    # 时间自动生成
    today = datetime.date.today()
    eng_ch = word.split('|', 2)
    word_dict = {
        "vocab": eng_ch[0].strip(), 
        "ch": eng_ch[1].strip(),
        "date": str(today),
        "wt": 0,
        "rt": 0
    }
    if not os.path.getsize("words.json"):
        word_list = []
    else:    
        with open("words.json", 'r', encoding = "utf-8") as f:
            word_list = json.load(f)
    for i in word_list:
        if word_dict["vocab"] == i["vocab"]:
            print("Repetition Word!")
            print("Add New Word Error!")
            return None
    return word_dict

def console_command():
    while(1):
        command = input('add/delete/modify/test/exit\n').strip().lower()
        if command == "add":
            print('input a new word with \"eng|ch\" OR exit:\r')
            while(1):
                word = input()
                if word.strip() == "exit":
                    break
                elif '|' not in word.strip():
                    print('Illegal Input!')
                    continue
                dict1 = add_word(word)
                write_word(dict1)
        elif command == "delete" or command == "del":
            print("No this function now")
        elif command == "modify" or command == "mod":
            print("No this function now")
        elif command == "test":
            print("No this function now")
        elif command == "exit" or command == "quit":
            os._exit(0)

if __name__ == "__main__":
    # today = datetime.date.today()
    # dict1 = {
    #     "vocab": "ilustrate", 
    #     "ch": "说明",
    #     "date": str(today),
    #     "wt": 0,
    #     "rt": 0
    # }
    # write_word(dict1)
    console_command()
