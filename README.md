# M42PL - Selenium commands

This repository hosts a set of commands for [M42PL](m42pl-core) to interacts
with [Selenium](selenium).

> Selenium is an umbrella project encapsulating a variety of tools and
  libraries enabling web browser automation.

Please note that you'll need to deploy a [Selenium hub](selenium-hub) to use
the `selenium_*` commands.

## Installation

### Production

To do.

### Developement

* Ensure [M42PL](m42pl-core) is installed
* Clone the repository: `git clone https://github.com/jpclipffel/m42pl-selenium`
* Install the package: `pip install -e m42pl-selenium`

## Usage

Include the package when starting M42PL, e.g. `m42pl repl -m m42pl_selenium`.

## Commands

| Aliases         | Syntax                | Description                                    |
|-----------------|-----------------------|------------------------------------------------|
| `selenium_get`  | `<url> [parameters] ` | Open a URL                                     |
| `selenium_find` | `<kind> <locator>`    | Locate objects `kind` with the given `locator` |

All commands support the same set of `parameters`:

| Parameter          | Description                                | Default                        |
|--------------------|--------------------------------------------|--------------------------------|
| `session_id={...}` | Selenium session ID                        | Generated at run time          |
| `browser={...}`    | Browser name to use (Chrome, Firefox, etc) | `Chrome`                       |
| `hub={...}`        | Selenium hub URL                           | `http://127.0.0.1:4444/wd/hub` |

By default, the first `selenium` command in a pipeline will instanciate a new
driver and a new session. The session ID is propagated to the next commands
through the `meta` attribute `selenium_session_id`.

You can force a command to use a specific session ID using the `session_id`
parameters (see bellow).

### `selenium_get`

Open a web page, creating a new session if necessary.

### `selenium_find`

Locate elements on the session using the given element `kind` and `locator`.

| Kind | Description |
|------|-------------|
| `xpath` | Locate elements using an `XPath` expression |

To do: Add the other `kind` from [here](https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webelement.WebElement.find_element).

---

[m42pl-core]: https://github.com/jpclipffel/m42pl-core
[selenium]: https://github.com/SeleniumHQ/selenium
[selenium-hub]: https://github.com/SeleniumHQ/docker-selenium
