# WenMind Benchmark

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

## Data Construction

The construction pipeline of WenMind includes data collection and data processing, as illustrated in Figure 2.

<p align="center">
    <img src="https://github.com/SCUT-DLVCLab/WenMind/blob/main/Images/Data_Construction.png" width="550"/>
<p>

<p align="center">
    <strong>Figure 2: Construction pipeline of WenMind Benchmark.</strong>
<p>

## TODO

We will soon release the code for model evaluation.
We are about to complete the README content.

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

The work is licensed under a [MIT License](https://lbesson.mit-license.org/).

![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)

The WenMind benchmark is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
