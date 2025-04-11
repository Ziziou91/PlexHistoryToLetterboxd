#!/usr/bin/env python3
"""
Plex to Letterboxd - Export your Plex watch history as Letterboxd csv format.
"""
import xml.etree.ElementTree as ET
import sys
from utils.ui import print_title, print_token_instructions
from plex_api.libraries import get_librarySectionID
from plex_api.history import get_watch_history

def main() -> None:
    """Main function where app logic is run."""
    sys.stdout.reconfigure(encoding='utf-8')

    print_title("Plex to Letterboxd")
    print_token_instructions()

    token = input("\nPlease enter your plex token: ")

    librarySectionID = get_librarySectionID(token)

    # TODO - Get list of users - accountId
    # https://plex.tv/api/users?X-Plex-Token=

    watch_history_response  = get_watch_history(token, 1, librarySectionID)

    root  = ET.fromstring(watch_history_response.content)

    for child in root:
        print(child.tag, child.attrib)

    # TODO: Add export to Letterboxd functionality


# ===================EXECTUION STARTS HERE===================
if __name__ == "__main__":
    main()
