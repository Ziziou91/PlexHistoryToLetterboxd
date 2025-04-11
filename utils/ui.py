"""UI-related utility functions."""

def print_title(title: str, line_length: int = 70) -> None:
    """Prints the title of the application."""
    title_spacing = int((line_length / 2) - (len(title) / 2))

    print(f"{'=' * line_length}")
    print(f"{'-' * title_spacing}{title}{'-' * title_spacing}")
    print(f"{'=' * line_length}")

def print_local_or_remote() -> None:
  """Prints instructions for local or remote access to Plex server."""
  instructions = """Is your Plex server on a local network or remote?

1. Local network (same home/office as you)
2. Remote (accessing from outside your home/office)
"""
  print(instructions)

def print_address_instructions() -> None:
  """Prints instructions for finding the Plex servers ip address."""
  instructions ="""
PLEX SEVER ADDRESS INSTRUCTIONS:
-----------------------
To find your Plex server's IP address, you can use the following methods:

======= External/Remote Access Instructions =======
1. Log into your Plex account at `https://app.plex.tv/desktop/`
2. Click on Settings (wrench icon) in the top-right corner
3. In the left sidebar, select "Remote Access"
4. Check if "Remote Access" is enabled
5. If enabled, look for "Public IP address" listed on this page
   - This is your external IP that can be used outside your local network
6. Note the port number listed (default is 32400)
7. Your remote Plex URL will be: `http://YOUR_PUBLIC_IP:PORT_NUMBER`

======= Troubleshooting =======
- If remote access shows as "Not available outside your network", you need to:
  1. Configure port forwarding on your router (port 32400)
  2. Check firewall settings to allow Plex traffic
  3. Ensure your ISP isn't blocking the required ports

- For secure remote access, consider using Plex's relay service or setting up a VPN
"""
  print(instructions)

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
