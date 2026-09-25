# KLEMP

**Key Utility Layer for Environment Management & Processing**

KLEMP is a modular command-line utility toolkit written in Python. It brings commonly used file, system, networking, security, utility, and Python-development tools together into a single extensible application.

> **Status:** Active Development

---

## Overview

KLEMP is designed around a modular architecture where individual tools are separated into functional categories. This makes the project easier to maintain, extend, and eventually support automatic module discovery.

The project also serves as a practical environment for exploring Python software architecture, CLI development, file handling, networking, APIs, error handling, and testing.

---

## Features

### File Tools

* File organization by extension
* Batch file renaming
* Duplicate file detection

### System Tools

* System information
* Process information and management
* Storage information

### Network Tools

* Host connectivity testing
* Port checking
* Network information

### Security Tools

* File hashing
* Password utilities

### Utility Tools

* Calculator
* Unit conversion
* Currency conversion
* JSON management

### Python Tools

* Python project creation
* Package inspection
* Python script execution

---

## Architecture

KLEMP follows a layered architecture:

```text
main.py
   │
   ▼
cli.py
   │
   ▼
core.py
   │
   ▼
modules/
   │
   ├── file_tools/
   ├── system_tools/
   ├── network_tools/
   ├── security_tools/
   ├── utility_tools/
   └── python_tools/
```

Supporting functionality is separated into the `utils/` package.

This structure allows individual components to be developed and tested independently.

---

## Project Structure

```text
KLEMP/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── klemp/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   └── core.py
│
├── modules/
│   ├── __init__.py
│   │
│   ├── file_tools/
│   ├── system_tools/
│   ├── network_tools/
│   ├── security_tools/
│   ├── utility_tools/
│   └── python_tools/
│
├── utils/
│   ├── __init__.py
│   ├── colors.py
│   ├── logger.py
│   ├── validators.py
│   └── helpers.py
│
├── tests/
│
└── data/
    ├── config.json
    └── history.json
```

---

## Requirements

* Python 3.10+
* `pip`
* Internet connection for features that depend on external APIs

Python dependencies are listed in:

```text
requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/KLEMP.git
```

Enter the project directory:

```bash
cd KLEMP
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Start KLEMP with:

```bash
python main.py
```

The application provides an interactive command-line interface for accessing the available tools.

---

## Development

KLEMP is structured to make adding new tools straightforward.

A typical module can be added under the appropriate category:

```text
modules/
└── utility_tools/
    └── example_tool.py
```

The long-term architecture is intended to support dynamic module discovery, allowing new tools to be integrated without requiring major changes to the core application.

---

## Roadmap

### Core Functionality

* [x] File organizer
* [x] File renamer
* [x] Duplicate finder
* [x] Calculator
* [x] Unit converter
* [x] Currency converter
* [ ] JSON tools

### System & Networking

* [ ] System information
* [ ] Process management
* [ ] Storage information
* [ ] Network information
* [ ] Ping utility
* [ ] Port checker

### Security

* [ ] File hashing
* [ ] Password utilities
* [ ] Additional security utilities

### Python Development

* [ ] Project generator
* [ ] Package checker
* [ ] Script runner

### Architecture

* [ ] Automatic module discovery
* [ ] Centralized configuration
* [ ] Improved logging
* [ ] Expanded test coverage
* [ ] CLI improvements

---

## Design Principles

KLEMP is developed around several principles:

* **Modularity** — tools should remain independent and replaceable.
* **Maintainability** — functionality should be organized into clear components.
* **Extensibility** — new tools should be easy to add.
* **Reliability** — invalid input and runtime errors should be handled safely.
* **Simplicity** — the CLI should remain straightforward to use.

---

## Contributing

Contributions, suggestions, and improvements are welcome.

Before submitting a contribution:

1. Keep changes focused on a specific feature or issue.
2. Follow the existing project structure.
3. Avoid unnecessary dependencies.
4. Test changes before submitting them.
5. Document new functionality where appropriate.

---

## License

KLEMP is distributed under the **MIT License**.

See [`LICENSE`](LICENSE) for the complete license text.

---

## Author

**Genkichi**

KLEMP is an independent project developed as a modular Python utility toolkit and learning-oriented software project.

---

<p align="center">
  Built with Python
</p>
