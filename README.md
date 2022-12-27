# Sneks submission template

Build the behavior for your Snek and upload it at https://www.sneks.dev/submit to see how
it does against other submitters. See the website for details regarding scoring and
submission help.

## Getting started

### Prerequisites

1. Install Python >=3.8 from https://www.python.org/downloads/
   1. Add Python to your Path to make things easier
2. _(Optional)_ Install an IDE to work in
   1. [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download)
   2. [Visual Studio Code](https://code.visualstudio.com/)
3. Download this repo to your local machine using one of the following options:
   1. Using git
      ```commandline
      git clone https://github.com/schana/sneks-submission.git
      ```
   2. As a zip from https://github.com/schana/sneks-submission/archive/refs/heads/main.zip
      1. Unzip after downloading

### Set up development environment

1. Open a terminal or command prompt
2. Change to the directory where your repo is located
   1. You should be located in the same directory as `pyproject.toml`
3. _(Optional, but recommended)_ Set up a virtual environment
   1. Install `venv` package
      ```commandline
      pip install venv
      ```
   2. Create virtual environment
      ```commandline
      python -m venv venv
      ```
   3. Activate the environment
      1. macOS / Linux
         ```commandline
         source venv/bin/activate
         ```
      2. Windows
         ```commandline
         venv\Scripts\activate
         ```
4. Install this package to enable testing locally
   ```commandline
   pip install --editable .
   ```
5. Ensure everything works by trying out the helper scripts
   1. Test that the current snake passes validation
      ```commandline
      validate
      ```
   2. Run the current snake by itself
      ```commandline
      run
      ```

### Develop your Snek

In `src/submission/snek/submission.py`, modify the logic of `get_next_direction()`
to control your Snek's behavior. See https://sneks.dev/docs for documentation of
the classes and helper functions available to help refine your Snek.
