# Sneks

Sneks is a programming competition where you build the behavior for Sneks that compete against other players'
submissions. Write Python code to control your Snek's behavior, then upload it to see how it performs!

Build the behavior for your Snek and upload it at [sneks.dev/submit](https://www.sneks.dev/submit) to see how it does
against other submitters. See the website for [live results](https://www.sneks.dev) and details regarding scoring and
submission help.

## Getting started

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

### Develop your Snek

In `src/submission/submission.py`, modify the logic of `get_next_action()`
to control your Snek's behavior. See [sneks.dev/docs](https://www.sneks.dev/docs/index.html) for documentation of the
classes and helper functions available to help refine your Snek. There are also a couple example Sneks in `src/examples`
that can be used as starting points.

## CLI Reference

Run `sneks --help` for full usage information.

### `sneks run`

Run your Snek locally to test its behavior.

| Option                 | Default | Description                      |
|------------------------|---------|----------------------------------|
| `--runs`               | 1       | Number of game runs to execute   |
| `--sneks-count`        | 1       | Number of Sneks to spawn         |
| `--step-delay`         | 40      | Delay in ms between steps        |
| `--step-keypress-wait` | False   | Wait for keypress between steps  |
| `--end-delay`          | 1000    | Delay in ms after run ends       |
| `--end-keypress-wait`  | False   | Wait for keypress after run ends |

### `sneks validate`

Validate your Snek for submission.

## Updating the submission template dependencies

If directed by your contest coordinator, you can use the following command to update the submission template
dependencies to the latest version:

```
pip install --upgrade --upgrade-strategy eager --editable .
```
