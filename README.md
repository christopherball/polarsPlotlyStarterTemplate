# Polars & Plotly Starter Template

## Instructions

From within VSCode...

1. Press `Cmd + Shift + P`
2. Select `Python: Create Environment`
3. Select `Venv`
4. Add new terminal below (`+`) and ensure the new console has a prefix of `(.venv)`.
5. Run `pip install -r requirements.txt` to install all required packages. This txt file was originally created via `pip freeze > requirements.txt`.

## VSCode Extensions

Install the following extensions:

1. `Python` (by Microsoft)
2. `Jupyter` (by Microsoft)
3. `Black Formatter` (by Microsoft) - Optional

## Notes

-   If you'd like to create a Jupyter Notebook, press `Cmd + Shift + P`, then search for and select `Create: New Jupyter Notebook`.
-   Ensure that the kernel in the upper right corner of your notebook is set to your `venv`.
-   All dependencies for this project exist within the `.venv` folder.
-   If you export-to-HTML Jupyter Notebooks from within VSCode, you can run `python ./notebookStyler.py notebook.html` to apply my manually crafted VSCode-matching dark theme. The corresponding `custom.css` file will now be referenced by the html file and thus must move with it.
-   If Pylance has resolution issues, either restart VSCode or run the `Developer: Reload Window` command.
