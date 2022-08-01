# How to Contribute to this Project

Clone the project

```bash
git clone https://github.com/zuri-training/team-15_my-cms.git
```

Go to the project directory

```bash
cd team-15_my-cms
```

---

<details><summary>Run Locally</summary>

> Preferred tool for creating and managing virtual environments: `pipenv` (see installation guide: <https://pypi.org/project/pipenv/>).

Create a virtual environment and install needed dependencies in it

```bash
pipenv install
```

Activate the virtual environment

```bash
pipenv shell
```

If `django-environ` isn't installed, you can install it with:

```bash
pipenv install django-environ
```

Create a `.env` file in the same directory as the `settings.py` (`config` folder) with the following contents:
> **Don't enclose the secret key in any quotation mark.**

```python
SECRET_KEY=<your-secret-key>
```

*Generate a secret key from <https://djecrety.ir/>.*

</details>

*If you'll just be working on the front-end, the *running locally* section is optional. All your `HTML`, `CSS`, and `JavaScript` files should go into the [`templates`](https://github.com/zuri-training/team-15_my-cms/tree/main/templates) directory.*

---

Create a branch to make your changes to.

```bash
git branch <your-github-username_feature>
```

Switch into your branch

```bash
git checkout <your-github-username_feature>
```

Commit and push your changes to your branch.

```bash
  git add . || git add --all || git add -A
  git commit -m <commit-message>
  git push
```

> You can also just *fork* the repository and make your changes to that fork.

**Create a pull request** on the [GitHub Repository](https://github.com/zuri-training/team-15_my-cms). [Learn How](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

**Request a review for your pull request** from [@jeremiey](https://www.github.com/jeremiey) and [@chidiarua](https://www.github.com/chidiarua).

Your changes will be merged into the `main` branch when they are approved by the reviewers.

<!-- ## Major packages used at the moment (list will be updated as we progress)

> You can choose to install individual packages with: `pipenv install package-name`)

- `django-environ` (run `pipenv install django-environ` to install manually). -->
