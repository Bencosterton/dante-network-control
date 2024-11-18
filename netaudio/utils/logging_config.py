import logging
import sys

def configure_logging():
    # Suppress all logging output by default
    logging.getLogger().setLevel(logging.CRITICAL)
    
    # Configure specific loggers
    netaudio_logger = logging.getLogger("netaudio")
    netaudio_logger.setLevel(logging.INFO)
    
    # Completely silence zeroconf
    logging.getLogger("zeroconf").setLevel(logging.CRITICAL)
    logging.getLogger("zeroconf.asyncio").setLevel(logging.CRITICAL)
    
    # This is the filtering of messages in terminal output
    class MessageFilter(logging.Filter):
        def filter(self, record):
            # List of messages I don't like.
            unwanted_messages = [
                "timed out getting mDNS service",
                "Failed to get a service by type",
                "Failed to get Dante device name",
                "Failed to get Dante channel counts"
            ]
            return not any(msg in record.msg for msg in unwanted_messages)
    
    # Configure handlers
    handler = logging.StreamHandler(sys.stdout)  # Use stdout instead of stderr
    handler.setLevel(logging.INFO)
    handler.addFilter(MessageFilter())
    formatter = logging.Formatter('%(message)s')  # Simple format, just the message
    handler.setFormatter(formatter)
    
    # Remove any existing handlers
    netaudio_logger.handlers = []
    netaudio_logger.addHandler(handler)
    
    # Prevent log propagation to avoid duplicate messages
    netaudio_logger.propagate = False
