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

## Data Construction

The construction pipeline of WenMind includes data collection and data processing, as illustrated in Figure 2.

<p align="center">
    <img src="https://github.com/SCUT-DLVCLab/WenMind/blob/main/Images/.png" width="800"/>
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
