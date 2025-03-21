# 直接做QA的模板
QA_TEMPLATE = """
Answer the following multiple-choice question by selecting only the correct option (A, B, C, or D). Do not provide an explanation.

{question_choice}

Format: Return only a single uppercase letter (A, B, C, or D).

Answer:
"""


# 为question生成explanation的模板
EXPLANATION_TEMPLATE = """
Identify and explain the key technical terms in the following question. Provide a concise definition for each term.

Question: {question}

Output format:
- **Term 1**: Definition
- **Term 2**: Definition
- **Term 3**: Definition
...
"""


# 加入知识后的模板
KNOWLEDGE_QA_TEMPLATE = """
### Step 1: Learning Phase
First, I will provide you with some background knowledge. Use this knowledge as a reference when answering, but feel free to apply reasoning and prior understanding where necessary.

[START KNOWLEDGE]
{knowledge}
[END KNOWLEDGE]

### Step 2: Question Phase
Now, based on the knowledge above, answer the following question:

Question: {question}

### Answer Guidelines:
1. Your answer should be **informed by the provided knowledge**, but you may also incorporate relevant reasoning.
2. If the question is multiple-choice, return only the correct option (A, B, C, or D).

Answer:
"""