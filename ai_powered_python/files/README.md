# AI-Powered Python — Code Samples

**UTHM CodeVerse Webinar | Rynet Malaysia**

Every runnable code file from the workshop slides (including the Part 0 Python refresher), one file per script, named exactly as shown on each slide, grouped by part.

## Folder structure

```
ai-powered-python-code-samples/
├── part0_python_refresher/
│   ├── basics.py               <- variables, types, print(), f-strings
│   ├── operators.py
│   ├── lists.py
│   ├── dictionaries.py
│   ├── list_of_dicts.py        <- the pattern used by every AI call later
│   ├── functions.py
│   ├── control_flow.py
│   ├── dot_notation.py         <- foreshadows response.choices[0].message.content
│   └── imports_and_errors.py
├── part1_ai_assisted_coding/
│   ├── explain_demo.py
│   ├── generate_demo.py
│   ├── buggy.py
│   └── fixed.py
├── part2_rest_apis/
│   ├── get_request.py
│   └── post_request.py
├── part3_ai_api_integration/
│   ├── groq_client.py        <- other scripts in this folder import from here
│   ├── zero_shot.py
│   ├── system_role.py
│   ├── few_shot.py
│   ├── chain_of_thought.py
│   ├── handle_response.py
│   ├── via_groq.py
│   └── via_claude.py
├── part4_mini_project/
│   ├── prompt.py              <- isolated Step 1 snippet
│   └── study_assistant.py     <- the full, self-contained mini project
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup (VS Code)

1. **Open the folder.** Unzip this, then in VS Code: `File > Open Folder...` and select `ai-powered-python-code-samples`.

2. **Create a virtual environment** (Terminal > New Terminal, then):
   ```bash
   python -m venv .venv
   ```
   Activate it:
   - macOS/Linux: `source .venv/bin/activate`
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`

   VS Code will usually prompt "Select Interpreter" — pick the one inside `.venv`. If not, open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) → **Python: Select Interpreter** → choose `.venv`.

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key.** Copy `.env.example` to a new file named `.env` in this same root folder, then paste your real key in:
   ```
   GROQ_API_KEY=gsk_...your real key...
   ```
   Get a free key at [console.groq.com](https://console.groq.com) → API Keys.

   `python-dotenv`'s `load_dotenv()` automatically searches upward from wherever a script runs, so **one `.env` file at this root folder covers every script in every subfolder** — you don't need to duplicate it.

5. **Run any script** from the integrated terminal, e.g.:
   ```bash
   python part0_python_refresher/basics.py
   python part2_rest_apis/get_request.py
   python part3_ai_api_integration/zero_shot.py
   python part4_mini_project/study_assistant.py
   ```

   Everything in `part0_python_refresher/` runs standalone with no API key and no internet — safe to demo first, even before your `.env` is set up.

## Notes

- **`part0_python_refresher/`** needs nothing but Python itself (no API key, no internet). `dot_notation.py` defines two tiny made-up classes just so the "attribute → index → attribute" chaining example actually runs — the point is the *shape* of the code, since that same shape reappears as `response.choices[0].message.content` in Part 3.
- **`part3_ai_api_integration/groq_client.py`** defines the Groq `client` once. Every other script in that same folder does `from groq_client import client` — this only works because they're all in the same folder (Python looks for imports next to the script that's running). Don't move a technique script out of `part3_ai_api_integration/` on its own, or the import will fail.
- **`part4_mini_project/study_assistant.py`** is deliberately self-contained (it defines its own client and its own `build_prompt`) so it can be copied, shared, or submitted as a single file.
- **`via_claude.py`** needs the `anthropic` package (already in `requirements.txt`) and an `ANTHROPIC_API_KEY` in your `.env`. It's optional — skip it if you're only using Groq.
- **`buggy.py`** is intentionally broken (it's the "before" half of the debug demo) — running it will raise a `NameError` on purpose. `fixed.py` is the corrected version.

## Resources

- Practice API: [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)
- Groq console: [console.groq.com](https://console.groq.com)
- Anthropic docs: [docs.claude.com](https://docs.claude.com)
- Python Requests docs: [requests.readthedocs.io](https://requests.readthedocs.io)
- Rynet Malaysia: [rynet.com.my](https://rynet.com.my)
