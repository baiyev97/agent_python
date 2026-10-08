# 1.1.1 小实战：agent_python_start

把 Prompt 文件与工单数据组装成标准 `messages` 请求体。
不联网、不调用模型；1.6.1 会把这份请求体原样交给真实模型。

## 目录

```text
agent_python_start/
├── app.py            主程序
├── prompts/
│   └── system.txt    角色与规则
├── data/
│   └── questions.jsonl  工单数据
├── .gitignore
└── README.md
```

## 运行

```powershell
python app.py
```

预期：为每条工单打印一份含 model / messages / temperature 的 JSON 请求体。
