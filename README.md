# Std Tech Dept Template

Template of python project by cookiecutter.

## Installation

Install cookiecutter

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install cookiecutter
pip install --upgrade pip
pip install cookiecutter
```

Create project

```bash
# There might be some templates in the future, so you can choose one of them.
# https://github.com/hinnytsang/std-tech-dept-template.git
#     |
#     ├── py-basic/  <- example: --directory="py-basic"
#     |   ├── {{cookiecutter.project_slug}}/
#     |   └── cookiecutter.json
#     └── ...

cookiecutter gh:HinnyTsang/std-tech-dept-template --directory="directory_name"
```

A project will be created in current directory, you can see it by the following command.

```bash
ls -l
```

## User defined configuration

There is a default configuration template in each template `<template/custom-config.template.yaml>`, you can modify it to fit your project.
