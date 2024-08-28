import torch
import json
import argparse

from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='Bloom-7B-Chunhua_result.json')
parser.add_argument('--model_path', type=str, default='wptoux/bloom-7b-chunhua')
args = parser.parse_args()

tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
  args.model_path,
  device_map='auto',
  torch_dtype=torch.bfloat16,
  trust_remote_code=True
)
model.eval()

model.generation_config.max_new_tokens = 2048
model.generation_config.temperature = 1.0
model.generation_config.top_p = 1
model.generation_config.top_k = 50
model.generation_config.repetition_penalty = 1.0
model.generation_config.do_sample = False

with open("../../WenMind_Benchmark/WenMind_ver1.json", "r", encoding = "utf-8") as f:
    data_test = json.load(f)

save_list = []

for i,_ in enumerate(tqdm(data_test)):
    instruction = """<|im_start|>系统\n你是春华，一个基于Bloom的古汉语问答模型，使用汉语古典文本数据库scripta-sinica进行微调，你具有丰富的中华古代知识，以及较强的古汉语理解能力。\n<|im_end|>\n<|im_start|>用户\n{}\n<|im_end|>\n<|im_start|>助手"""
    string = data_test[i]["question"]
    prompt = instruction.format(string)
    inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
    generated_ids = model.generate(**inputs, eos_token_id=tokenizer.eos_token_id)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, generated_ids)]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    data_test[i]["LLM_name"] = "Bloom-7B-Chunhua"
    data_test[i]["LLM_response"] = response
    save_list.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_list, f, ensure_ascii=False, indent=2)