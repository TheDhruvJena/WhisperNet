from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

EMBEDDING_MODELS = {
    "openai/gpt-3.5-turbo": "all-MiniLM-L6-v2",
    "openai/gpt-4": "all-MiniLM-L6-v2",
    "openai/gpt-4o": "all-MiniLM-L6-v2",
    "huggingface/meta-llama/Llama-2-7b-chat-hf": "all-MiniLM-L6-v2",
    "huggingface/tiiuae/falcon-7b-instruct": "all-MiniLM-L6-v2",
    "lambda/lambda-llama2-13b": "all-MiniLM-L6-v2",
    "groq/llama3-70b": "all-MiniLM-L6-v2",
    "gemini/gemini-pro": "all-MiniLM-L6-v2",
    "mistral/mistral-small": "all-MiniLM-L6-v2",
    "mistral/mistral-medium": "all-MiniLM-L6-v2"
}

_loaded_models = {}

def get_embedding_model(model_name):
    if model_name not in _loaded_models:
        emb_model_name = EMBEDDING_MODELS.get(model_name, "all-MiniLM-L6-v2")
        _loaded_models[model_name] = SentenceTransformer(emb_model_name)
    return _loaded_models[model_name]

def compute_semantic_similarity(text1, text2, model_name=None):
    model = get_embedding_model(model_name)
    emb1 = model.encode([text1])
    emb2 = model.encode([text2])
    return cosine_similarity(emb1, emb2)[0][0]