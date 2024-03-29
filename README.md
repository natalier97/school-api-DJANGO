--------------------------------PART 4 -------------------
# School API IV

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## Student Model

In this assignment we will write the following Django Serializers that will return the following example response for a single Student instance:

- StudentSerializer

```json
{
  "name": "John W. Watson",
  "student_email": "thisIsAnEmail@school.com",
  "locker_number": 13
}
```

- StudentAllSerializer

```json
{
  "name": "John W. Watson",
  "student_email": "thisIsAnEmail@school.com",
  "personal_email": "thisIsAnEmail@gmail.com",
  "locker_number": 13,
  "locker_combination": "12-33-44",
  "good_student": true
}
```

## Running Tests

Replace the `test.py` file inside your app with the `test.py` file already attached to this repository.

Now you can run the test suite by typing the following

```bash
  python manage.py test
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run


--------------------------------PART 3 -------------------
# School API III

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## Student Model

In this assignment we will extend the application of the Student Models fields by validating data entry to either custom or built in validators.

| field     | required |type |example data  | unique | default | validator/s |
| --------- | -----|-------|------------- | --------| ------- | ----------- |
| name | True |string | John W. Watson | False | None | custom regex format |
| student_email | True | string | johnnyBoy@school.com | True | None | custom regex to end in '@school.com' |
| personal_email | False | string | johnnyBoy@gmail.com | True | None | None |
| locker_number | True |int |137 | True | 110 | MinVal = 1 and MaxVal = 200 |
| locker_combination | True |string |37-68-98 | False | "12-12-12"| custom regex format |
| good_student | True |boolean | True | False | True | None |

- Custom Validators
  - validate_name_format: Only accepts string in the following format "First M. Last"
    - Validation Error: 'Name must be in the format "First Middle Initial. Last"'
  - validate_school_email: Only accepts string ending with "@school.com"
    - Validation Error: 'Invalid school email format. Please use an email ending with "@school.com".'
  - validate_combination_format: Only accepts string in the following format "12-12-12" (Ensures there are numbers only)
    - Validation Error: 'Combination must be in the format "12-12-12"'

## Running Tests

Replace the `test.py` file inside your app with the `test.py` file already attached to this repository.

Now you can run the test suite by typing the following

```bash
  python manage.py test
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run

--------------------------------PART 1 -------------------
# School API

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and schollastic equipment.

## Student Model

In this assignment we will create a Student Django Model with the following fields

| field            | required |type |example data                    |
| ----------------- | -----|-------|------------- |
| name | True |string | John W. Watson |
| student_email | True | string(email) | johnnyBoy@school.com |
| personal_email | False | string(email) | johnnyBoy@gmail.com |
| locker_number | True |int |137 |
| locker_combination | True |string |37-68-98 |
| good_student | True |boolean | True |

## Django Set Up

Creating and activating VENV

```bash
  #creating venv
  python -m venv <name_of_env>

  #activating venv
  source <name_of_env>/bin/activate
```

Installing Django and starting a project with an app

```bash
    #installing Django
    pip install django

    #creating project
    django-admin startproject school_proj .

    #creating student app
    python manage.py startapp student_app
```

Creating Database

```bash
    createdb school_db
```

**Don't forget to add the app under the `INSTALLED_APPS` section in `settings.py` and changing from sqlite to postgresql with a database name!**

Installing Psycopg3 to speak with PostgreSQL

```bash
  pip install "psycopg[binary]"
```

Once the Student Model is completed makemigrations and migrate to the school_db

```bash
  python manage.py makemigrations
  python manage.py migrate
```

## Running Tests

Replace the `test.py` file inside your app with the `test.py` file already attached to this repository.

Now you can run the test suite by typing the following

```bash
  python manage.py test
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run


--------------------------------PART 2 -------------------

# School API II

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## Student Model

In this assignment we will extend the application of the Student Models fields by specifying which fields should or should not be unique and assigning default values.

| field            | required |type |example data  | unique | default |
| ----------------- | -----|-------|------------- | --------| ------- |
| name | True |string | John W. Watson | False | None |
| student_email | True | string | johnnyBoy@school.com | True | None |
| personal_email | False | string | johnnyBoy@gmail.com | True | None |
| locker_number | True |int |137 | True | 110 |
| locker_combination | True |string |37-68-98 | False | "12-12-12"|
| good_student | True |boolean | True | False | True |

## Student Model Methods

Now that we've added some more details to our student table we can begin adding some methods to this model class:

- str__ Method:    Returns student name, student email, and locker number as such "John W. Watson - johnnyBoy@school.com - 137"
- locker_reassignment method: Takes in an int representing the new locker number and will change a students "locker_number" property to said value
- student_status method: Takes in a bool representing if a student is a good student and changes a students "good_student" property to said value

## Running Tests

Replace the `test.py` file inside your app with the `test.py` file already attached to this repository.

Now you can run the test suite by typing the following

```bash
  python manage.py test
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run