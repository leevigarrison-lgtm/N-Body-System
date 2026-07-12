# N-Body System

A simulation of gravitational interactions between multiple bodies in space.

**WARNING:** This version was logged locally and is an approximate artifact due to file loss in globals.py
**DISCLAIMER:** All code is human-written. I used AI to help me find and track bugs, but never to modify or re-write existing code. I required myself to understand every part of every issue I encountered, and fix it myself with the help of AI as a helping hand.

**PLEASE NOTE:** I didn't upload anything to Github until 6/29/26. Many of the changes were made previously towards the start of June or late May. 
------

# Getting Started:

## Prerequisites:

- I used Python 3.10.11
- Numpy and Copy imports required

# Running the Sim

- Copy the repository at any version
- Run render.py via 'python render.py' in the terminal.
- Note V0 and V1 don't work since they don't have a complete render.py.

## Version History

### V0 - Initial Commit

**Files:** 
'integrate.py',
'globals.py', 
'object.py', 
'render.py'

**Overview:**

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

### V2 - Basic Rendering & Non-Functional UI Implementation

**Files:** 

'integrate.py',
'globals.py', 
'object.py', 
'render.py', 
'compute_acceleration.py', 
'compute_energy.py', 
'screen_manager.py', 
'simulate.py', 
'ui_manager.py'

**Overview:**

- Adds basic rendering to a simple orbital system (earth-sun rotation)
- Splits up the acceleration and energy methods into seperate scripts for less complexity in the integrate.py script.
- Globals doesn't change. This is probably because globals was made formal in this version, but I overroad the V0 globals with this one.
- Added screen_manager.py script. Truncates massive orbital mechanics values into pixels for visual representation via several methods.
- Added ui_manager.py script. Not to be confused with screen_manager, UI manager manages all of the UI (text, labels, ect)
- Added simulate script that generalizes the process from numerical integrator -> on-screen pixels.

**File Structure:**

'integrate.py'
    - Exclusively handles numerical integration of motion using various methods.

'globals.py'
    - Sets values that should hold globally. 
    - Suspends the values into memory for dynamical changes during render.
    - Split up into two seperate classes for now (changables and globals, changables is supposted to be the only class that changes during the simulation and can be modified)
    - Sun and Earth are defined here for testing sake. 

'object.py'
    - Creates a basic body() class that everything else depends on. Class renamed from Body() to body().

'compute_acceleration.py'
    - Calculates acceleration using a brute-force calculation (O(n^2) time complexity)
    - Moved in a seperate script from integrate.py for simplicity.

'compute_energy.py'
    - Calculates error ratio of methods using first law of thermodynamics
    - Uses formula (energy_initial - energy_now)/energy_initial to calculate total energy loss over time.
    - Not used currently.

'screen_manager.py'
    - Not to be confused with ui_manager.py
    - Contains a class that converts massive orbital mechanics values into readable pixel-values.
    - Claude AI helped me significantly here, but I tried my best to construct the code on my own.

'ui_manager.py'
    - The basis for the UI in the future.
    - Creates a basic text button using pygame_gui

'simulate.py'
    - Contains a method that calls the numerical integrator of choice (defined in globals) and returns the integrated bodies.

'render.py'
    - Using pygame to construct the basic simulation.
    - Splits up rendering into a couple different scripts (screen_manager.py, ui_manager.py, simulate.py, and this one that combines them all)

### V3 - Functional UI Implementation

**Files:** 

'integrate.py',
'globals.py', 
'object.py', 
'render.py', 
'compute_acceleration.py', 
'compute_energy.py', 
'screen_manager.py', 
'simulate.py', 
'ui_manager.py'

**Overview:**

- Adds basic-level UI implementation beyond the simple "pause button" showcase in the previous version.
- The UI that works and has proper functionality up to this point is: Pause Button, Dimension Text Box, G-Constant Text Box, Delta Time Text Box, Menu % Text Box, and the FPS Text Box.
- Works by detecting button click or when text is done entering, then changing globals.py's global's class suspended into memory's information.
- Made global features a local-based item. Instead of defining classes globally, you call it inside the function in order to account for dynamical global information.

**File Structure:**

'integrate.py'
    - Exclusively handles numerical integration of motion using various methods.

'globals.py'
    - Sets values that should hold globally. 
    - Suspends the values into memory for dynamical changes during render.
    - Split up into two seperate classes for now (changables and globals, changables is supposted to be the only class that changes during the simulation and can be modified)
    - Sun and Earth are defined here for testing sake. 

'object.py'
    - Creates a basic body() class that everything else depends on. Class renamed from Body() to body().

'compute_acceleration.py'
    - Calculates acceleration using a brute-force calculation (O(n^2) time complexity)
    - Moved in a seperate script from integrate.py for simplicity.

'compute_energy.py'
    - Calculates error ratio of methods using first law of thermodynamics
    - Uses formula (energy_initial - energy_now)/energy_initial to calculate total energy loss over time.
    - Not used currently. (Non-Functional at it's current state)

'screen_manager.py'
    - Not to be confused with ui_manager.py
    - Contains a class that converts massive orbital mechanics values into readable pixel-values.
    - Claude AI helped me significantly here, but I tried my best to construct the code on my own.

'ui_manager.py'
    - The basis for the UI in the future.
    - Creates a basic text button using pygame_gui

'simulate.py'
    - Contains a method that calls the numerical integrator of choice (defined in globals) and returns the integrated bodies.

'render.py'
    - Using pygame to construct the basic simulation.
    - Splits up rendering into a couple different scripts (screen_manager.py, ui_manager.py, simulate.py, and this one that combines them all)

## Author
Leevi Garrison - github.com/leevigarrison-lgtm
