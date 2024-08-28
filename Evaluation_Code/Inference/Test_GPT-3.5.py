import openai
import json
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='GPT-3.5_result.json')
parser.add_argument('--api_base', type=str, required=True, help='转发')
parser.add_argument('--api_key', type=str, required=True)
args = parser.parse_args()

openai.api_base = args.api_base
openai.api_key = args.api_key

def main_use(all_prompt):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "user", "content": all_prompt}
    ],
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=1,
    )
    # generated_text = completion.choices[0].text
    result = completion.choices[0]["message"]["content"]
    return result

with open("../../WenMind_Benchmark/WenMind_ver1.json", "r", encoding = "utf-8") as f:
    data_test = json.load(f)

save_answer = []

for i,_ in enumerate(tqdm(data_test)):
    query = data_test[i]["question"]
    response_text = main_use(query)

    data_test[i]["LLM_name"] = "GPT-3.5"
    data_test[i]["LLM_response"] = response_text
    save_answer.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_answer, f, ensure_ascii=False, indent=2)