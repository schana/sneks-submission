# Sneks

Sneks is a programming competition where you build the behavior for Sneks that compete against other players'
submissions. Write Python code to control your Snek's behavior, then upload it to see how it performs!

Build the behavior for your Snek and upload it at [sneks.dev/submit](https://www.sneks.dev/submit) to see how it does
against other submitters. See the website for [live results](https://www.sneks.dev) and details regarding scoring and
submission help.

## How the Game Works

### The Basics

Sneks is a snake-like game played on a grid of cells. Your Snek moves around the board collecting food to grow longer.
Each turn, your code decides which action your Snek takes next.

- **Food**: When your Snek's head moves onto a cell containing food, your Snek grows longer
- **Occupied cells**: If your Snek's head moves onto a cell occupied by another Snek or your own body, your Snek's run
  ends—it stops taking turns and remains static in its last position
- **Scoring**: Your score is based on how long you survive and how long your Snek grows. Scores are min-max normalized,
  meaning the best performer gets 100% and the worst gets 0%, with everyone else scaled in between.

### The Board

The game board is **toroidal** (wraps around). If your Snek moves off the right edge, it appears on the left. Same for
top/bottom.

### Vision

Your Snek has a limited **vision range**. You can only see occupied cells within a certain distance from your head.
Food, however, is always visible regardless of distance.

### Relative Coordinates

All positions your Snek receives are **relative to its head**. Your head is always at `Cell(0, 0)`. This means:

- Positive X is to the right of your head
- Positive Y is above your head
- Food and occupied cell positions are offsets from where you currently are

## Getting Started

### Prerequisites

1. Install Python >=3.10 from [python.org/downloads](https://www.python.org/downloads/)
    1. Add Python to your Path to make things easier
2. _(Optional)_ Install an IDE to work in
    1. [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download)
       (_Note_: scroll down for the free Community edition)
    2. [Visual Studio Code](https://code.visualstudio.com/)
3. Download `template.zip` to your local machine
   from [sneks.dev/template/template.zip](https://www.sneks.dev/template/template.zip) and extract its contents.

### Set up development environment

1. Open a terminal or command prompt
2. Change to the directory where the template is located. After unzipping, it should be the directory called
   `sneks-submission-main`.
    1. You should be located in the same directory as `pyproject.toml`
3. _(Optional, but recommended)_ Set up a virtual environment
    1. Create virtual environment
       ```
       python -m venv venv
       ```
    2. Activate the environment
        1. macOS / Linux
           ```
           source venv/bin/activate
           ```
        2. Windows
           ```
           venv\Scripts\activate
           ```
            1. If you get an error saying your execution policy prevents the running of the activate script, you can
               disable that policy temporarily with `Set-ExecutionPolicy Unrestricted -Scope Process`.
4. Install this package to enable testing locally
   ```
   pip install --editable .
   ```
5. Ensure everything works by trying out the CLI
    1. Test that the current Snek passes validation
       ```
       sneks validate
       ```
    2. Run the current Snek by itself
       ```
       sneks run
       ```

## Developing Your Snek

Edit `src/submission/submission.py` to implement your Snek's behavior. The key method is `get_next_action()`:

```python
from sneks.engine.core.action import Action
from sneks.engine.core.snek import Snek


class CustomSnek(Snek):
    def get_next_action(self) -> Action:
        # Your logic here
        return Action.UP  # Return one of: UP, DOWN, LEFT, RIGHT, MAINTAIN
```

See [sneks.dev/docs](https://www.sneks.dev/docs/index.html) for full documentation. There are also example Sneks in
`src/examples`
that can be used as starting points.

### Available Actions

- `Action.UP` - Move up
- `Action.DOWN` - Move down
- `Action.LEFT` - Move left
- `Action.RIGHT` - Move right
- `Action.MAINTAIN` - Continue in current direction

### Example Strategies

Check `src/examples/` for starter ideas:

- `chaotic.py` - Picks a random action each turn
- `circle.py` - Uses instance variables to track state and move in a pattern
- `looking_up.py` - Uses `look()` to detect obstacles and avoid them

### Useful Helper Methods

Your Snek class has several built-in methods to help you make decisions:

- `look(direction)` - Returns the distance to the nearest occupied cell in a direction (or the edge of your vision range
  if no obstacle is visible)
- `get_occupied()` - Returns all occupied cells your Snek can see
- `get_food()` - Returns all food cells on the board
- `get_closest_food()` - Returns the nearest food cell
- `get_direction_to_destination(cell)` - Returns the best direction to travel toward a cell
- `get_bearing()` - Returns your Snek's current velocity

Cells also have useful methods:

- `get_distance(other_cell)` - Returns the distance to another cell (accounts for board wrapping)
- `get_neighbor(direction)` - Returns the adjacent cell in a direction
- `get_up()`, `get_down()`, `get_left()`, `get_right()` - Returns the adjacent cell in that direction

Directions have a helpful method too:

- `get_action()` - Converts a Direction to the corresponding Action (useful with `get_direction_to_destination()`)

See [sneks.dev/docs](https://www.sneks.dev/docs/index.html) for full documentation.

## Testing Locally

```bash
# Validate your submission
sneks validate

# Run a single game
sneks run

# Run multiple games
sneks run --runs 10

# Run with multiple Sneks
sneks run --sneks-count 4

# Step through slowly
sneks run --step-delay 200
```

Run `sneks run --help` for full usage information.

| Option                 | Default | Description                      |
|------------------------|---------|----------------------------------|
| `--runs`               | 1       | Number of game runs to execute   |
| `--sneks-count`        | 1       | Number of Sneks to spawn         |
| `--step-delay`         | 40      | Delay in ms between steps        |
| `--step-keypress-wait` | False   | Wait for keypress between steps  |
| `--end-delay`          | 1000    | Delay in ms after run ends       |
| `--end-keypress-wait`  | False   | Wait for keypress after run ends |

## Rules

- Your submission must pass `sneks validate`
- Your `submission.py` must contain a `CustomSnek` class
- No external libraries allowed
- Submissions that take too long to compute a turn will not pass validation

## Tips for Success

- Read the documentation to learn what methods and helpers are available
- Test extensively with `sneks run` before submitting
- Add debug print statements and use `--step-keypress-wait` to step through the game slowly and understand what's
  happening

## Updating the submission template dependencies

If directed by your contest coordinator, you can use the following command to update the submission template
dependencies to the latest version:

```
pip install --upgrade --upgrade-strategy eager --editable .
```
