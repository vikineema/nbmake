from typing import Optional

from nbformat import NotebookNode
from pydantic import BaseModel

class NotebookWarning(BaseModel):
    source: str
    summary: str
    warning_cell_index: int

class NotebookError(BaseModel):
    summary: str
    trace: str
    failing_cell_index: int


class NotebookResult(BaseModel):
    nb: NotebookNode
    error: Optional[NotebookError]
