"""Base Plex client functionality."""
import requests

def get_plex_response(url: str, token: str) -> requests.Response:
    """calls a plex server with a given token and prints the response.
    
    Args:
        url: The URL to call, including everything except the token
        token: The Plex authentication token
        
    Returns:
        Response object from the Plex API
        
    Raises:
        SystemExit: If the connection times out or returns an HTTP error
    
    """
    try:
        r = requests.get(f"{url}{token.strip()}", timeout=10)
        r.raise_for_status()
    except requests.exceptions.Timeout as err:
        print("\n ERROR - connection timed out.\n")
        raise SystemExit(err) from err
    except requests.exceptions.HTTPError as err:
        print(f"\n ERROR - please check token \'{token}\' is correct.\n")
        raise SystemExit(err) from err

    return r
