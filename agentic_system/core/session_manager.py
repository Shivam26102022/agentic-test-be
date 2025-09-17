
from agents.memory.session import SessionABC
from agents.items import TResponseInputItem
from typing import List

class MyCustomSession(SessionABC):
    """Custom session implementation following the Session protocol."""

    def __init__(self, session_id: str):
        self.session_id = session_id
        self.messages: List[TResponseInputItem] = []

    async def get_items(self, limit: int | None = None) -> List[TResponseInputItem]:
        """Retrieve conversation history for this session."""
        if limit is not None:
            return self.messages[-limit:]
        return self.messages

    async def add_items(self, items: List[TResponseInputItem]) -> None:
        """Store new items for this session."""
        self.messages.extend(items)

    async def pop_item(self) -> TResponseInputItem | None:
        """Remove and return the most recent item from this session."""
        if self.messages:
            return self.messages.pop()
        return None

    async def clear_session(self) -> None:
        """Clear all items for this session."""
        self.messages.clear()

from typing import List, Optional






class SimpleSession:
    """
    Simple in-memory session for storing conversation history as a list of messages.
    """
    def __init__(self, session_id: str, initial_messages: Optional[List[dict]] = None):
        self.session_id = session_id
        self.messages: List[dict] = initial_messages.copy() if initial_messages else []

    async def get_items(self, limit: Optional[int] = None, user_query: Optional[str] = None) -> List[dict]:
        """
        Retrieve conversation history for this session.
        """
        if limit is not None:
            return self.messages[-limit:]
        return self.messages

    async def add_items(self, items: List[dict]) -> None:
        """
        Store new items for this session.
        Each item should be a dict with 'role' and 'content'.
        """
        self.messages.extend(items)

    async def pop_item(self) -> Optional[dict]:
        """
        Remove and return the most recent item from this session.
        """
        if self.messages:
            return self.messages.pop()
        return None

    async def clear_session(self) -> None:
        """
        Clear all items for this session.
        """
        self.messages.clear()