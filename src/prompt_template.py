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
KNOWLEDGE_QA_TEMPLATE = KNOWLEDGE_QA_TEMPLATE = """
### Step 1: Background Knowledge
I will now provide you with some background knowledge from my perspective. This information may or may not be directly related to the question. However, please consider it thoughtfully, as it might help inform your reasoning.

[START KNOWLEDGE]
{knowledge}
[END KNOWLEDGE]

### Step 2: Question
Now, based on the question below, provide your answer. Feel free to incorporate relevant ideas or reasoning from the background knowledge if it helps you form a better answer.

Question: {question}

### Answer Format (strictly required):
Your answer **must** follow this exact format:

Choice: <A/B/C/D>, Explanation: <your explanation here>

### Format Example:
Choice: B, Explanation: Because it allows astronomers to analyze a wide range of wavelengths, which helps identify various physical processes in the observed system.

### Now Your Answer:
"""