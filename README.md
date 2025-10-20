<img width="822" height="507" alt="Structure" src="https://github.com/user-attachments/assets/059ea6d7-d19a-47ff-94fe-22ad9fa68c79" />
🧠 PromptLearn: AI-Based Interactive Teaching using PEARL

PromptLearn is an interactive AI teaching assistant that guides learners through the PEARL learning stages —
Problem Identification, Exploration, Application, Reflection, and Learning Outcome.

It is built using Gradio, Hugging Face Inference API, and Meta-Llama 3.1-8B, providing a hands-on platform for prompt engineering pedagogy and AI-assisted learning.



⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/yourusername/PromptLearn.git
cd PromptLearn/prompt_teacher/src

2️⃣ Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate        # For Linux/macOS
venv\Scripts\activate           # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


Your requirements.txt should include:

gradio
python-dotenv
huggingface-hub
pydantic
pyyaml
sentence-transformers

4️⃣ Set Up Hugging Face API Key

Create a file named .env inside the /src directory:

HUGGINGFACE_API_KEY=hf_your_token_here


🟢 Tip: If you exceed free monthly credits on Hugging Face,
you can:

Create a new Hugging Face account for fresh credits, or

Switch to the free model (mistralai/Mistral-7B-Instruct-v0.3) inside app.py.

5️⃣ Run the Application
python -m prompt_teacher.app


If everything is set up correctly, you’ll see:

✅ Using Hugging Face model: meta-llama/Llama-3.1-8B
✅ Loaded 5 metaprompts.
* Running on local URL:  http://127.0.0.1:7860


Open that URL in your browser to start PromptLearn 🚀

💡 How It Works
PEARL Stage	Description	Example Prompt
🧩 Problem Identification	Helps the learner form a clear, meaningful question.	“Explain Newton’s First Law.” → “State Newton’s First Law with one real-world example.”
🔍 Exploration	Encourages deep understanding with analogies or examples.	“Explain using a car example.”
🧪 Application	Applies knowledge through problem-solving or code.	“Write Python code to simulate motion using Newton’s First Law.”
💭 Reflection	Encourages critical review of understanding.	“Compare two different ways of explaining Newton’s First Law.”
🎯 Learning Outcome	Summarizes insights and sets the next learning goal.	“I learned how Newton’s Law relates to real-world motion.”
🧩 Core Files Explanation
app.py

Contains main Gradio interface and PEARL stage processing functions.

Communicates with Hugging Face via InferenceClient.

Automatically cleans model output (removes “processed prompt” noise).

metaprompts.yml

Defines each PEARL stage template and description:

- name: "Problem Identification"
  explanation: "Helps form a clear and focused question."
  example_prompt: "Explain gradient descent."
  example_prompt_explanation: "This can be refined for clarity and context."
  template: |
    Reframe this question to make it clear and precise:
    {prompt}

callbacks.py

Manages UI interactivity (button visibility, responses).

Provides feedback message after each stage is selected.

🔄 Model Fallback Logic

If the Meta-Llama-3.1-8B model fails (due to quota or access),
the app automatically falls back to the Mistral 7B open model.

GATED_MODEL = "meta-llama/Llama-3.1-8B"
DEFAULT_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"


✅ Mistral runs without API limits, perfect for testing and classroom demos.

🔒 Environment File Example
HUGGINGFACE_API_KEY=hf_your_newtoken
DEFAULT_HF_MODEL=mistralai/Mistral-7B-Instruct-v0.3

🧠 Features Summary

✅ AI-powered PEARL learning guidance

✅ Works with Hugging Face Llama 3.1 or Mistral 7B

✅ Multi-stage interactive learning flow

✅ Automatic output cleaning & formatting

✅ Local Gradio-based UI

✅ Simple .env configuration for keys

✅ Extensible YAML-based stage definitions

📘 Example Workflow

Select a PEARL stage → Problem Identification

Enter:

What is Newton’s First Law?


Click Apply PEARL Stage → AI generates improved version

Click Explain Stage → AI explains the reasoning

Click Generate Learning Outcome → Short reflection summary

🧱 Future Extensions

📊 Add CSV-based logging of all user interactions

💬 Integrate voice input/output for accessibility

🧩 Add visualization of PEARL learning cycles

🧠 Support local inference with Ollama (offline Llama 3)

👨‍💻 Credits

Developed by Karunyaram
3rd Year B.Tech CSE, Kalasalingam University
Part of the ICTIEE–PEARL Research Paper Project

“PromptLearn: AI-Based Interactive Teaching using PEARL”
