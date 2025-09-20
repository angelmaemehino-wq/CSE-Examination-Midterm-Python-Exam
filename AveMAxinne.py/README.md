# CSE-Examination

My Code Explanation

I created a Python program exam.py that simulates a *basic GPS tracker*.

How it works?
- The player starts at position *(0, 0)*.
- The program accepts movement commands:
  - *N / North* → move up (increase Y)
  - *S / South* → move down (decrease Y)
  - *E / East* → move right (increase X)
  - *W / West* → move left (decrease X)
- After each move, the program shows the *current position*.
- The user can type *STOP* to end the session.
- At the end:
  - The program shows the *final position*.
  - It also says if the player returned to the origin *(0, 0)* or not.