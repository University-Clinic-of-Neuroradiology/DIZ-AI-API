# DIZ AI API

This repo provides a simple Python script and a config.json file (for VS Code Extension Continue) to interact with the DIZ Llama API. The script sends a prompt to the API and returns the response.

## Prerequisites

- Python 3.x
- `requests` library
- `python-dotenv` library

You can install the required libraries using pip:

```bash
pip install requests python-dotenv
```

## Setup
1. Clone the repository or download the `DIZ_llama_api.py` file.
2. Create a `.env` file in the root directory and add the following variables:
```bash
DIZ_API_KEY=sk-XXX...XXX
```
Replace `sk-XXX...XXX` with your actual API key.

## Configuration
The API endpoint and headers are defined in the script:
```python
url = "https://ki-plattform.diz-ag.med.ovgu.de/api/chat/completions"
headers = {
    "Authorization": f"Bearer {DIZ_API_KEY}",
    "Content-Type": "application/json"
}
```

## How to use DIZ deepseek-coder in VS Code
1. Install [Continue](https://github.com/continuedev/continue) in VS Code.
2. Open Continue Config.
3. Change the `config.json` (use the [config.json](/config/config.json) template).
4. Replace `sk-XXX...XXX` with your actual API key.

## License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.