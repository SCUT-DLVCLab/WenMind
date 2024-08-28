import json
import torch
import argparse

from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='Gemma-1.1-7B-IT_result.json')
parser.add_argument('--model_path', type=str, default='google/gemma-7b-it')
args = parser.parse_args()

tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(args.model_path, torch_dtype=torch.bfloat16, trust_remote_code=True).cuda()

model.generation_config.max_new_tokens = 2048
model.generation_config.temperature = 1.0
model.generation_config.top_p = 1
model.generation_config.top_k = 50
model.generation_config.repetition_penalty = 1.0
model.generation_config.do_sample = False

with open("../../WenMind_Benchmark/WenMind_ver1.json", "r", encoding = "utf-8") as f:
    data_test = json.load(f)

save_answer = []

for i,_ in enumerate(tqdm(data_test)):
    query = data_test[i]["question"]
    input_ids = tokenizer(query, return_tensors="pt").to("cuda")
    outputs = model.generate(**input_ids)
    response = tokenizer.decode(outputs[0]).replace("<bos>","").replace(query,"").replace("<eos>","").rstrip("\n")

    data_test[i]["LLM_name"] = "Gemma-1.1-7B-IT"
    data_test[i]["LLM_response"] = response
    save_answer.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_answer, f, ensure_ascii=False, indent=2)