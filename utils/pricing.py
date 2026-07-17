MODEL_PRICING = {

    "gpt-5.5": {
        "input": 1.25,
        "output": 10.00,
    },

    "gpt-5.5-mini": {
        "input": 0.25,
        "output": 2.00,
    },

    "gpt-5.5-nano": {
        "input": 0.05,
        "output": 0.40,
    },

    "gemini-3.5-flash": {
        "input": 0.0,
        "output": 0.0,
    },

    "qwen/qwen3.6-27b": {
        "input": 0.0,
        "output": 0.0,
    },
}


def estimate_cost(
    model,
    input_tokens,
    output_tokens,
):

    if model not in MODEL_PRICING:
        return 0

    p = MODEL_PRICING[model]

    return (
        input_tokens * p["input"] +
        output_tokens * p["output"]
    ) / 1_000_000


