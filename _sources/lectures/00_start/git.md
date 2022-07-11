# Git and GitHub

Basic knowledge of [Git](https://git-scm.com/) and [GitHub](https://github.com/) is essential for the course.
Although **we expect some working knowledge of those**, it is good to refresh some basics or review some best
practices before the class.

We expect you to fork the repository periodically to experiment with the code during the course. You will also implement
your end2end ML project that should be hosted on GitHub, so you will have a way to version and share your code with us.

## Git

**Git** is a free and open-source distributed **version control system** designed to handle projects with speed and
efficiency. It is the most widely used modern version control system in the world today.

> ✏️ You might find {cite}`learn_git` nad {cite}`git_cheat_sheet` helpful when working with Git.

To start using Git on your system, we recommend the following guides based on your platform:

- [Install Git on Mac OS X](https://www.atlassian.com/git/tutorials/install-git#mac-os-x)
- [Install Git on Windows](https://www.atlassian.com/git/tutorials/install-git#windows)
- [Install Git on Linux](https://www.atlassian.com/git/tutorials/install-git#linux)

### Basic commands

| Command                                             | Description                                                                                         |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `git clone <link> <repo name in local file system>` | clone repository into local file system                                                             |
| `git status`                                        | check current branch, changes and overall repo status                                               |
| `git log`                                           | list all commits on local active branch (can differ from origin branch when changes are not pulled) |
| `git pull`                                          | update local branch by `origin master` branch                                                       |

### Branch commands

| Command                         | Description                                        |
|---------------------------------|----------------------------------------------------|
| `git branch`                    | list all repo branches (active one is highlighted) |
| `git checkout <branch name>`    | switch into branch                                 |
| `git checkout -b <branch name>` | create branch and switch into new created branch   |
| `git branch -d <branch name>`   | delete branch                                      |
| `git remote prune origin`       | delete unused remote branches from local machine   |

### Branch naming conventions

- `prefix/name-in-lowercase-kebab-case`
- prefix options:
    - `feat/` - feature development
    - `fix/` - bug fix
    - `refactor/` - refactoring
    - `docs/` - documentation
    - `test/` - tests
    - `chore/` - grunt tasks (no production code change)
    - `style/` - code style change

### Commit commands

| Command                                 | Description                                                                                      |
|-----------------------------------------|--------------------------------------------------------------------------------------------------|
| `git add .`                             | add all changed files into commit                                                                |
| `git add <file>`                        | add changed file into commit                                                                     |
| `git commit -m "<message>"`             | create commit with message                                                                       |
| `git commit -m "<message>" -m "<body>"` | create commit with message and body                                                              |
| `git push origin <branch>`              | push commit into branch on public git server                                                     |
| `git commit --amend`                    | add current commit to previous commit (default editor pops up and commit message can be changed) |
| `git push -f origin <branch>`           | force push commit into branch on public git server (aplicable when using `commit --amend`)       |
| `git commit --fixup <commit id>`        | use when fixing commit during code review                                                        |

### Commit message conventions

- `type(optional scope): write short message in lower case and imperative`
- type options are the same as branch prefix options

## GitHub

GitHub is a cloud-based hosting service that lets you manage Git repositories.

To get started working with Git, we recommend reviewing the following:

- [Hello World exercise](https://docs.github.com/en/get-started/quickstart/hello-world) to create a repository (for more
  detail, visit the [link](https://docs.github.com/en/get-started/quickstart/create-a-repo)), create a branch (can be
  handled with Git as well), and contribute to a repository.
- [Fork a repo guide](https://docs.github.com/en/get-started/quickstart/fork-a-repo) to learn how to copy a repository
  to experiment with it. This is the preferred way of getting a copy of the course exercises.
- Once you fork a repo, you might want
  to [keep it synced with the upstream repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)
  . This is recommended way to keep your course copy up to date.

For additional information visit {cite}`learn_github`.

## Resources

```{bibliography}
:filter: docname in docnames
```