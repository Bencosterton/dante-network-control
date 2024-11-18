#!/usr/bin/env python3

import signal
import sys
from netaudio.utils.logging_config import configure_logging

def handler(signum, frame):
    sys.exit(main())

if __name__ == "__main__":
    from netaudio.console.application import main

    # Configure logging before starting the application
    configure_logging()
    
    signal.signal(signal.SIGINT, handler)

    sys.exit(main())
