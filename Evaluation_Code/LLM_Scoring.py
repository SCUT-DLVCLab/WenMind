#  Evaluating LLM Responses Using ERNIE-3.5

import requests
import json
from tqdm import tqdm

#  Enter [ERNIE-3.5 model's API_KEY and SECRET_KEY] here
API_KEY = "your_API_KEY"
SECRET_KEY = "your_SECRET_KEY"

#  Enter [the file storage path for the responses of different models] here
LLM_response_path = "/your/storage/path/LLM_response.json"

# Enter [the file storage path for the files scored by ERNIE-3.5 model] here
LLM_score_path = "/your/storage/path/LLM_score.json"

# Enter [the file storage path for the scoring prompts] here
LLM_prompt_path = "/your/storage/path/Task_Score_Prompt.json"

def main_use(all_prompt):  
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-3.5-8k-0329?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": all_prompt
            }
        ],
        "disable_search": False,
        "enable_citation": False
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
    
def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

with open(LLM_response_path, 'r') as file:
    data = json.load(file)

with open(LLM_prompt_path, 'r') as file:
    prompt_list = json.load(file)

multi_choice = [3627,3630,3632,3633,3635,3637,3643,3646,3650,3666,3671,3672,3674]
all_list = []

for i in tqdm(range(0,len(data))):
    if data[i]["coarse_grained_task_zh"] == "文言文写作":
        input = prompt_list[7]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "七言律诗" in data[i]["question"]:
        input = prompt_list[8]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "五言律诗" in data[i]["question"]:
        input = prompt_list[9]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "七言绝句" in data[i]["question"]:
        input = prompt_list[10]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "五言绝句" in data[i]["question"]:
        input = prompt_list[11]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "七言排律" in data[i]["question"]:
        input = prompt_list[12]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "五言排律" in data[i]["question"]:
        input = prompt_list[13]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "念奴娇" in data[i]["question"]:
        input = prompt_list[14]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "满江红" in data[i]["question"]:
        input = prompt_list[15]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "虞美人" in data[i]["question"]:
        input = prompt_list[16]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "浣溪沙" in data[i]["question"]:
        input = prompt_list[17]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "菩萨蛮" in data[i]["question"]:
        input = prompt_list[18]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "水调歌头" in data[i]["question"]:
        input = prompt_list[19]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "卜算子" in data[i]["question"]:
        input = prompt_list[20]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "如梦令" in data[i]["question"]:
        input = prompt_list[21]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "渔家傲" in data[i]["question"]:
        input = prompt_list[22]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "西江月" in data[i]["question"]:
        input = prompt_list[23]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "天净沙" in data[i]["question"]:
        input = prompt_list[24]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "山坡羊" in data[i]["question"]:
        input = prompt_list[25]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "湘妃怨" in data[i]["question"]:
        input = prompt_list[26]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "古诗词创作" and "清江引" in data[i]["question"]:
        input = prompt_list[27]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "对联" and data[i]["fine_grained_task_zh"] == "接下联":
        input = prompt_list[4]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "对联" and data[i]["fine_grained_task_zh"] == "对联创作":
        input = prompt_list[5]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "对联" and data[i]["fine_grained_task_zh"] == "拟横批":
        input = prompt_list[6]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["coarse_grained_task_zh"] == "成语" and data[i]["fine_grained_task_zh"] == "近义词":
        input = prompt_list[3]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    elif data[i]["question_format"] == "MCQ" and data[i]["id"] in multi_choice:
        input = prompt_list[1]["prompt"].format(data[i]["LLM_response"],data[i]["answer"])
    elif data[i]["question_format"] == "MCQ" and data[i]["id"] not in multi_choice and data[i]["coarse_grained_task_zh"] != "情感分类":
        input = prompt_list[0]["prompt"].format(data[i]["LLM_response"],data[i]["answer"])
    elif data[i]["coarse_grained_task_zh"] == "情感分类":
        input = prompt_list[2]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])
    else:
        input = prompt_list[2]["prompt"].format(data[i]["LLM_response"],data[i]["answer"],data[i]["question"])      

    response_json = json.loads(main_use(input))
    response_text = response_json["result"]
    data[i]["LLM_score"] = response_text
    all_list.append(data[i])

    #  Save file
    with open(LLM_score_path, "w", encoding="utf-8") as f:
        json.dump(all_list, f, ensure_ascii=False, indent=2)