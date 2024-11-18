import logging
import sys

def configure_logging():
    # Suppress all logging output by default
    logging.getLogger().setLevel(logging.CRITICAL)
    
    # Configure specific loggers
    netaudio_logger = logging.getLogger("netaudio")
    netaudio_logger.setLevel(logging.INFO)
    
    # zeroconf displays an unholy amount of mDNS errors, despite it working, so I shall mute logging here.
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
    
    # reduce output mesaaging
    handler = logging.StreamHandler(sys.stdout) 
    handler.setLevel(logging.INFO)
    handler.addFilter(MessageFilter())
    formatter = logging.Formatter('%(message)s')  
    handler.setFormatter(formatter)
    
    # I personally don't think this is useful to end-user, it's gone
    netaudio_logger.handlers = []
    netaudio_logger.addHandler(handler)
    
    # Prevent log propagation to avoid duplicate messages
    netaudio_logger.propagate = False
