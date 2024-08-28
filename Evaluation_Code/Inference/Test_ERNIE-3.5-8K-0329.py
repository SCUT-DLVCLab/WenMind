import requests
import json
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--API_KEY', type=str, required=True)
parser.add_argument('--SECRET_KEY', type=str, required=True)
parser.add_argument('--output_path', type=str, default='ernie3.5_result.json')
args = parser.parse_args()

def main_use(all_prompt):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-3.5-8k-0329?access_token=" + get_access_token()
    payload = json.dumps({
        "temperature": 1.0,
        "top_p": 1.0,
        "top_k": 50,
        "penalty_score": 1,
        "disable_search": True,
        "enable_citation": False,
        "enable_trace": False,
        "max_new_tokens": 2048,
        "do_sample": False,
        "messages": [
            {
                "role": "user",
                "content": all_prompt
            }
        ],
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
    
def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": args.API_KEY, "client_secret": args.SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

with open("../../WenMind_Benchmark/WenMind_ver1.json", "r", encoding = "utf-8") as f:
    data_test = json.load(f)

save_answer = []

for i,_ in enumerate(tqdm(data_test)):
    query = data_test[i]["question"]
    response_json = json.loads(main_use(query))
    response_text = response_json["result"]

    data_test[i]["LLM_name"] = "ERNIE-3.5-8K-0329"
    data_test[i]["LLM_response"] = response_text
    save_answer.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_answer, f, ensure_ascii=False, indent=2)