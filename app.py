"""1.1.1 小实战：组装模型请求体。

把 Prompt 文件与工单数据组装成
标准的 messages 请求体并打印。
运行：python app.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent


def load_system_prompt(path):
    # 读取角色与规则文本
    return path.read_text(
        encoding="utf-8"
    ).strip()


def load_questions(path):
    # 每行一个 JSON 对象
    items = []
    text = path.read_text(encoding="utf-8")
    for number, line in enumerate(
        text.splitlines(), start=1
    ):
        if not line.strip():
            continue
        item = json.loads(line)
        if not item.get("question"):
            print(f"第 {number} 行缺 question，跳过")
            continue
        items.append(item)
        question = item.get("question", "")
        if not question.strip():
            print(f"第 {number} 行 question 为空，跳过")
            continue
    return items


def build_messages(system_prompt, question):
    return [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": question,
        },
    ]


def main():
    system_prompt = load_system_prompt(
        ROOT / "prompts" / "system.txt"
    )
    questions = load_questions(
        ROOT / "data" / "questions.jsonl"
    )

    for item in questions:
        messages = build_messages(
            system_prompt, item["question"]
        )
        request_body = {
            "model": "your-model-name",
            "messages": messages,
            "temperature": 0.2,
            "max_tokens": 512,
            "stream": False,
        }
        print(f"=== 工单 {item['case_id']} ===")
        print(json.dumps(
            request_body,
            ensure_ascii=False,
            indent=2,
        ))


if __name__ == "__main__":
    main()