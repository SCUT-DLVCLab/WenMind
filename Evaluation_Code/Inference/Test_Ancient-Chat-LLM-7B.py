import torch
import json
import argparse

from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='Ancient-Chat-LLM-7B_result.json')
parser.add_argument('--model_path', type=str, default='HinGwenWoong/ancient-chat-7b')
args = parser.parse_args()

if args.model_path == 'HinGwenWoong/ancient-chat-7b':
    from modelscope import snapshot_download
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

model = model.eval()

with open("../../WenMind_Benchmark/WenMind_ver1.json", "r", encoding = "utf-8") as f:
    data_test = json.load(f)

save_answer = []

for i,_ in enumerate(tqdm(data_test)):
    
    instruction = """<s><|im_start|>system\n你精通中国文化和中文知识，你总能解答用户关于中国文化和中文的相关知识。<|im_end|>\n<|im_start|>user\n{}<|im_end|>\n<|im_start|>assistant\n"""
    string = data_test[i]["question"]
    prompt = instruction.format(string)
    inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
    generated_ids = model.generate(**inputs, eos_token_id=tokenizer.eos_token_id)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, generated_ids)]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    data_test[i]["LLM_name"] = "Ancient-Chat-LLM-7B"
    data_test[i]["LLM_response"] = response
    save_answer.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_answer, f, ensure_ascii=False, indent=2)