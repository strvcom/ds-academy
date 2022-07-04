# Setup Environment

## Intro

The project uses [conda](https://docs.conda.io/en/latest/) to manage its environment and packages. Conda is an
open-source package management system and environment management system that runs on Windows, macOS, and Linux. You
should have a relatively smooth experience running the project with any of those platforms.

> **NOTE:**  We test the project running on Linux based system (ML workstations) and MacBook M1 laptops (ARM-based CPU).
> It is
> generally harder to get Python things running on M1. However, we do not test the implementation under Windows.

Well, this guide is not intended as an extensive intro to conda. To get more insight, we recommend reading
{cite}`conda_guide_1` or {cite}`conda_guide_2`.

## Setup

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

## Tips

You can delete the environment and start over at any time with the command:

```console
conda remove --name ds-academy --all
```

## Resources

```{bibliography}
:filter: docname in docnames
```