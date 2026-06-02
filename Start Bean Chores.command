#!/bin/bash
# Double-click this file to start Bean's Chore Quest on your home network.
# Keep the window that opens running while the family uses the app.
cd "$(dirname "$0")"
PORT=8080
NAME="$(scutil --get LocalHostName 2>/dev/null).local"
IP="$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null)"
echo "================================================="
echo "   Bean's Chore Quest  -  home network server"
echo "================================================="
echo ""
echo "  On THIS Mac:        http://localhost:$PORT"
echo ""
echo "  On Bean's iPad / phones (same Wi-Fi):"
echo "      http://$NAME:$PORT"
[ -n "$IP" ] && echo "      http://$IP:$PORT     <- use this if the name doesn't work"
echo ""
echo "  On each device: open that link in Safari, then"
echo "  Share -> Add to Home Screen."
echo ""
echo "  Keep this window OPEN. Press Ctrl+C to stop the server."
echo "================================================="
echo ""
python3 server.py $PORT
