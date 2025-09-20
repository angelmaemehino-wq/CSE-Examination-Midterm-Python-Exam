# gps_tracker.py
def gps_tracker():
    """
    Simple interactive GPS tracker.
    Starts at (0,0). Accepts N/S/E/W or full words (north, south, east, west),
    case-insensitive. Type STOP to finish the session.
    """
    x, y = 0, 0  # starting coordinates
    print("Starting position: (0, 0)")

    try:
        while True:
            raw = input("Enter direction (N/S/E/W) or STOP to end: ").strip()
            # normalize to lowercase for easy checking
            cmd = raw.lower()

            if cmd == "stop":
                break
            elif cmd in ("n", "north"):
                y += 1
            elif cmd in ("s", "south"):
                y -= 1
            elif cmd in ("e", "east"):
                x += 1
            elif cmd in ("w", "west"):
                x -= 1
            else:
                print("Invalid input. Please enter N, S, E, W, or STOP (full words ok).")
                continue

            print(f"Current position: ({x}, {y})")

    except KeyboardInterrupt:
        # If user presses Ctrl+C, gracefully finish the session
        print("\nSession interrupted by user — ending session.")

    # Session ended: show final position and whether returned to origin
    print(f"\nFinal position: ({x}, {y})")
    if (x, y) == (0, 0):
        print("You returned to the origin (0,0).")
    else:
        print("You did not return to the origin.")

if __name__ == "__main__":
    gps_tracker()