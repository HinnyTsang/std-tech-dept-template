"""Post generate hook"""

import subprocess
import logging


def update_poetry_and_dependency():
    """Update poetry and dependency"""
    logging.info("Updating poetry and dependency")
    subprocess.run(["poetry", "self", "update"], check=False)
    subprocess.run(["poetry", "update"], check=False)


update_poetry_and_dependency()

print(
    """
    Finish generating project structure with cookie cutter.
    Thanks for using Std Tech Dept Template.
    """
)
