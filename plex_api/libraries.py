"""Plex api library functionality."""
import xml.etree.ElementTree as ET
from .client import get_plex_response

def get_librarySectionID(token: str, lib_type: str = "movie") -> str:
    """Return section key for a requested library.
    
        Args:
        token: The Plex authentication token
        lib_type: The type of library to look for (defaults to 'movie')
        
    Returns:
        The library section ID as a string
    """
    list_res = get_plex_response("http://localhost:32400/library/sections?X-Plex-Token=", token)
    print("\nSuccess! Listing media libraries below.\n")

    root  = ET.fromstring(list_res.content)

    for child in root:
        if child.attrib["type"] == lib_type:
            return child.attrib["key"]

    return f"ERROR - No library found matching type {lib_type}"
