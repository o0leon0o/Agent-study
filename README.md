# agent-study · 学习代码

> DeepSeek API 的学习练习。跟学习跟踪站（`server.mjs`）无关，这里是独立的一个仓库。
> 现在只有 `Stage_0/`：最基础的 API 调用（W0 环境三件套之后的第一次跑通）。

## 目录

```
.
├─ README.md          ← 本文件
├─ .venv/             ← 本地 Python 3.14 虚拟环境（已在 .gitignore，不会提交）
├─ .vscode/           ← 解释器指向 .venv，只对「以此目录为根打开的窗口」有效
└─ Stage_0/
   ├─ LLM_API.py      ← 纯 requests 版：手写 POST /chat/completions，打印 usage
   └─ LLM_API_sdk.py  ← openai SDK 版：同一条链路，换成客户端调用
```

## 怎么跑

```powershell
cd <本仓库目录>
.\.venv\Scripts\Activate.ps1          # 或 .\.venv\Scripts\python.exe 直接跑
$env:DEEPSEEK_API_KEY = "sk-..."      # 只放环境变量，不要写进任何文件
python .\Stage_0\LLM_API.py           # 输入 exit / quit 退出
python .\Stage_0\LLM_API_sdk.py
```

用 VS Code 时**以本仓库为根目录打开**，`.vscode/settings.json` 里的解释器路径才对得上。

## 依赖

已装在 `.venv`：`requests`、`openai`（连带 `httpx2`、`pydantic`、`truststore` 等）。
环境没了就重建：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install requests openai
```

## 已知问题（留着自己改，别当成范例）

- `Stage_0/LLM_API_sdk.py` 里 `basa_url=` 拼错了，应为 `base_url=`；不改它就必报 `TypeError`。
- 同文件顶部 `from email import message` / `from http import client` 是多余的导入，可以删。

## 纪律

- 新练习一个子目录：`Stage_1/`、`Stage_2/`……别把脚本丢在仓库根下。
- `.venv/`、`.env`、运行产物一律不进仓库；它们已经在 `.gitignore` 里。
- 产物（下载的数据、模型、截图）放仓库外的临时目录，不要提交。

## 远程仓库

<https://github.com/o0leon0o/Agent-study>（`main` 分支）

- 本机 remote 走 SSH：`git@github.com:o0leon0o/Agent-study.git`
- 换机器时重设：`git remote set-url origin <地址>`；HTTPS 地址同样可用，
  凭据交给 Git Credential Manager 弹窗登录。

```powershell
git push -u origin main
```
