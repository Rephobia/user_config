#!/usr/bin/env python3

# We have two workspace types, major and minor. Minor workspace names starts with _PREFIX
_PREFIX = "s:"

def _remove_prefix(text: str):
    if text.startswith(_PREFIX):
        return text[len(_PREFIX):]
    return text

# Checks if workspace name is minor
def is_minor(workspace: str) -> bool:
    return workspace.startswith(_PREFIX)

# Construct major workspace name
def major(workspace: str) -> str:
    return _remove_prefix(workspace)

# Construct minor workspace name
def minor(workspace: str) -> str:
    return _PREFIX + _remove_prefix(workspace)
  
    
