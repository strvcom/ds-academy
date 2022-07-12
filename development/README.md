# Contributing to STRV Data Science Academy

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

The following is a set of simple guidelines for contributing. These are mostly guidelines, not rules. Use your best
judgment, and feel free to propose changes to this document in a pull request.

> ✏️ If you are not sure, ask [Jan Maly](https://github.com/honzaMaly).

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

> ✏️ Do not forget to list your name in the [intro section](../README.md#strv-data-science-academy).

### Reporting Bugs

Follow the guidelines described [here](../README.md#reporting-bugs).

### Suggesting Enhancements

Follow the guidelines described [here](../README.md#suggesting-enhancements).

### Project structure

The repository consists of two parts - one covers the development and the second one is the actual course.

#### The development part

| File or directory  | Purpose                                                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------|
| development folder | holds this README.md with guides, several templates and the development environment (environment.yml) |
 | _config.yml        | defines the setting for the handbook and should be left (mostly) untouched                            |
 | _toc.yml           | defines the content of the handbook                                                                   |
 | references.bib     | lists all resources referenced in the course (handbook)                                               |

#### The course part

| File or directory | Purpose                                                                   |
|-------------------|---------------------------------------------------------------------------|
| lectures folder   | holds individual lectures (documents and notebooks) and the intro section |
 | environment.yml   | the conda environment specification used by students during the course    |
 | static            | holds static resources (for example, images)                              |

### Creating Handbook

This is a quick guide describing the process of creating the handbook. Only the most essential steps are included,
mainly the process of turning this repository into a handbook hosted on GitHub Pages. Check out
the [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) documentation to get started.

> ✏️ Run all commands presented in this guide with the development environment.

#### Adding new content

TODO

#### Adding References

TODO

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
