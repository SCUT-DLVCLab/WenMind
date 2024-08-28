import json
import torch
import argparse

from tqdm import tqdm
from transformers import AutoTokenizer, AutoModel

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='ChatGLM2-6B_result.json')
parser.add_argument('--model_path', type=str, default='THUDM/chatglm2-6b')
args = parser.parse_args()

chat_tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code = True)
chat_model = AutoModel.from_pretrained(args.model_path, trust_remote_code = True).cuda()

# chat_model.generation_config.max_new_tokens = 2048
# chat_model.generation_config.temperature = 1.0
# chat_model.generation_config.top_p = 1
# chat_model.generation_config.top_k = 50
# chat_model.generation_config.repetition_penalty = 1.0
# chat_model.generation_config.do_sample = False

chat_model = chat_model.eval()

with open("../../WenMind_Benchmark/WenMind_ver1.json", "r", encoding = "utf-8") as f:
    data_test = json.load(f)

save_answer = []

for i,_ in enumerate(tqdm(data_test)):
    query = data_test[i]["question"]
    response, _ = chat_model.chat(
        chat_tokenizer, 
        query, 
        history = [], 
        max_new_tokens = 2048,
        temperature = 1.0,
        top_p = 1,
        top_k = 50,
        repetition_penalty = 1.0,
        do_sample = False
    )

    data_test[i]["LLM_name"] = "ChatGLM2-6B"
    data_test[i]["LLM_response"] = response
    save_answer.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_answer, f, ensure_ascii=False, indent=2)