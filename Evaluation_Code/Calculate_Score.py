#  Calculate Model Score

import json
import locale

locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8')

# Enter [the file storage path for the files scored by ERNIE-3.5 model] here
LLM_score_path = "/your/storage/path/LLM_score.json"

with open(LLM_score_path, "r", encoding = "utf-8") as f:
    data = json.load(f)

all_score = []

for i in range(len(data)):
    data[i]["LLM_score"] = data[i]["LLM_score"].replace("\\n","").replace("\n","").replace("”]","\"]")
    score_list = json.loads(data[i]["LLM_score"])
    print("Data with ID {} has been loaded".format(i))

    # Check if the LLM scoring meets the specifications
    if len(score_list) > 3:
        raise ValueError("The scoring list exceeds 3 items, which does not meet the requirements.")
    if len(score_list) == 1 or len(score_list) == 2:
        score_list[0] = float(score_list[0])
        if score_list[0] > 1:
            raise ValueError("The score given exceeds 1, which does not meet the requirements.")
        if score_list[0] < 0:
            raise ValueError("The score given is less than 0, which does not meet the requirements.")
    if len(score_list) == 3:
        score_list[0] = float(score_list[0])
        score_list[1] = float(score_list[1])
        if score_list[0] < 1:
            raise ValueError("The score for the reference answer must be at least 1 point.")
        if score_list[0] < score_list[1]:
            score_list[1] = score_list[0]

    #  Calculate Score
    if len(score_list) == 1 or len(score_list) == 2:
        all_score.append(score_list[0])
    else:
        all_score.append(score_list[1]/score_list[0])

print("\nAll Score:", sum(all_score)/len(all_score))

related_dic = {"文言文句式":"T01",
               "文言文-白话文翻译":"T02",
               "白话文-文言文翻译":"T03",
               "命名实体识别":"T04",
               "文言文句读":"T05",
               "文言文主题分类":"T06",
               "文言文字词解释":"T07",
               "文言文阅读理解":"T08",
               "文言文虚词":"T09",
               "文言文通假字":"T10",
               "文言文单字多义":"T11",
               "文言文写作":"T12",
               "古诗词赏析":"T13",
               "古诗词创作":"T14",
               "古诗词基础问答":"T15",
               "古诗词-白话文翻译":"T16",
               "古诗词情感分类":"T17",
               "古诗词-英文翻译":"T18",
               "诗人介绍":"T19",
               "意象解析":"T20",
               "对联":"T21",
               "成语":"T22",
               "谜语":"T23",
               "歇后语":"T24",
               "古汉语音韵":"T25",
               "国学常识问答":"T26"
               }

related_dic_2 = {"倒装句语序":"T01-1",
                 "省略句":"T01-2",
                 "倒装句类型":"T01-3",
                 "判断句式":"T01-4",
                 "古诗词赏析真题":"T13-1",
                 "古诗词自由赏析":"T13-2",
                 "诗创作":"T14-1",
                 "词创作":"T14-2",
                 "曲创作":"T14-3",
                 "古诗词内容回答":"T15-1",
                 "古诗词题目作者回答":"T15-2",
                 "古诗词下句默写":"T15-3",
                 "古诗词上句默写":"T15-4",
                 "古诗词理解性默写":"T15-5",
                 "判断古诗词体裁":"T15-6",
                 "接下联":"T21-1",
                 "对联主题创作":"T21-2",
                 "拟横批":"T21-3",
                 "近义词":"T22-1",
                 "成语出处":"T22-2",
                 "成语蕴含":"T22-3",
                 "解释含义":"T22-4"
               }

#  Scores corresponding to different tasks
print("\nClassified according to different tasks")
question_types_list = list(set(d['task_name'] for d in data))
question_types_list = sorted(question_types_list, key=locale.strxfrm)
question_types_list_sub = list(set(d['detail_task_name'] for d in data))
question_types_list_sub = sorted(question_types_list_sub, key=locale.strxfrm)
sentence_list = []

for j in range(len(question_types_list)):
    score_list_sub = []
    for k in range(len(data)):
        if data[k]["task_name"] == question_types_list[j]:
            score_list_sub.append(all_score[k])
    string = "Task(Coarse-grained):" + question_types_list[j] + " Score:" + str(sum(score_list_sub)/len(score_list_sub))
    print(string)
    string_2 = "Task(Coarse-grained):" + related_dic[question_types_list[j]] + " Score:" + str(sum(score_list_sub)/len(score_list_sub))
    sentence_list.append(string_2)

sentence_list = sorted(sentence_list)
print("\n")
for i in range(len(sentence_list)):
    print(sentence_list[i])
print("\n")
string_sub = []
sentence_list_2 = []

for j in range(len(question_types_list_sub)):
    if question_types_list_sub[j] == "":
        continue
    score_list_sub = []
    flag = 0
    for k in range(len(data)):
        if data[k]["detail_task_name"] == question_types_list_sub[j]:
            score_list_sub.append(all_score[k])
            flag = k
    string = "Task(Coarse-grained):" + data[flag]["task_name"] + " Task(Fine-grained):" + question_types_list_sub[j] + " 得分:" + str(sum(score_list_sub)/len(score_list_sub))
    string_sub.append(string)
    string_2 = "Task(Fine-grained):" + related_dic_2[question_types_list_sub[j]] + " Score:" + str(sum(score_list_sub)/len(score_list_sub))
    sentence_list_2.append(string_2)

string_sub = sorted(string_sub, key=locale.strxfrm)
for item in string_sub:
    print(item)
sentence_list_2 = sorted(sentence_list_2)
print("\n")
for i in range(len(sentence_list_2)):
    print(sentence_list_2[i])

#  Scores corresponding to different question types
print("\nClassified according to different question types")
question_types_list = ["FB","MCQ","QA"]

for j in range(len(question_types_list)):
    score_list_sub = []
    for k in range(len(data)):
        if data[k]["question_type"] == "TF":
            data[k]["question_type"] = "QA"
        if data[k]["question_type"] == question_types_list[j]:
            score_list_sub.append(all_score[k])
    string = "Question Type:" + question_types_list[j] + " Score:" + str(sum(score_list_sub)/len(score_list_sub))
    print(string)

#  Scores corresponding to different capabilities
ability_list_generation = []
ability_list_comprehension = []
ability_list_knowledge = []

task_name_generation = ["文言文写作","古诗词创作","对联"]
task_name_comprehension = ["文言文句式","文言文-白话文翻译","白话文-文言文翻译","命名实体识别","文言文句读","文言文主题分类","文言文字词解释","文言文阅读理解","文言文虚词","文言文通假字","文言文单字多义","古诗词赏析","古诗词-白话文翻译","古诗词情感分类","古诗词-英文翻译"]
task_name_knowledge = ["古诗词基础问答","诗人介绍","意象解析","成语","谜语","歇后语","古汉语音韵","国学常识问答"]

for i in range(len(data)):
    if data[i]["task_name"] in task_name_generation:
        ability_list_generation.append(all_score[i])
    if data[i]["task_name"] in task_name_comprehension:
        ability_list_comprehension.append(all_score[i])
    if data[i]["task_name"] in task_name_knowledge:
        ability_list_knowledge.append(all_score[i])

print("\nClassified according to different capabilities")
print("Capability:Understanding Score:{}".format(sum(ability_list_comprehension)/len(ability_list_comprehension)))
print("Capability:Generation Score:{}".format(sum(ability_list_generation)/len(ability_list_generation)))
print("Capability:Knowledge Score:{}".format(sum(ability_list_knowledge)/len(ability_list_knowledge)))

#  Scores corresponding to different domains
domain_list_1 = []
domain_list_2 = []
domain_list_3 = []

domain_name_1 = ["文言文句式","文言文-白话文翻译","白话文-文言文翻译","命名实体识别","文言文句读","文言文主题分类","文言文字词解释","文言文阅读理解","文言文虚词","文言文通假字","文言文单字多义","文言文写作"]
domain_name_2 = ["古诗词赏析","古诗词创作","古诗词基础问答","古诗词-白话文翻译","古诗词情感分类","古诗词-英文翻译","诗人介绍","意象解析"]
domain_name_3 = ["对联","成语","谜语","歇后语","古汉语音韵","国学常识问答"]

for i in range(len(data)):
    if data[i]["task_name"] in domain_name_1:
        domain_list_1.append(all_score[i])
    if data[i]["task_name"] in domain_name_2:
        domain_list_2.append(all_score[i])
    if data[i]["task_name"] in domain_name_3:
        domain_list_3.append(all_score[i])

print("\nClassified according to different domains")
print("Domain:Ancient Prose Score:{}".format(sum(domain_list_1)/len(domain_list_1)))
print("Domain:Ancient Poetry Score:{}".format(sum(domain_list_2)/len(domain_list_2)))
print("Domain:Ancient Literary Culture Score:{}".format(sum(domain_list_3)/len(domain_list_3)))