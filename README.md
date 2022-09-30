<p align="center">
  <img src="https://user-images.githubusercontent.com/87664239/183072505-f90dfcf1-8347-4fba-bb0a-e022f0fdee33.png">
  <br>
  <br>
   <img src="https://img.shields.io/badge/license-MIT-brightgreen" alt="contributors" href="https://github.com/zuri-training/team-15_my-cms/blob/main/LICENSE">
   <img src="https://img.shields.io/pypi/pyversions/django" alt="python-versions" href="https://www.python.org/downloads/">
   <img src="https://img.shields.io/pypi/v/pipenv" alt="pypi" href="https://python.org/pypi/pipenv">
   <img src="https://img.shields.io/badge/code%20style-black%20%7C%20prettier-blueviolet" alt="code style" href="#badge">
   <img src="https://img.shields.io/github/contributors/zuri-training/team-15_my-cms" alt="contributors" href="https://github.com/zuri-training/team-15_my-cms/graphs/contributors">
</p>

Clovar is a Content Management System.
It is a platform that allows users to spin up a basic website and allows as many customizations as possible.

## Contributing

See [`CONTRIBUTING.md`](https://github.com/zuri-training/my_cms-pjt-15/blob/main/CONTRIBUTING.md) if you want to make contributions to this project.

Please ensure you follow the steps in the [`CONTRIBUTING.md`](https://github.com/zuri-training/my_cms-pjt-15/blob/main/CONTRIBUTING.md). If you don't, your contribution will be rejected.

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

Create a `.env` file in the same directory as the `settings.py` (`config` folder) with the following contents:

> **Don't enclose the secret key in any quotation mark.**

```python
SECRET_KEY=<your-secret-key>
```

*Generate a secret key from <https://djecrety.ir/>.*

Run the migrations

```python
python manage.py migrate
```

Run the server

```python
python manage.py runserver
```

> Architecture Used: Monolith (Django Templating)

## Features

- **User: Unauthenticated**
  - Visit the platform to view basic information about it.
  - View and Interact with the documentation.
  - Register to set up a new website.
  - Setup the website by filling out some information.
  - Browse through available templates.

- **User: Authenticated**
  - Full access to the platform.
  - Access to the backend of the created website.
  - Ability to create more pages.
  - Ability to change the template.
  - Unique address.
  - Ability to add social media links.

## Tools Used

HTML • CSS • JavaScript • Python • Django • Figma

## Useful Resources

- [Documentation](https://zuri-training.github.io/clovar-documentation).
- [Database Schema](https://drawsql.app/optimistic/diagrams/team-15-my-cms)
- [Figma Board](https://www.figma.com/file/lKANaLq3ZTbx80EsqDymdn/Team-15_My-cms-(Copy)?node-id=755%3A669)

## Contributors

<details><summary>Developers</summary>

- [@jeremy0x](https://www.github.com/jeremy0x)
- [@chidiarua](https://www.github.com/chidiarua)
- [@steph-ayo](https://www.github.com/steph-ayo)
- [@optimistictech](https://www.github.com/optimistictech)
- [@alvanokey](https://www.github.com/alvanokey)
- [@magnificientStudios](https://www.github.com/magnificientStudios)
- [@BioMeindinyo](https://www.github.com/BioMeindinyo)
- [@yusufadegbite](https://www.github.com/yusufadegbite)
- [@Noble101](https://www.github.com/Noble101)
- [@musoye](https://www.github.com/musoye)
- [@Chelsofia](https://www.github.com/Chelsofia)
- [@Ismat27](https://www.github.com/Ismat27)
- [@Prideland-okoi](https://github.com/Prideland-okoi)

</details>

<details><summary>Product Designers</summary>

- [@Paccid](https://www.github.com/Paccid)
- [@Bisolaawwal](https://www.github.com/Bisolaawwal)
- [@Rhoda-k](https://www.github.com/Rhoda-k)
- [@Anya-ndulue](https://www.github.com/Anya-ndulue)
- [@Temarii](https://www.github.com/Temarii)
- [@Dizue](https://www.github.com/Dizue)
- [@Joshua-Ogunwoolu](https://github.com/Joshua-Ogunwoolu)
- [@Emmanuel-Etukudo](https://www.github.com/Emmanuel-Etukudo)

</details>
