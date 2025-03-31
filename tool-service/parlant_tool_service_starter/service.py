import asyncio
from enum import Enum
import json

from parlant.sdk import (
    PluginServer,
    ToolContext,
    ToolResult,
    tool,
)

with open("products.json", 'r') as file:
    database = json.load(file)

class ProductType(Enum):
    MONITOR = "Monitor"
    KEYBOARD = "Keyboard"
    MOUSE = "Mouse"
    HEADSET = "Headset"
    AUDIO = "Audio"
    LAPTOP = "Laptop"
    OTHER = "Other"

@tool
async def get_products_by_type(
    context: ToolContext,
    product_type: ProductType,
) -> ToolResult:
    """Get all products that match the specified product type"""
    products = [item for item in database if item['type'] == product_type.value]
    return ToolResult({"available_products": products})

TOOLS = [
    get_products_by_type
]

async def main() -> None:
    async with PluginServer(tools=TOOLS, port=8089):
        pass

if __name__ == "__main__":
    asyncio.run(main())