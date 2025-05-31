def get_prompt(task_type, input_text):
    if task_type == 'storytelling':
        return f"Continue the story coherently:\n\"{input_text}\""
    elif task_type == 'procedural':
        return f"Restate the instructions clearly:\n\"{input_text}\""
    elif task_type == 'factual':
        return f"Restate the following fact as clearly and accurately as possible:\n\"{input_text}\""

def backcheck_prompt(original, final):
    return f"Original: {original}\nFinal: {final}\nDoes the final response match the original fact?"
