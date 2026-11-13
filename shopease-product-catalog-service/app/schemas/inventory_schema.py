"""Pydantic schemas for the inventory APIs."""
from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator

from app.schemas.product_schema import MAX_STOCK


class StockChange(BaseModel):
    model_config = ConfigDict(extra="forbid")

    quantity: int
    remarks: str | None = None

    @field_validator("quantity")
    @classmethod
    def _quantity(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Quantity must be greater than 0")
        if v > MAX_STOCK:
            raise ValueError(f"Quantity must not exceed {MAX_STOCK}")
        return v

    @field_validator("remarks")
    @classmethod
    def _remarks(cls, v: str | None) -> str | None:
        if v is None:
            return None
        v = " ".join(v.split())
        if len(v) > 255:
            raise ValueError("Remarks must be at most 255 characters")
        return v or None


class TransactionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    transaction_type: str
    quantity: int
    previous_stock: int
    updated_stock: int
    remarks: str | None
    performed_by: int | None
    created_at: datetime


class StockResponse(BaseModel):
    product_id: int
    sku: str
    name: str
    stock_quantity: int
    low_stock_threshold: int
    is_low_stock: bool


class HistoryResponse(BaseModel):
    product_id: int
    items: list[TransactionResponse]
    total: int
    page: int
    page_size: int
    total_pages: int


class LowStockItem(BaseModel):
    product_id: int
    sku: str
    name: str
    category_id: int
    stock_quantity: int
    is_active: bool


class LowStockResponse(BaseModel):
    threshold: int
    total: int
    page: int
    page_size: int
    total_pages: int
    items: list[LowStockItem]


class MessageResponse(BaseModel):
    message: str


class ErrorResponse(BaseModel):
    status_code: int
    error: str
    message: str
    details: list[dict] | None = None
