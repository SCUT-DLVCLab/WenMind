import json
import torch
import argparse

from tqdm import tqdm
from modelscope import snapshot_download
from transformers import AutoTokenizer, AutoModelForCausalLM

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='Xunzi-Qwen1.5-7B_result.json')
parser.add_argument('--model_path', type=str, default='Xunzillm4cc/Xunzi-Qwen1.5-7B_chat')
args = parser.parse_args()

if args.model_path == 'Xunzillm4cc/Xunzi-Qwen1.5-7B_chat':
    model_dir = snapshot_download(args.model_path)
else:
    model_dir = args.model_path

tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_dir, torch_dtype=torch.bfloat16, trust_remote_code=True).cuda()

model.generation_config.max_new_tokens = 2048
model.generation_config.temperature = 1.0
model.generation_config.top_p = 1
model.generation_config.top_k = 50
model.generation_config.repetition_penalty = 1.0
model.generation_config.do_sample = False

def use_model(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    model_inputs = tokenizer([text], return_tensors="pt").to('cuda')

    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=2048
    )

    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return response

with open('../../WenMind_Benchmark/WenMind_ver1.json', "r", encoding = "utf-8") as f:
    data_test = json.load(f)

save_answer = []

for i,_ in enumerate(tqdm(data_test)):
    query = data_test[i]["question"]
    response = use_model(query)

    data_test[i]["LLM_name"] = "Xunzi-Qwen1.5-7B"
    data_test[i]["LLM_response"] = response
    save_answer.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_answer, f, ensure_ascii=False, indent=2)