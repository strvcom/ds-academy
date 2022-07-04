# Setup Environment

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
