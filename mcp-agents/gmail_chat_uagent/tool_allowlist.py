"""Gmail MCP tool name allowlist (shared by chat protocol and tests)."""

from __future__ import annotations

ALLOWED_GMAIL_TOOLS = frozenset(
    {
        "setup_oauth",
        "complete_oauth",
        "check_auth_status",
        "reset_oauth_tokens",
        "send_email",
        "list_emails",
        "read_email",
        "delete_email",
        "delete_last_sent_email",
        "get_profile",
    }
)


def normalize_tool_name(name: str) -> str:
    return name.split(".")[-1].strip()


def validate_gmail_tool_name(fn_name: str) -> str:
    normalized = normalize_tool_name(fn_name)
    if normalized not in ALLOWED_GMAIL_TOOLS:
        raise ValueError(f"Gmail tool not allowed: {fn_name!r}")
    return normalized
