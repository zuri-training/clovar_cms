# How to Contribute to this Project

## Run Locally

> Preferred tool for creating and managing virtual environments: `pipenv` (see installation guide: <https://pypi.org/project/pipenv/>).

Clone the project

```bash
  git clone https://github.com/zuri-training/team-15_my-cms.git
```

Go to the project directory

```bash
  cd team-15_my-cms
```

Create a virtual environment and install needed dependencies in it

```bash
  pipenv install
```

Activate the virtual environment

```bash
pipenv shell
```

> If ```django-environ``` isn't installed, you can install it with:

```bash
  pipenv install django-environ
```

Create a branch for you to work on

```bash
git branch <your-github-username>
```

Switch into your branch

```bash
git checkout <your-github-username>
```

Generate a secret key from <https://djecrety.ir/>.

Create a `.env` file in the same directory as the `settings.py` (`config` folder) with the following contents:
> **Don't enclose the secret key in any quotation mark.**

```python
SECRET_KEY=<your-secret-key>
```

Commit and push your changes to your branch.

```bash
  git add . || git add --all || git add -A
  git commit -m <commit-message>
  git push
```

Create a pull request on the [GitHub Repository](https://github.com/zuri-training/team-15_my-cms). [Learn How](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

### Major packages used at the moment (list will be updated as we progress)

> You can choose to install individual packages with: `pipenv install package-name`)

- `django-environ` (run `pipenv install django-environ` to install).

---

**To update your branch when there's a change in the main branch, run the following commands:**

```bash
git checkout main

git pull

git checkout <your-branch-name>

git pull origin main
```
