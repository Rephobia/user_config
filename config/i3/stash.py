#!/usr/bin/env python3

# We have two workspace types, major and minor. Minor workspace names end with _SUFFIX
_SUFFIX = ":s"

def _remove_sufix(text: str):
    if text.endswith(_SUFFIX):
        print(text[:len(_SUFFIX)])
        return text[:-len(_SUFFIX)]
    return text

# Checks if workspace name is minor
def is_minor(workspace: str) -> bool:
    return workspace.endswith(_SUFFIX)

# Construct major workspace name
def major(workspace: str) -> str:
    return _remove_sufix(workspace)

# Construct minor workspace name
def minor(workspace: str) -> str:
    return _remove_sufix(workspace) + _SUFFIX
  
    
