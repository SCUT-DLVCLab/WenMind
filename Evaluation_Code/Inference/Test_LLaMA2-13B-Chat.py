import json
import torch
import argparse

from tqdm import tqdm
from transformers.generation.utils import GenerationConfig
from transformers import AutoTokenizer, AutoModelForCausalLM

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='LLaMA2-13B-Chat_result.json')
parser.add_argument('--model_path', type=str, default='meta-llama/Llama-2-13b-chat-hf')
args = parser.parse_args()

tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(args.model_path, torch_dtype=torch.bfloat16, trust_remote_code=True).cuda()
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
    instruction = """[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.
                If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.\n<</SYS>>\n\n{} [/INST]"""

    string = data_test[i]["question"]
    prompt = instruction.format(string)
    inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
    generated_ids = model.generate(**inputs, eos_token_id=tokenizer.eos_token_id)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, generated_ids)]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    data_test[i]["LLM_name"] = "LLaMA2-13B-Chat"
    data_test[i]["LLM_response"] = response
    save_list.append(data_test[i])

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(save_list, f, ensure_ascii=False, indent=2)