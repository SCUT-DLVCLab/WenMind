import json
import torch
import argparse

from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='Ziya-LLaMA-13B_result.json')
parser.add_argument('--model_path', type=str, default='IDEA-CCNL/Ziya-LLaMA-13B-v1.1')
args = parser.parse_args()

tokenizer = AutoTokenizer.from_pretrained(args.model_path, use_fast=False, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(args.model_path, device_map="auto", torch_dtype=torch.bfloat16, trust_remote_code=True)
# model.generation_config = GenerationConfig.from_pretrained(args.model_path)

model.generation_config.max_new_tokens = 2048
model.generation_config.temperature = 1.0
model.generation_config.top_p = 1
model.generation_config.top_k = 50
model.generation_config.repetition_penalty = 1.0
model.generation_config.do_sample = False
model = model.eval()

with open("../../WenMind_Benchmark/WenMind_ver1.json", "r", encoding = "utf-8") as f:
    data_test = json.load(f)

save_list = []

for i,_ in enumerate(tqdm(data_test)):
    instruction = """<human>:{}\n<bot>:"""
    string = data_test[i]["question"]
    prompt = instruction.format(string)
    inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
    generated_ids = model.generate(**inputs, eos_token_id=tokenizer.eos_token_id)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, generated_ids)]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    data_test[i]["LLM_name"] = "Ziya-LLaMA-13B"
    data_test[i]["LLM_response"] = response
    save_list.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_list, f, ensure_ascii=False, indent=2)