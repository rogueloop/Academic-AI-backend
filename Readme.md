# Poetry Django Project

This is a Django project powered by Poetry, a dependency management tool for Python.

## Prerequisites

- Python 3.x
- Poetry

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Install project dependencies using Poetry:

    ```bash
    poetry install
    ```

4. Apply database migrations:

    ```bash
    poetry run python manage.py migrate
    ```

## Usage

To start the Django development server, run the following command:
    ```bash
    python manage.py runserver
    ```
