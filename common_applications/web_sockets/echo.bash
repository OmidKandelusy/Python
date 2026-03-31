#!/bin/bash
# run_echo.sh - starts server and allows interactive client messages

# Start server in the background
echo "Starting server..."
python3 server.py &
SERVER_PID=$!
sleep 1  # wait for server to start

# Interactive prompt
echo "Server started. Type messages to send (Ctrl+C to exit):"

trap "echo 'Stopping server...'; kill $SERVER_PID; exit" SIGINT SIGTERM

while true; do
    read -p ">> " message
    if [[ -z "$message" ]]; then
        continue
    fi
    python3 client.py "$message"
done