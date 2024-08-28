import SparkAPI
import json
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='Spark_result.json')
parser.add_argument('--appid', type=str, required=True)
parser.add_argument('--api_secret', type=str, required=True)
parser.add_argument('--api_key', type=str, required=True)
args = parser.parse_args()

def main_use(args, all_prompt):
    domain = "generalv3.5"
    Spark_url = "ws://spark-api.xf-yun.com/v3.5/chat"
    question = [
        {
            "role": "user",
            "content": all_prompt
        }
    ]
    SparkAPI.answer =""
    SparkAPI.main(args.appid, args.api_key, args.api_secret, Spark_url, domain, question)
    result = str(SparkAPI.answer).strip()

    return result

with open("../../WenMind_Benchmark/WenMind_ver1.json", "r", encoding = "utf-8") as f:
    data_test = json.load(f)

save_answer = []

for i,_ in enumerate(tqdm(data_test)):
    query = data_test[i]["question"]
    response_text = main_use(args, query)

    data_test[i]["LLM_name"] = "Spark-3.5"
    data_test[i]["LLM_response"] = response_text
    save_answer.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_answer, f, ensure_ascii=False, indent=2)