from typing import Any, Callable, TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])

def xframe_options_deny(view_func: _F) -> _F: ...
def xframe_options_sameorigin(view_func: _F) -> _F: ...
def xframe_options_exempt(view_func: _F) -> _F: ...
