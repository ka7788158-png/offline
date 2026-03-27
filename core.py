from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

class OfflineCodingAssistant:
    def __init__(self):
        print("🤖 Initializing Offline Coder...")
        print("⏳ Loading model into memory (this may take a minute depending on your hardware)...")
        
        # Using a small, highly capable coding model from Hugging Face
        model_id = "deepseek-ai/deepseek-coder-1.3b-instruct"

        self.llm = HuggingFacePipeline.from_model_id(
            model_id = model_id,
            task="text-generation",
            device = 0,
            pipeline_kwargs={
                "max_new_tokens": 512,  # How much code it can write at once
                "temperature": 0.1,     # Low temperature = highly logical, less hallucination
                "do_sample": True
            }

        )

        # # Create a Prompt Template instructing the AI exactly how to behave
        template = """You are an expert, offline Python coding assistant. 
Provide clean, bug-free, and well-commented code to solve the user's problem.
Do not provide unnecessary explanations, just the code and a brief summary.

User Question: {question}

Assistant Answer:"""

        self.prompt = PromptTemplate.from_template(template)

        # Connect the prompt and the local LLM into a sequence (Runnable)
        self.chain = self.prompt | self.llm
        print("✅ Model loaded and ready!")

    def ask_code_question(self, user_query):
        """Passes the user's query through the prompt template and into the local model."""
        try:
            # invoke() passes the query into the {question} placeholder in our template
            response = self.chain.invoke({"question": user_query})
            
            # Hugging Face pipelines sometimes return the prompt mixed with the answer.
            # This cleanly splits the output so you only see the AI's actual answer.
            clean_response = response.split("Assistant Answer:")[-1].strip()
            return clean_response
            
        except Exception as e:
            return f"An error occurred: {str(e)}"

# --- Terminal Testing Loop ---
if __name__ == "__main__":
    # Instantiate our OOP backend
    coder = OfflineCodingAssistant()
    
    print("\n" + "="*50)
    print("🔒 OFFLINE CODING ASSISTANT SECURE TERMINAL")
    print("Type 'exit' to quit.")
    print("="*50 + "\n")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'exit':
            print("Shutting down local instance...")
            break
            
        print("🧠 Thinking (running locally)...")
        reply = coder.ask_code_question(user_input)
        print(f"\n💻 Code Output:\n{reply}\n")
        print("-" * 50)