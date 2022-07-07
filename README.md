# STRV Data Science Academy

> **NOTE:** The repository contains materials used during the STRV Data Science Academy

STRV is pleased to offer this 7-week intensive course as part of
our [STRV Academy](https://www.strv.com/blog/everything-you-need-to-know-about-the-strv-academy-inside-strv).
During the course, you will learn to apply plenty of practical and theoretical skills needed for developing and
completing your own End-to-End Machine Learning Projects. You will gain practical knowledge and hands-on experience
with applied ML techniques and an intuitive understanding of what can be achieved through ML and what its
limitations are.

**Hearty thanks to our authors**: [Jan Maly](https://github.com/honzaMaly), <mark>TODO: add your profiles</mark>

## Getting Started

### Handbook

The handbook for this course can be found [here](https://strvcom.github.io/ds-academy/intro.html).

### How to Use this Course

- Learn more
  about [STRV Academy](https://www.strv.com/blog/everything-you-need-to-know-about-the-strv-academy-inside-strv)
- All essential materials and information (such as code, theory, guides, and links to resources) are distributed in the
  form of a [handbook](https://strvcom.github.io/ds-academy/intro.html)
- Follow the [Setup](#setup) to be able to create an environment for code execution

> ⚠️ There might be some formatting issues when running notebooks. We use a special Markdown
> to generate the handbook.

### Setup

The code was tested with [conda](https://docs.conda.io/en/latest/) running on Mackbook M1 (ARM-based CPU). It is
generally harder to get Python things running on M1, so the experience on Linux-like and Windows systems should be
smoother.

To get your environment up and running for this course, we prepared
a [guide](https://strvcom.github.io/ds-academy/extra/environment-setup.html) describing all the necessary steps to
replicate our environment.

## Creating Handbook

This is a quick guide describing the process of turning this repository into a handbook hosted on GitHub Pages.

> ✏️ Run all commands presented in this guide with the environment.

### Build handbook’s HTML

Do so by running the following command:

```console
jupyter-book build --all ./
```

This will generate a fully-functioning HTML site using a static site generator. The site will be placed in
the `_build/html` folder. The outputs should not be tracked in the main repository.

To preview your book, you can open the generated HTML files in your browser. Double-click the html file in your
local folder.

To find additional information, consult the [official guide](https://jupyterbook.org/en/stable/start/build.html).

### Publish handbook to GitHub Pages

Do so by running the following command:

```console
ghp-import -n -p -f ./_build/html
```

The command uploads generated content to `gh-pages` branch. The branch is already registered with GitHub Pages. Vist the
[project's GitHub Page](https://strvcom.github.io/ds-academy/intro.html) to see final results.

To find additional information, consult the [official guide](https://jupyterbook.org/en/stable/start/publish.html).