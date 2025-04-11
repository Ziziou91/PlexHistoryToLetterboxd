"""UI-related utility functions."""

def print_title(title: str, line_length: int = 70) -> None:
    """Prints the title of the application."""
    title_spacing = int((line_length / 2) - (len(title) / 2))

    print(f"{'=' * line_length}")
    print(f"{'-' * title_spacing}{title}{'-' * title_spacing}")
    print(f"{'=' * line_length}")


def print_token_instructions() -> None:
    """Prints instructions for finding the Plex authentication token."""
    instructions = """
PLEX TOKEN INSTRUCTIONS:
-----------------------
To find your Plex token:

Method 1 - From the Plex Web App:
  1. Log in to Plex Web App (app.plex.tv)
  2. Open any media item and play it
  3. While it's playing, click the three dots (...) and select 'Get Info'
  4. In the URL of the info page, look for '&X-Plex-Token=' followed by your token

Method 2 - From browser cookies:
  1. Log in to Plex Web App
  2. Open browser developer tools (F12 or right-click > Inspect)
  3. Go to the 'Application' or 'Storage' tab
  4. Look for cookies and find 'X-Plex-Token'

Method 3 - From Plex Media Server XML:
  1. Log in to Plex Web App
  2. Go to: https://plex.tv/devices.xml
  3. Search for the 'token' attribute in the XML

Your token is a long alphanumeric string like 'xxxxxxxxxxxxxx'.
Keep this token private as it provides access to your Plex server.
"""
    print(instructions)
