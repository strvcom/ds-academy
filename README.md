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

- Learn more about [STRV Academy](https://www.strv.com/blog/everything-you-need-to-know-about-the-strv-academy-inside-strv)
- All essential materials and information (such as code, theory, guides, and links to resources) are distributed in the
  form of a [handbook](https://strvcom.github.io/ds-academy/intro.html)
- Follow the [Setup](#setup) to be able to create an environment for code execution

### Setup

The code was tested with [conda](https://docs.conda.io/en/latest/) running on Mackbook M1 (ARM-based CPU). It is
generally harder to get Python things running on M1, so the experience on Linux-like and Windows systems should be
smooth.

Before installing the environment,
follow [official instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) for
installing conda on your target platform. We recommend installing the minimal version of **Anaconda** called
**Miniconda**. The minimalistic version includes only conda and its dependencies.

> **NOTE:**  To speed up the installation of any conda environment, install [Mamba](https://github.com/mamba-org/mamba)
> to the base conda environment with the following:
>
> ```console
> conda install mamba -n base -c conda-forge
> ```

Once installed, run the following command to replicate the environment that is being used for lectures and exercises:

```console
mamba env create -f environment.yml
```

If you have installed Mamba. If not, run:

```console
conda env create -f environment.yml
```

You can delete the environment at any time with the command:

```console
conda remove --name ds-academy --all
```

To start using the environment, run:

```console
conda activate ds-academy
```

Once active, you might want to run Jupyter Notebook Server by executing:

```console
jupyter notebook
```

Other alternative ways of executing stuff located in this repository are covered in the handbook <mark>TODO: link</mark>

## Creating Handbook

This is a quick guide describing the process of turning this repository into a handbook hosted on GitHub Pages.

> **NOTE:**  Run all commands presented in this guide with the environment.

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