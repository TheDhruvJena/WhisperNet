# Configuration for model and experiments
NUM_HOPS = 5
TASK_TYPES = ['storytelling', 'procedural', 'factual']
RANDOM_SEEDS = [42, 43, 44, 45, 46]
model = [ "openai/gpt-3.5-turbo", "openai/gpt-4", "openai/gpt-4o", "huggingface/meta-llama/Llama-2-7b-chat-hf", "huggingface/tiiuae/falcon-7b-instruct", "lambda/lambda-llama2-13b", "groq/llama3-70b", "gemini/gemini-pro", "mistral/mistral-small", "mistral/mistral-medium" ]
platform, MODELS = model.split("/", 1) if "/" in model else ("huggingface", model)