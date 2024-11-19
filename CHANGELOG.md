## 0.0.2 (2024-11-18)
### Ben Costerton Update

- Added the device handling for 'subscription list' back in
- Removed a fair bit of mDNS output to clean up terminal
- Removed the connection status appended to the end of all subscription messages
- Added logging_config.py to __main__ to reduce the amount of cli output from netaudio
- Cleaned up the SIGPIPE error so it runs smoother on Windows systems out the box
