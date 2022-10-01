# Documentation

[![Documentation Status](https://readthedocs.org/projects/cislunar-explorers-software-documentation/badge/?version=latest)](https://cislunar-explorers-software-documentation.readthedocs.io/en/latest/?badge=latest)

Documentation for the Cislunar Explorers mission

## Viewing the Documentation

Simply go to the documentation [website](https://cislunar-explorers-software-documentation.readthedocs.io/en/latest/)!

## Adding to the Documentation

### Setting up

Create a virtual Python environment and install the necessary dependencies from the requirements file. Make sure you run this from the root of the repository!

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You can exit this environment by running `deactivate`. To re-enter an existing environment, all you need is `source venv/bin/activate`. 

#### Viewing your changes locally

To build/view your changes locally without needing to push, run the following:

```bash
make html
cd build/html
python -m http.server 8080
```

Then, visit `http://localhost:8080` in a browser.