import asyncio
import signal
import os
from bot import main

# Global flag to track if restart is needed
should_restart = False

def signal_handler(sig, frame):
    print("\nShutting down...")
    global should_restart
    if not should_restart:
        try:
            exit()
        except SystemExit:
            exit()
    else:
        should_restart = False

def restart_handler(sig, frame):
    print("\nRestarting bot...")
    global should_restart
    should_restart = True
    try:
        exit()
    except SystemExit:
        pass

if __name__ == "__main__":
    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGUSR1, restart_handler)  # Custom signal for restart
    
    while True:
        try:
            # Run the bot
            asyncio.run(main())
        except KeyboardInterrupt:
            print("\nBot stopped by user (Ctrl+C)")
            exit()
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            try:
                exit()
            except SystemExit:
                pass
        
        # Check if we should restart
        if should_restart:
            should_restart = False  # Reset the flag after restart
            continue
        else:
            exit() 