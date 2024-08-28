import json
import torch
import argparse

from tqdm import tqdm
from transformers.generation.utils import GenerationConfig
from transformers import AutoTokenizer, AutoModelForCausalLM

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='Baichuan2-7B-Chat_result.json')
parser.add_argument('--model_path', type=str, default='baichuan-inc/Baichuan2-7B-Chat')
args = parser.parse_args()

chat_tokenizer = AutoTokenizer.from_pretrained(args.model_path, use_fast=False, trust_remote_code=True)
chat_model = AutoModelForCausalLM.from_pretrained(args.model_path, device_map="auto", torch_dtype=torch.bfloat16, trust_remote_code=True)
chat_model.generation_config = GenerationConfig.from_pretrained(args.model_path)
chat_model.eval()

chat_model.generation_config.max_new_tokens = 2048
chat_model.generation_config.temperature = 1.0
chat_model.generation_config.top_p = 1
chat_model.generation_config.top_k = 50
chat_model.generation_config.repetition_penalty = 1.0
chat_model.generation_config.do_sample = False

with open("../../WenMind_Benchmark/WenMind_ver1.json", "r", encoding = "utf-8") as f:
    data_test = json.load(f)

save_answer = []

for i,_ in enumerate(tqdm(data_test)):
    query = data_test[i]["question"]
    messages = []
    messages.append({"role": "user", "content": query})
    response = chat_model.chat(chat_tokenizer, messages)

    data_test[i]["LLM_name"] = "Baichuan2-7B-Chat"
    data_test[i]["LLM_response"] = response
    save_answer.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_answer, f, ensure_ascii=False, indent=2)