# learn-flask

## Table of Contents

- [learn-flask](#learn-flask)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Testing](#testing)
  - [Installation](#installation)
  - [Setup](#setup)
    - [Clone this Project](#clone-this-project)
    - [Github Project from Scratch](#github-project-from-scratch)
    - [Local Only Project from Scratch](#local-only-project-from-scratch)
    - [Creating a Poetry Project](#creating-a-poetry-project)
    - [Install Python Dependencies](#install-python-dependencies)

## Overview

This project is more of a learn by example then a tutorial, it
provides a set of documented examples for each advancing step in
the development of a Flask application.

1. [Basic](./learn_flask/01_basic/__init__.py)
2. [Routing](./learn_flask/02_routing/__init__.py)
3. [Routing Rules](./learn_flask/03_routing_rules/__init__.py)
4. [HTML Escaping](./learn_flask/04_html_escaping/__init__.py)
5. [Unique URLs and Redirects](./learn_flask/05_unique_urls_and_redirects/__init__.py)
6. [HTTP Methods](./learn_flask/06_http_methods/__init__.py)


## Testing

This repository has been onboarded with Poetry and Nox Poetry, so you can
run the following to install the dependencies:

```bash
poetry install
```

To run the Nox test sessions, you can use the following:

```bash
poetry run nox -s tests
```

To run the specific applications locally you can use the
following:

```bash
poetry run 01_basic
poetry run 02_routing
poetry run 03_routing_rules
poetry run 04_html_escaping
poetry run 05_unique_urls_and_redirects
poetry run 06_http_methods
```


## Installation

For Ubuntu, install the required dependencies:

```bash
sudo apt update && sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
```

Install Pyenv:

```bash
curl https://pyenv.run | bash
```

Add Pyenv Environment Variables to your `~/.bashrc`:

```bash
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Reload your `~/.bashrc`:

```bash
source ~/.bashrc
```

Verify your version to ensure installation was complete:

```bash
pyenv --version
```

Install Python 3.11:

```bash
pyenv install 3.11
```

Set 3.11 as your Global version:

```bash
pyenv global 3.11
```

Now any shell you open will use this global version by default:

```bash
$ python -V
Python 3.11.5
```

Install Python Poetry:

```
curl -sSL https://install.python-poetry.org | python3 -
```

Add the following to your `~/.bashrc`:

```
[ -f "$HOME/.poetry/env" ] && . $HOME/.poetry/env
```

Reload your `~/.bashrc`:

```bash
source ~/.bashrc
```

Check the Poetry command works:

```bash
$ poetry --version
Poetry (version 1.7.1)
```

## Setup

Choose between either of the following next steps on how to begin a project:

- [learn-flask](#learn-flask)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Testing](#testing)
  - [Installation](#installation)
  - [Setup](#setup)
    - [Clone this Project](#clone-this-project)
    - [Github Project from Scratch](#github-project-from-scratch)
    - [Local Only Project from Scratch](#local-only-project-from-scratch)
    - [Creating a Poetry Project](#creating-a-poetry-project)
    - [Install Python Dependencies](#install-python-dependencies)

### Clone this Project

Clone the Repository and `cd` to it:

```bash
git clone github.com:xransum/learn-flask
cd learn-flask/
```

Continue from [Install Python Dependencies](#install-python-dependencies)

### Github Project from Scratch

Create a [GitHub](https://github.com) a repository, and populate
it with `README.md` and `LICENSE` files, preferably use the
[MIT license](https://choosealicense.com/licenses/mit/), since
it's a simple permissive license.

Clone the repository to your machine, and `cd` into it:

```
git clone git@github.com:<github-username>/new-project.git
cd new-project/
```

### Local Only Project from Scratch

Create your project directory and `cd` to it:

```bash
mkdir new-project
cd new-project/
```

Continue from [Creating a Poetry Project](#creating-a-poetry-project).

### Creating a Poetry Project

Initialize your Python project:

```bash
poetry init
```

You should see something of the sorts:

```bash
$ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [new-project]:
Version [0.1.0]:
Description []:  My project for doing things!
Author [github-username-here <github-username-here@users.noreply.github.com>, n to skip]:
License []:  MIT
Compatible Python versions [^3.11]:

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "new-project"
version = "0.1.0"
description = "My project for doing things!"
authors = ["github-username-here <github-username-here@users.noreply.github.com>"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

Do you confirm generation? (yes/no) [yes] yes
```

You should now have a `pyproject.toml` file, the new Python package
configuration file specified in [PEP 517](https://www.python.org/dev/peps/pep-0517/)
and [518](https://www.python.org/dev/peps/pep-0518/).

Continue from [Install Python Dependencies](#install-python-dependencies)

### Install Python Dependencies

To add dependencies, you can use the following:

```bash
poetry add Flask
```

To remove dependencies:

```bash
poetry remove Flask
```

From within your project directory, you can use the install
sub-command with Poetry to install the dependencies specified
in your projects `pyproject.toml`.

```bash
poetry install
```
