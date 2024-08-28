import json
import torch
import argparse

from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='LLaMA3-8B-Instruct_result.json')
parser.add_argument('--model_path', type=str, default='meta-llama/Meta-Llama-3-8B-Instruct')
args = parser.parse_args()

tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(args.model_path, torch_dtype=torch.bfloat16, trust_remote_code=True).cuda()
model.eval()

with open("../../WenMind_Benchmark/WenMind_ver1.json", "r", encoding = "utf-8") as f:
    data_test = json.load(f)

save_list = []

for i,_ in enumerate(tqdm(data_test)):
    string = data_test[i]["question"]
    messages = [
        {"role": "user", "content": string},
    ]
    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)
    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]
    outputs = model.generate(
        input_ids,
        max_new_tokens=2048,
        eos_token_id=terminators,
        do_sample=False,
        temperature=1.0,
        top_p=1,
        top_k=50,
        repetition_penalty=1.0,
    )
    response = outputs[0][input_ids.shape[-1]:]
    response = tokenizer.decode(response, skip_special_tokens=True)
    
    data_test[i]["LLM_name"] = "LLaMA3-8B-Instruct"
    data_test[i]["LLM_response"] = response
    save_list.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_list, f, ensure_ascii=False, indent=2)