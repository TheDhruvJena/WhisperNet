import random
from .prompts import get_prompt, backcheck_prompt

def mock_llm_response(prompt):
    # Replace with OpenAI API or other LLMs in production
    return prompt.replace(":", "").split("\n")[-1] + " [modified]"

def run_agent_chain(initial_msg, task_type, num_hops=5, voting=False, backcheck=False):
    chain = [initial_msg]
    for hop in range(num_hops):
        prompt = get_prompt(task_type, chain[-1])
        if voting:
            outputs = [mock_llm_response(prompt + f" [seed {i}]") for i in range(3)]
            selected = majority_vote(outputs)
        else:
            selected = mock_llm_response(prompt)
        chain.append(selected)

    if backcheck:
        original = chain[0]
        final = chain[-1]
        is_consistent = "yes" in mock_llm_response(backcheck_prompt(original, final)).lower()
        if not is_consistent:
            chain[-1] = original + " [revised]"
    return chain

def majority_vote(outputs):
    from collections import Counter
    token_counts = [Counter(o.split()) for o in outputs]
    avg_scores = []
    for i, count in enumerate(token_counts):
        others = token_counts[:i] + token_counts[i+1:]
        overlap = sum(sum((count & other).values()) for other in others)
        avg_scores.append(overlap)
    return outputs[avg_scores.index(max(avg_scores))]
