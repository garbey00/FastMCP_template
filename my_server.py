import asyncio
from fastmcp import FastMCP
from mcp.types import CallToolResult
import os

mcp = FastMCP("My MCP Server")

@mcp.tool(
    meta={
        "openai/outputTemplate": "ui://property_search.html",
        "openai/widgetAccessible": True,
        "openai/resultCanProduceWidget": True,
        "readOnlyHint": True,
    }
)
def property_search() -> CallToolResult:
    """Search for real estate properties based on user criteria."""
    return CallToolResult(
        _meta={
            "openai/toolInvocation/invoking": "Searching properties…",
            "openai/toolInvocation/invoked": "Properties found.",
        }
    )

@mcp.resource("ui://property_search.html", mime_type="text/html+skybridge")
def property_search_html():
    path = os.path.join("components", "property_search.html")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


async def main():
    await mcp.run_async()

if __name__ == "__main__":
    asyncio.run(main())

    
