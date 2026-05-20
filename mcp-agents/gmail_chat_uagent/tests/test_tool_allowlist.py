"""Tests for Gmail MCP tool allowlist."""

import pytest

from tool_allowlist import ALLOWED_GMAIL_TOOLS, normalize_tool_name, validate_gmail_tool_name


def test_allowed_tools_registered():
    assert "send_email" in ALLOWED_GMAIL_TOOLS
    assert "list_emails" in ALLOWED_GMAIL_TOOLS


def test_normalize_strips_prefix():
    assert normalize_tool_name("gmail_tools.send_email") == "send_email"


def test_validate_accepts_known_tool():
    assert validate_gmail_tool_name("list_emails") == "list_emails"


def test_validate_rejects_unknown_tool():
    with pytest.raises(ValueError, match="not allowed"):
        validate_gmail_tool_name("__import__")


def test_validate_rejects_os_system_gadget():
    with pytest.raises(ValueError, match="not allowed"):
        validate_gmail_tool_name("os.system")
