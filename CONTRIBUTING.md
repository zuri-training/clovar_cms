# How to Contribute to this Project

Learn how to use git with multiple people working on a project - [How to use git with multiple people working on the same project](https://medium.com/@sriteja95/how-to-use-git-with-multiple-people-working-on-the-same-project-8fb411bad6b9).

**Working on your first Pull Request?**

You can learn how from this *free* series: [How to Contribute to an Open Source Projects on GitHub](https://kcd.im/pull-request).

## Run Locally

> Preferred tool for creating and managing virtual environmnents: `pipenv` (see installation guide: <https://pypi.org/project/pipenv/>).

Clone the project
```bash
  git clone https://github.com/zuri-training/my_cms-pjt-15.git
```

Go to the project directory

```bash
  cd my_cms-pjt-15
```

Create a virtual environment and install django in it

```bash
  pipenv install django
```

Activate the virtual environment
```bash
pipenv shell
```

Create a branch while in that virtual environment and switch into that branch
```bash
git checkout -b your-gihub-username
```

Install all packages in the `Pipfile`
```bash
pipenv install
```
> You can choose to install individual packages with: `pipenv install package-name`)
### Major packages used at the moment (list will be updated as we progress)

- `django-environ` (tip: pipenv install django-environ)

## Note

**Use your username as the branch name when you want to create a branch for contributions.**

To update your branch when there's a change in the main branch,run:

```bash
git checkout your-branch

git pull origin main
```
