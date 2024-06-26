# WenMind Benchmark

WenMind is a comprehensive benchmark dedicated for evaluating Large Language Models (LLMs) in Chinese Classical Literature and Language Arts (CCLLA). WenMind covers the sub-domains of **Ancient Prose**, **Ancient Poetry**, and **Ancient Literary Culture**, comprising 4,875 question-answer pairs, spanning 42 fine-grained tasks, 3 question formats, and 2 evaluation scenarios: domain-oriented and capability-oriented.

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

## TODO

We will soon release the code for model evaluation.

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

The work is licensed under a [MIT License](https://lbesson.mit-license.org/).

![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)

The WenMind benchmark is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
