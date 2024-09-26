# WenMind Benchmark

- 2024/09/26 WenMind Benchmark paper has been accepted by NeurIPS 2024.

WenMind is a comprehensive benchmark dedicated for evaluating Large Language Models (LLMs) in Chinese Classical Literature and Language Arts (CCLLA). WenMind covers the sub-domains of **Ancient Prose**, **Ancient Poetry**, and **Ancient Literary Culture**, comprising 4,875 question-answer pairs, spanning **42 fine-grained tasks** (as shown in the figure 1), **3 question formats** (Fill-in-the-Blank questions, Multiple-Choice questions and Question-and-Answer questions), and **2 evaluation scenarios** (domain-oriented and capability-oriented).

<p align="center">
    <img src="https://github.com/SCUT-DLVCLab/WenMind/blob/main/Images/WenMind_Overall.png" width="800"/>
<p>

<p align="center">
    <strong>Figure 1: Overview of WenMind Benchmark, which covers 3 sub-domains and 42 fine-gained tasks.</strong>
<p>
  
## Download

You can obtain the complete WenMind evaluation dataset from **WenMind Benchmark folder** on GitHub.

## Data Format
```
  {
    "id": 2464,
    "domain": "ancient literary culture",
    "capability": "knowledge",
    "question_format": "QA",
    "coarse_grained_task_zh": "成语",
    "coarse_grained_task_en": "idiom",
    "fine_grained_task_zh": "成语解释",
    "fine_grained_task_en": "idiom explanation",
    "question": "解释下面成语的意思：\n暮去朝来",
    "answer": "黄昏过去，清晨又到来。形容时光流逝。"
  }
```

The following is an explanation of the various fields in the data samples:

- **`id`**: The unique identifier for the data sample, used to distinguish different samples.

- **`domain`**: The domain to which the data sample belongs, including ancient prose, ancient poetry and ancient literary culture.

- **`capability`**: The type of capability of the data sample, including knowledge, understanding and generation.

- **`question_format`**: The format of the question, indicating the type of question in the sample, including FB, MCQ and QA.

- **`coarse_grained_task_zh`**: The Chinese name of the coarse-grained task classification. Describes the coarse-grained task category of the sample, with a total of 26 categories.

- **`coarse_grained_task_en`**: The English name of the coarse-grained task classification. Corresponds to **`coarse_grained_task_zh`**, describing the coarse-grained task category of the sample, with a total of 26 categories.

- **`fine_grained_task_zh`**: The Chinese name of the fine-grained task classification. Describes the fine-grained task category of the sample, with a total of 42 categories.

- **`fine_grained_task_en`**: The English name of the fine-grained task classification. Corresponds to **`fine_grained_task_zh`**, describing the fine-grained task category of the sample, with a total of 42 categories.

- **`question`**: The actual content of the question. The question to be answered in the sample.

- **`answer`**: The answer to the corresponding question. Provides a detailed response to the question.

## Task List

### T1-1: Inverted Sentence Structure (倒装句语序)
- **Task Description**: Correct word order for inverted sentences.
- **Capability**: Understanding
- **Scale**: 18

### T1-2: Elliptical Sentence (省略句)
- **Task Description**: Answer the omitted information in the elliptical sentence.
- **Capability**: Understanding
- **Scale**: 32

### T1-3: Inverted Sentence Types (倒装句类型)
- **Task Description**: Identify the inversion type of inverted sentences.
- **Capability**: Understanding
- **Scale**: 7

### T1-4: Sentence Structure Identification (判断句式)
- **Task Description**: Identify the sentence's syntactic type.
- **Capability**: Understanding
- **Scale**: 43

### T2: Classical Chinese to Modern Chinese (文白翻译)
- **Task Description**: Translate classical Chinese into modern Chinese.
- **Capability**: Understanding
- **Scale**: 200

### T3: Modern Chinese to Classical Chinese (白文翻译)
- **Task Description**: Translate modern Chinese into classical Chinese.
- **Capability**: Understanding
- **Scale**: 200

### T4: Named Entity Recognition (命名实体识别)
- **Task Description**: Extract named entities from Classical Chinese sentences.
- **Capability**: Understanding
- **Scale**: 200

### T5: Punctuation (句读)
- **Task Description**: Add punctuation to Classical Chinese sentences.
- **Capability**: Understanding
- **Scale**: 200

### T6: Topic Classification (主题分类)
- **Task Description**: Select theme categories based on Classical Chinese sentences.
- **Capability**: Understanding
- **Scale**: 200

### T7: Word Explanation (字词解释)
- **Task Description**: Explain the words and phrases in Classical Chinese sentences.
- **Capability**: Understanding
- **Scale**: 100

### T8: Reading Comprehension (阅读理解)
- **Task Description**: Read Classical Chinese texts and answer related questions.
- **Capability**: Understanding
- **Scale**: 100

### T9: Function Words (虚词)
- **Task Description**: Answer the usage of function words in classical Chinese sentences.
- **Capability**: Understanding
- **Scale**: 100

### T10: Homophones (通假字)
- **Task Description**: Identify whether a character is a homophone.
- **Capability**: Understanding
- **Scale**: 200

### T11: Polysemy (单字多义)
- **Task Description**: Distinguish between different meanings of the same character.
- **Capability**: Understanding
- **Scale**: 200

### T12: Classical Chinese Writing (文言文写作)
- **Task Description**: Writing in classical Chinese.
- **Capability**: Generation
- **Scale**: 100

### T13-1: Appreciation Exam Questions (赏析真题)
- **Task Description**: Answer appreciation questions based on ancient poetry.
- **Capability**: Understanding
- **Scale**: 150

### T13-2: Free Appreciation (自由赏析)
- **Task Description**: Conduct a free and detailed analysis of ancient poetry.
- **Capability**: Understanding
- **Scale**: 100

### T14-1: Poetry Writing (诗创作)
- **Task Description**: Compose a poem based on the theme.
- **Capability**: Generation
- **Scale**: 30

### T14-2: Ci Writing (词创作)
- **Task Description**: Compose a ci based on the theme.
- **Capability**: Generation
- **Scale**: 50

### T14-3: Qu Writing (曲创作)
- **Task Description**: Compose a qu based on the theme.
- **Capability**: Generation
- **Scale**: 20

### T15-1: Content Q&A (内容问答)
- **Task Description**: Answer the complete content of ancient poetry according to the title and author.
- **Capability**: Knowledge
- **Scale**: 200

### T15-2: Title and Author Q&A (题目作者问答)
- **Task Description**: Answer the title and author according to the content of ancient poetry.
- **Capability**: Knowledge
- **Scale**: 200

### T15-3: Write the Next Sentence (下句默写)
- **Task Description**: Write the next sentence according to the previous sentence in the ancient poem.
- **Capability**: Knowledge
- **Scale**: 100

### T15-4: Write the Previous Sentence (上句默写)
- **Task Description**: Write the previous sentence according to the next sentence in the ancient poem.
- **Capability**: Knowledge
- **Scale**: 100

### T15-5: Comprehension Dictation (理解性默写)
- **Task Description**: Provide ancient poetry sentences that meet the requirements.
- **Capability**: Knowledge
- **Scale**: 30

### T15-6: Genre Judgment (判断体裁)
- **Task Description**: Judge the genre of ancient poetry.
- **Capability**: Knowledge
- **Scale**: 120

### T16: Ancient Poetry Translation (古诗词翻译)
- **Task Description**: Translate ancient poetry into modern Chinese.
- **Capability**: Understanding
- **Scale**: 200

### T17: Sentiment Classification (情感分类)
- **Task Description**: Judge the sentiment contained in ancient poetry.
- **Capability**: Understanding
- **Scale**: 200

### T18: Ancient Poetry to English (古诗词英文翻译)
- **Task Description**: Translate ancient poetry into English.
- **Capability**: Understanding
- **Scale**: 50

### T19: Poet Introduction (诗人介绍)
- **Task Description**: Provide a detailed introduction of the poet.
- **Capability**: Knowledge
- **Scale**: 110

### T20: Analysis of Imagery (意象解析)
- **Task Description**: Provide the meanings of the imagery.
- **Capability**: Knowledge
- **Scale**: 185

### T21-1: Couplet Following (接下联)
- **Task Description**: Create the following couplet based on the previous one.
- **Capability**: Generation
- **Scale**: 100

### T21-2: Couplet Writing (主题创作)
- **Task Description**: Write a couplet based on the theme.
- **Capability**: Generation
- **Scale**: 100

### T21-3: HengPi Writing (拟横批)
- **Task Description**: Write HengPi based on the content of a couplet.
- **Capability**: Generation
- **Scale**: 100

### T22-1: Synonyms (近义词)
- **Task Description**: Provide the synonym for the idiom.
- **Capability**: Knowledge
- **Scale**: 100

### T22-2: The Origin of Idiom (成语出处)
- **Task Description**: Provide the source of the idiom.
- **Capability**: Knowledge
- **Scale**: 100

### T22-3: Idiom Finding (成语蕴含)
- **Task Description**: Extract idioms from ancient Chinese sentences and provide their meanings.
- **Capability**: Knowledge
- **Scale**: 100

### T22-4: Idiom Explanation (解释含义)
- **Task Description**: Provide the meaning of idioms.
- **Capability**: Knowledge
- **Scale**: 100

### T23: Riddle (谜语)
- **Task Description**: Guess the answer based on clues or clever hints.
- **Capability**: Knowledge
- **Scale**: 100

### T24: Xiehouyu (歇后语)
- **Task Description**: Complete the second half of the proverb based on the first half.
- **Capability**: Knowledge
- **Scale**: 100

### T25: Historical Chinese Phonology (古汉语音韵)
- **Task Description**: Answer questions about ancient Chinese phonetics and rhymes.
- **Capability**: Knowledge
- **Scale**: 100

### T26: Knowledge of Sinology Q&A (国学常识问答)
- **Task Description**: Answer questions about Sinology.
- **Capability**: Knowledge
- **Scale**: 130

## Data Construction

The construction pipeline of WenMind includes data collection and data processing, as illustrated in Figure 2.

<p align="center">
    <img src="https://github.com/SCUT-DLVCLab/WenMind/blob/main/Images/Data_Construction.png" width="550"/>
<p>

<p align="center">
    <strong>Figure 2: Construction pipeline of WenMind Benchmark.</strong>
<p>

## Data Statistics

Table 1 provides the statistics of the WenMind dataset.

<div align="center">

**Table 1: The statistics of the WenMind Benchmark. "Q" represents "Question" and "A" represents "Answer".**

<table>
  <thead>
    <tr>
      <th align="left"><strong>Domain</strong></th>
      <th align="center"><strong>Tasks</strong></th>
      <th align="center"><strong>#Q</strong></th>
      <th align="center"><strong>Max. #Q</strong></th>
      <th align="center"><strong>Min. #Q</strong></th>
      <th align="center"><strong>Avg. Q Tokens</strong></th>
      <th align="center"><strong>Avg. A Tokens</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">Ancient Prose</td>
      <td align="center">15</td>
      <td align="center">1,900</td>
      <td align="center">200</td>
      <td align="center">7</td>
      <td align="center">107.51</td>
      <td align="center">62.12</td>
    </tr>
    <tr>
      <td align="left">Ancient Poetry</td>
      <td align="center">16</td>
      <td align="center">1,845</td>
      <td align="center">200</td>
      <td align="center">20</td>
      <td align="center">73.42</td>
      <td align="center">94.93</td>
    </tr>
    <tr>
      <td align="left">Ancient Literary Culture</td>
      <td align="center">11</td>
      <td align="center">1,130</td>
      <td align="center">100</td>
      <td align="center">100</td>
      <td align="center">26.68</td>
      <td align="center">14.26</td>
    </tr>
    <tr>
      <td align="left"><strong>Overall</strong></td>
      <td align="center">42</td>
      <td align="center">4,875</td>
      <td align="center">200</td>
      <td align="center">7</td>
      <td align="center">75.87</td>
      <td align="center">63.44</td>
    </tr>
  </tbody>
</table>

</div>

## Inference

### a. Obtain the model’s responses

#### Open-source Model

For open-source models, we perform inference locally, only requiring the model path and the output file path for the answers.

```
--model_path The path to the model, defaults to loading from huggingface
--output_path The file path for the model's answer output, defaults to {model_name}_result.json
```

e.g.

```
CUDA_VISIBLE_DEVICES=0,1 python Evaluation_Code/Inference/Test_Baichuan2-7B-Chat.py \  
    --model_path baichuan-inc/Baichuan2-7B-Chat \  
    --output_path Baichuan2-7B-Chat_result.json
```

#### API Model

For GPT-3.5 and GPT-4 models, provide two parameters: `api_base` and `api_key`.  
For ERNIE-3.5 and ERNIE-4.0 models, provide two parameters: `api_key` and `secret_key`.  
For Spark models, provide three parameters: `api_key`, `secret_key`, and `appid`.  
Refer to the official documentation of each API model for details.  

e.g.

```
python Test_ERNIE-3.5-8K-0329.py \
    --API_KEY {api_key} \
    --SECRET_KEY {secret_key} \
    --output_path {output_path}
```
### b. Use ERNIE-3.5 to score the responses

Step 1: Check whether the LLM response file is consistent with the format of the `JSON/LLM_Response_Examples.json` file.

Step 2: Open the `Evaluation_Code/LLM_Scoring.py` file, input the `API_KEY` and `SECRET_KEY` for the scoring model ERNIE-3.5, replace `LLM_response_path` with the storage path of the LLM response file, replace `LLM_score_path` with the path where the scoring results will be saved, and replace `LLM_prompt_path` with the storage path of `JSON/Task_Score_Prompt.json`.

Step 3: Run the following command to obtain the scoring results:

```
python Evaluation_Code/LLM_Scoring.py 
```

### c. Calculate the model’s score

Step 1: Check whether the scoring file is consistent with the format of the `JSON/LLM_Score_Examples.json` file.

Step 2: Open the `Evaluation_Code/Calculate_Score.py` file and replace `LLM_score_path` with the storage path of the scoring file.

Step 3: Run the following command to obtain the model's score:

```
python Evaluation_Code/Calculate_Score.py 
```
## Evaluation Result

<p align="center">
    <strong>Table 2: Results of all evaluated models on different domains and capabilities.</strong>
<p>
<p align="center">
    <img src="https://github.com/SCUT-DLVCLab/WenMind/blob/main/Images/Evaluation_Result.png" width="750"/>
<p>


## Acknowledgement

- [SCUT-C2MChn](https://github.com/Zongyuan-Jiang/C2MChn)
- [WYWEB](https://github.com/baudzhou/WYWEB)
- [Daizhige](https://github.com/garychowcmu/daizhigev20)
- [ACLUE](https://github.com/isen-zhang/ACLUE)
- [Websites-A Related to Ancient Poetry](http://ts300.5156edu.com/)
- [Websites-B Related to Ancient Poetry](https://www.gushixuexi.com/)
- [Sou Yun](https://www.sou-yun.cn/)
- [THU-FSPC](https://github.com/THUNLP-AIPoet/Datasets)
- [Han Dian](https://www.zdic.net/)

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

The work is licensed under a [MIT License](https://lbesson.mit-license.org/).

![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)

The WenMind benchmark is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
