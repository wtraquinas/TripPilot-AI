from pydantic import BaseModel


class Usage(BaseModel):

    input_tokens: int = 0

    output_tokens: int = 0

    total_tokens: int = 0

    estimated_cost: float = 0.0