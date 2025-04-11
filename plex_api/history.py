"""Plex watch history functionality."""
from .client import get_plex_response

def get_watch_history(address: str, token: str, accountID: str, librarySectionID: str) -> str:
    """Return list of media watched by a given user in a library.
    
    Args:
        token: The Plex authentication token
        accountID: The account ID to get history for
        librarySectionID: The library section ID to get history from
        
    Returns:
        Response object containing watch history data
    """
    url = f"http://{address}:32400/status/sessions/history/all?accountId={accountID}&librarySectionID={librarySectionID}&X-Plex-Token="
    history_response = get_plex_response(url, token)
    
    return history_response
    gi
