# ds-academy

## Creating Handbook

This is a quick guide describing the process of turning this repository into a handbook hosted on GitHub Pages.

### Setup

- Use Conda ENV Manager to create new ENV: `conda env create -f environment.yml`
- Activate the ENV: `conda activate academy-handbook`

**Run all commands presented in this guide with the environment.**

### Build handbook’s HTML

Do so by running the following command:

```
jupyter-book build --all handbook/
```

This will generate a fully-functioning HTML site using a static site generator. The site will be placed in
the `_build/html` folder. The outputs should not be tracked in the main repository.

To find additional information, consult the [official guide](https://jupyterbook.org/en/stable/start/build.html).

### Publish handbook to GitHub Pages

Do so by running the following command:

```
ghp-import -n -p -f handbook/_build/html
```

The command uploads generated content to `gh-pages` branch. The branch is already registered with GitHub Pages. Vist the
[project's GitHub Page](https://strvcom.github.io/ds-academy/intro.html) to see final results.

To find additional information, consult the [official guide](https://jupyterbook.org/en/stable/start/publish.html).