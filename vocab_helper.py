import json
import datetime
import os

def write_word(word_dict):
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

def add_word():
    # 通过命令行输入方式添加新词
    # 时间自动生成
    today = datetime.date.today()
    word = input('input a new word with \"eng|ch\":')
    eng_ch = word.split('|', 2)
    word_dict = {
        "vocab": eng_ch[0].strip(), 
        "ch": eng_ch[1].strip(),
        "date": str(today),
        "wt": 0,
        "rt": 0
    }
    return word_dict

if __name__ == "__main__":
    # today = datetime.date.today()
    # dict1 = {
    #     "vocab": "ilustrate", 
    #     "ch": "说明",
    #     "date": str(today),
    #     "wt": 0,
    #     "rt": 0
    # }
    
    dict1 = add_word()

    write_word(dict1)