# How to Contribute to this Project

Learn how to use git with multiple people working on a project - [How to use git with multiple people working on the same project](https://medium.com/@sriteja95/how-to-use-git-with-multiple-people-working-on-the-same-project-8fb411bad6b9).

**Working on your first Pull Request?**

You can learn how from this *free* series: [How to Contribute to an Open Source Projects on GitHub](https://kcd.im/pull-request).

## How to run this project locally

> Preferred tool for creating and managing virtual environmnents: `pipenv` (see installation guide: <https://pypi.org/project/pipenv/>)

1. Clone this repo (which create a folder)
2. Change directory into the repo folder (using the `cd` command)
3. Run this command: `pipenv install django` (this step will create a virtual environment that will take the repo name and install django in it)
4. Run this command to activate the environment: `pipenv shell`
5. While in the virtual environment, create your repo branch and switch into it
6. Lastly, install all packages in the Pipfile with this command: `pipenv install` (or, you can choose to install individual packages with: `pipenv install package-name`)

### Major packages used at the moment (list will be updated as we progress)
- `django-environ` (tip: pipenv install django-environ)
