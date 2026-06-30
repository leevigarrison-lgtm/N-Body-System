# N-Body System

A simulation of gravitational interactions between multiple bodies in space.

**WARNING:** This version was logged locally and is an approximate artifact due to file loss in globals.py
**DISCLAIMER:** All code is human-written. I used AI to help me find and track bugs, but never to modify or re-write existing code. I required myself to understand every part of every issue I encountered, and fix it myself with the help of AI as a helping hand.
------

# Getting Started:

## Prerequisites:

- I used Python 3.10.11
- Numpy and Copy imports required

# Running the Sim:

- N/A right now. Merely created and tested numerical methods.

## Version History

### V0 - Initial Commit
**Files:** 'integrate.py','globals.py', 'object.py', 'render.py'

- Numerical methods, object class, and globals established
- Basic mass definition along with three numerical methods: Euler, Improved Euler, and Velocity Verlet.
- Used the help of Claude AI to verify code correctness and functionality before continuing.

**File Structure:**

'integrate.py'
    - Handles numerical integration of motion using various methods.
    - Calculates error ratio of methods using first law of thermaldynamics
    - Calculates acceleration using a brute-force calculation (O(n^2) time complexity)

'globals.py'
    - Sets values that should hold globally. 
    - Suspends the values into memory for dynamical changes during render (useful later)

'object.py'
    - Creates a basic Body() class that everything else depends on
    - Claude AI suggested several changes during the construction of this class, many were taken.
'render.py'
    - A script that will eventually render the entire sim using pygame.
    - Nothing in here yet.

### V1 - README Addition

- Nothing new, but figured I should add a README.md. 
- This is my first time using Version Control, so I'm just trying to get used to it.

## Author
Leevi Garrison - github.com/leevigarrison-lgtm
