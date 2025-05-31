from pydantic import BaseModel, Field, field_validator
from typing import Literal

class BlackScholesInput(BaseModel):
    S: float = Field(..., gt=0, description="Spot price of the underlying asset")
    K: float = Field(..., gt=0, description="Strike price")
    T: float = Field(..., gt=0, description="Time to maturity in years")
    sigma: float = Field(..., gt=0, description="Volatility of the underlying asset")
    option_type: Literal['call', 'put']

    @field_validator('option_type')
    def validate_option_type(cls, v):
        return v.lower()
