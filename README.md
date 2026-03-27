# 🔒 Secure Offline Coding Assistant

A 100% offline, privacy-first AI coding assistant powered by local Large Language Models (LLMs) and GPU acceleration. 

This project allows you to ask coding questions, debug scripts, and generate proprietary code without ever sending your data to the internet or relying on paid API keys. The AI runs entirely on your local hardware using Hugging Face pipelines, LangChain, and a clean Streamlit user interface.

## 🚀 Features
* **Total Privacy:** No internet connection required after the initial model download. Your proprietary code never leaves your machine.
* **GPU Accelerated:** Optimized to utilize NVIDIA GPUs via PyTorch CUDA for lightning-fast inference.
* **Specialized Coding Model:** Uses `deepseek-ai/deepseek-coder-1.3b-instruct`, a highly capable and lightweight open-source coding model.
* **Interactive UI:** A sleek, responsive chat interface built with Streamlit, featuring built-in session state for memory and context.

## 🛠️ Tech Stack
* **Python 3.10+**
* **LangChain & LangChain-Core:** For prompt templating and connecting the LLM pipeline.
* **Hugging Face Transformers:** For loading and interacting with the local DeepSeek model.
* **PyTorch (CUDA 12.x/13.0+):** For offloading matrix calculations to the GPU.
* **Streamlit:** For the frontend web application.

## ⚙️ Prerequisites
To get the blazing-fast speeds this project offers, you need a machine with a dedicated **NVIDIA GPU** and up-to-date drivers.

## 📦 Installation

```bash
1. Clone the repository

git clone [https://github.com/yourusername/offline-coding-assistant.git](https://github.com/yourusername/offline-coding-assistant.git)
cd offline-coding-assistant

2. Create and activate a virtual environment

python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

3. Install PyTorch with CUDA Support
⚠️ Important: Do NOT use pip install torch (it installs CPU version)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

4. Install remaining dependencies
pip install streamlit transformers langchain-huggingface langchain-core

5. Run the application
streamlit run app.py
```

🎮 Usage
Note on the first run: You will need Wi-Fi ON the very first time you run the script so it can download the ~2.6GB model from Hugging Face. Once it says "Model loaded and ready!", you can turn off your Wi-Fi forever.

Run the Streamlit UI
To launch the interactive chat application:

```Bash
streamlit run offline_ui.py
This will open a local web server at http://localhost:8501.
```

If you prefer a pure hacker terminal experience, you can run the core engine directly:

```Bash
python offline_coder.py
```

📁 Project Structure
offline_coder.py: The core backend class that initializes the Hugging Face pipeline, forces it onto the GPU (device=0), and sets up the LangChain Prompt Templates.

offline_ui.py: The frontend Streamlit application that handles the chat interface, caches the heavy model into memory, and manages conversation history.

🤝 Acknowledgments
Built by Kavya Agrawal

Powered by open-source models from DeepSeek and the Hugging Face ecosystem.

Guided by LangChain framework concepts.
