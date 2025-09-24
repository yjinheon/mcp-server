from importlib import import_module

# loader

DEFAULT_TOOLS = [
    "app.mcp.tools.hello",
    "app.mcp.tools.send_callback",
]


def load_tools(mcp, modules=DEFAULT_TOOLS):
    for mod in modules:
        m = import_module(mod)
        # each moduel offers 'resister'  function
        if hasattr(m, "register"):
            m.register(mcp)
