from whispernet.agents import run_agent_chain
from whispernet.metrics import compute_semantic_similarity



def run_experiment(dataset, task_type, correction=None, model_name=None):
    results = []
    for example in dataset:
        chain = run_agent_chain(example, task_type, voting=(correction=='voting'), backcheck=(correction=='backcheck'), model_name=model_name)
        sim = compute_semantic_similarity(chain[0], chain[-1], model_name=model_name)
        results.append({
            "chain": chain,
            "semantic_similarity": sim
        })
    return results
