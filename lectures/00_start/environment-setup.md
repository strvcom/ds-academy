# Setup Environment

The project uses [conda](https://docs.conda.io/en/latest/) to manage its environment and packages. Conda is an
open-source package management system and environment management system that runs on Windows, macOS, and Linux. You
should have a relatively smooth experience running the project with any of those platforms. **Conda handles library
dependencies outside the Python packages as well as the Python packages themselves.**

> ✏️ We test the project running on Linux based system (ML workstations) and MacBook M1 laptops
> (ARM-based CPU). It is generally harder to get Python things running on M1. However, we do not test the
> implementation under Windows.

Well, this guide is not intended as an extensive intro to conda. To get more insight, we recommend reading
{cite}`vatsal_2022` or {cite}`sarmiento_2020`.

## Setup

Before installing the environment,
follow [official instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) for
installing conda on your target platform. We recommend installing the minimal version of **Anaconda** called
**Miniconda**. The minimalistic version includes only conda and its dependencies.

> ✏️ To speed up the installation of packages, install [Mamba](https://github.com/mamba-org/mamba)
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

To start using the environment, run:

```console
conda activate ds-academy
```

Once active, you might want to run **Jupyter Notebook Server** by executing:

```console
jupyter notebook
```

Another alternative way to execute notebooks is using [IDEs](ide-overview.md). To start with notebooks, check out the
guide on [notebooks](notebooks.ipynb).

## New Environment

It is convenient to create a separate environment for experimenting (and for the end2end ML project).
The `environment.yml` located in the project can be used as an inspiration. Check out recommended resources
{cite}`vatsal_2022` or {cite}`sarmiento_2020` to get a better idea.

In general, we recommend installing as many packages as possible using Conda as it handles library dependencies outside
of the Python packages as well as the Python packages themselves. Most of the packages are hosted
on [conda-forge](https://anaconda.org/conda-forge/repo). If you cannot find your package in any conda-forge repository,
install them using pip.

```yaml
name: my-awesome-project
channels:
  - conda-forge  # prioritize packages from conda-forge repositories
  - defaults
dependencies:
  - python>=3.7,<=3.9  # version of Python, there are minimum requirements on version, we leave it up to conda
  - pip  # a package taken from conda repository
  - matplotlib
  - numpy
  - notebook
  - pip:
      - see  # an example of package installed using pip as it is not available on conda
```

> ✏️ For **production environments**, it is good practice to fix the package version to ensure that
> the environment is the same as the original one. For example, to specify the version of Python,
> use `python>=3.7,<=3.9`.

## Tips

You can delete the `ds-academy` environment and start over at any time with the command:

```console
conda remove --name ds-academy --all
```

## Resources

```{bibliography}
:filter: docname in docnames
```