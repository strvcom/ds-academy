# Contributing to STRV Data Science Academy

TODO

## Setup

The whole setup is described [here](../lectures/00_start/environment-setup.md#setup). However, ensure that you are
installing the right [environment in the development folder](environment.yml). Additional dependencies are needed for
the development (mainly to generate the handbook).

## How Can I Contribute?

The process described here has several goals:

- Maintain **STRV quality**
- Follow the [STRV guides](https://github.com/strvcom/awesome-ds-docs/tree/master/guides)
- Solve problems/tasks that are important to attendees, follow [issues](https://github.com/strvcom/ds-academy/issues)
  and the [project page](https://github.com/strvcom/ds-academy/projects/1)
- Make sure that you **update both conda environments** when adding dependencies

### Reporting Bugs

Follow the guidelines described [here](../README.md#reporting-bugs).

### Suggesting Enhancements

Follow the guidelines described [here](../README.md#suggesting-enhancements).

### Creating Handbook

This is a quick guide describing the process of turning this repository into a handbook hosted on GitHub Pages.

> ✏️ Run all commands presented in this guide with the environment.

#### Build handbook’s HTML

Do so by running the following command:

```console
jupyter-book build --all ./
```

This will generate a fully-functioning HTML site using a static site generator. The site will be placed in
the `_build/html` folder. The outputs should not be tracked in the main repository.

To preview your book, you can open the generated HTML files in your browser. Double-click the html file in your
local folder.

To find additional information, consult the [official guide](https://jupyterbook.org/en/stable/start/build.html).

#### Publish handbook to GitHub Pages

Do so by running the following command:

```console
ghp-import -n -p -f ./_build/html
```

The command uploads generated content to `gh-pages` branch. The branch is already registered with GitHub Pages. Vist the
[project's GitHub Page](https://strvcom.github.io/ds-academy/intro.html) to see final results.

To find additional information, consult the [official guide](https://jupyterbook.org/en/stable/start/publish.html).