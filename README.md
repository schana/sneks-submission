# Sneks submission template

Build the behavior for your Snek and upload it at [sneks.dev/submit](https://www.sneks.dev/submit) to see how
it does against other submitters. See the website for details regarding scoring and
submission help.

## Getting started

### Prerequisites

1. Install Python >=3.8 from [python.org/downloads](https://www.python.org/downloads/)
   1. Add Python to your Path to make things easier
2. _(Optional)_ Install an IDE to work in
   1. [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download)
   2. [Visual Studio Code](https://code.visualstudio.com/)
3. Download `template.zip` to your local machine from [sneks.dev/template/template.zip](https://www.sneks.dev/template/template.zip)
   and extract its contents.

### Set up development environment

1. Open a terminal or command prompt
2. Change to the directory where the template is located. After unzipping, it should be the directory called
   `sneks-submission-main`.
   1. You should be located in the same directory as `pyproject.toml`
3. _(Optional, but recommended)_ Set up a virtual environment
   1. Install `venv` package
      ```
      pip3 install venv
      ```
   2. Create virtual environment
      ```
      python3 -m venv venv
      ```
   3. Activate the environment
      1. macOS / Linux
         ```
         source venv/bin/activate
         ```
      2. Windows
         ```
         venv\Scripts\activate
         ```
4. Install this package to enable testing locally
   ```
   pip3 install --editable .
   ```
5. Ensure everything works by trying out the helper scripts
   1. Test that the current snake passes validation
      ```
      validate
      ```
   2. Run the current snake by itself
      ```
      run
      ```

### Develop your Snek

In `src/submission/snek/submission.py`, modify the logic of `get_next_direction()`
to control your Snek's behavior. See [sneks.dev/docs](https://www.sneks.dev/docs/index.html) for documentation of
the classes and helper functions available to help refine your Snek.
