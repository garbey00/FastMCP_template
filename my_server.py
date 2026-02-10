import asyncio
from fastmcp import FastMCP
from mcp.types import CallToolResult, TextContent
import os

mcp = FastMCP("My MCP Server", stateless_http=True)

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
        content=[TextContent(type="text", text="Hello from FastMCP!")],
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
    await mcp.run_async(transport="http", stateless_http=True)

if __name__ == "__main__":
    asyncio.run(main())

    
