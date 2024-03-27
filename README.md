













--------------------------------PART 9-------------------
## Tasks

Create CRUD capabilities for all 3 models within our School API.

- Grade:
  - Create a Grade with a Student, Subject, and a starting grade of 100.00
  - Update a Grades numeric value
  - Delete a Grade for a Student and Subject

- Student:
  - Create a Student with default values and no subject
  - Create a route that will allow you to add subjects to students
  - Update a Students (all fields)
  - Delete a Student from the DB

- Subject:
  - Create a Subject with default values
  - Update the name or professor of a Subject
  - Delete a Subject

  
# School API IX

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## School API Update Capability

In this assignment you will implement the users capability to update Student, Subject, and Grade Data within our Django API through our React application.



--------------------------------PART 7-------------------
# School API VII

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## Tasks

- Update app urls.py files with url patterns and paths
- Create APIViews for GET requests that will Respond with the correct serialized data
- Ensure url paths contain the proper url pattern, Class Based View (as_view()), and name



## A Students

Build an API endpoint of `http://127.0.0.1:8000/api/v1/students/3/` with the name of `a_students`, that will return a students inside the the database in the following format or a 404 Response:

```json
{
  "name": "Francisco R. Avila",
  "student_email": "francisco@school.com",
  "personal_email": "francisco@gmail.com",
  "locker_number": 1,
  "locker_combination": "12-12-12",
  "good_student": true,
  "subjects": [
    {
      "subject_name": "Python",
      "professor": "Professor Adam",
      "students": 6,
      "grade_average": 54.05
    }
  ]
}
```

## A Subjects

Build an API endpoint of `http://127.0.0.1:8000/api/v1/subjects/python/` with the name of `a_subjects`, that will return a subjects inside the the database in the following format or a 404 Response:

```json
{
  "subject_name": "Python",
  "professor": "Professor Adam",
  "students": 6,
  "grade_average": 54.05
}
```

## Running Tests

Delete all the test files inside of each individual application. Add the `tests` folder inside of this repository to your projects ROOT directory.

```bash
  python manage.py test tests
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run

## Considerations

Consider utilizing django shortcuts for querying the database and automatically returning a 404 response if the query returns None.




--------------------------------PART 6-------------------
# School API VI

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## All Students

Build an API endpoint of `http://127.0.0.1:8000/api/v1/students/` with the name of `all_students`, that will return all students inside the the database in the following format:

```json
[
    {
        "name": "Francisco R. Avila",
        "student_email": "francisco@school.com",
        "personal_email": "francisco@gmail.com",
        "locker_number": 1,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            }
        ],
    },
    {
        "name": "Adam B. Cahan",
        "student_email": "adam@school.com",
        "personal_email": "adam@gmail.com",
        "locker_number": 2,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            },
            {
                "subject_name": "Javascript",
                "professor": "Professor Zaynab",
                "students": 4,
                "grade_average": 41.33,
            },
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
        ],
    },
    {
        "name": "This I. Zaynab",
        "student_email": "zaynab@school.com",
        "personal_email": "zaynab@gmail.com",
        "locker_number": 3,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
            {
                "subject_name": "History",
                "professor": "Professor Nick",
                "students": 5,
                "grade_average": 25.39,
            },
            {
                "subject_name": "Philosophy",
                "professor": "Professor Avila",
                "students": 5,
                "grade_average": 51.37,
            },
        ],
    },
    {
        "name": "Tanjaro D. Kamado",
        "student_email": "tanjaro@school.com",
        "personal_email": "tanjaro@gmail.com",
        "locker_number": 4,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Javascript",
                "professor": "Professor Zaynab",
                "students": 4,
                "grade_average": 41.33,
            },
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
            {
                "subject_name": "History",
                "professor": "Professor Nick",
                "students": 5,
                "grade_average": 25.39,
            },
        ],
    },
    {
        "name": "Mark M. Grayson",
        "student_email": "mark@school.com",
        "personal_email": "mark@gmail.com",
        "locker_number": 5,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            },
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
            {
                "subject_name": "Philosophy",
                "professor": "Professor Avila",
                "students": 5,
                "grade_average": 51.37,
            },
        ],
    },
    {
        "name": "Ash A. Katchum",
        "student_email": "ash@school.com",
        "personal_email": "ash@gmail.com",
        "locker_number": 6,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            },
            {
                "subject_name": "Javascript",
                "professor": "Professor Zaynab",
                "students": 4,
                "grade_average": 41.33,
            },
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
        ],
    },
    {
        "name": "Nezuko M. Kamato",
        "student_email": "nezuko@school.com",
        "personal_email": "nezuko@gmail.com",
        "locker_number": 7,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "C#",
                "professor": "Professor Benjamin",
                "students": 6,
                "grade_average": 42.54,
            },
            {
                "subject_name": "History",
                "professor": "Professor Nick",
                "students": 5,
                "grade_average": 25.39,
            },
            {
                "subject_name": "Philosophy",
                "professor": "Professor Avila",
                "students": 5,
                "grade_average": 51.37,
            },
        ],
    },
    {
        "name": "Monkey D. Luffy",
        "student_email": "monkey@school.com",
        "personal_email": "monkey@gmail.com",
        "locker_number": 8,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            },
            {
                "subject_name": "History",
                "professor": "Professor Nick",
                "students": 5,
                "grade_average": 25.39,
            },
            {
                "subject_name": "Philosophy",
                "professor": "Professor Avila",
                "students": 5,
                "grade_average": 51.37,
            },
        ],
    },
    {
        "name": "Monkey D. Ace",
        "student_email": "ace@school.com",
        "personal_email": "ace@gmail.com",
        "locker_number": 9,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "History",
                "professor": "Professor Nick",
                "students": 5,
                "grade_average": 25.39,
            }
        ],
    },
    {
        "name": "Nick M. Smith",
        "student_email": "nick@school.com",
        "personal_email": "nick@gmail.com",
        "locker_number": 10,
        "locker_combination": "12-12-12",
        "good_student": true,
        "subjects": [
            {
                "subject_name": "Python",
                "professor": "Professor Adam",
                "students": 6,
                "grade_average": 54.05,
            },
            {
                "subject_name": "Javascript",
                "professor": "Professor Zaynab",
                "students": 4,
                "grade_average": 41.33,
            },
            {
                "subject_name": "Philosophy",
                "professor": "Professor Avila",
                "students": 5,
                "grade_average": 51.37,
            },
        ],
    },
]
```

## All Subjects

Build an API endpoint of `http://127.0.0.1:8000/api/v1/subjects/` with the name of `all_subjects`, that will return all subjects inside the the database in the following format:

```json
[
    {
        "subject_name": "Python",
        "professor": "Professor Adam",
        "students": 6,
        "grade_average": 54.05,
    },
    {
        "subject_name": "Javascript",
        "professor": "Professor Zaynab",
        "students": 4,
        "grade_average": 41.33,
    },
    {
        "subject_name": "C#",
        "professor": "Professor Benjamin",
        "students": 6,
        "grade_average": 42.54,
    },
    {
        "subject_name": "History",
        "professor": "Professor Nick",
        "students": 5,
        "grade_average": 25.39,
    },
    {
        "subject_name": "Philosophy",
        "professor": "Professor Avila",
        "students": 5,
        "grade_average": 51.37,
    },
]
```

## Running Tests

Delete all the test files inside of each individual application. Add the `tests` folder inside of this repository to your projects ROOT directory.

```bash
  python manage.py test tests
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run

## Considerations

You just made some changes to your student model, meaning you may have to adjust your tests regarding `serializers` to match the new output. Ensure to write serializers and validators to the best of your ability

## Tasks

- Create and/or Update Serializers to return the correct Data
- Ensure test 18 and 19 of test_models.py are passing (confirms serializers are returning the proper data)
- Create app urls.py files with url patterns and paths
- Create APIViews for GET requests that will Respond with the correct serialized data
- Ensure url paths contain the proper url pattern, Class Based View (as_view()), and name


--------------------------------PART 5 -------------------

# School API V

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## Student Model

In this assignment we will extend the application of the Student Models fields by creating a ManyToMany relationship to the Class Model and Grade.

| field              | required | type    | example data         | unique | default    | validator/s                          | related_name |
| ------------------ | -------- | ------- | -------------------- | ------ | ---------- | ------------------------------------ | ------------ |
| name               | True     | string  | John W. Watson       | False  | None       | custom regex format                  |              |
| student_email      | True     | string  | johnnyBoy@school.com | True   | None       | custom regex to end in '@school.com' |              |
| personal_email     | False    | string  | johnnyBoy@gmail.com  | True   | None       | None                                 |              |
| locker_number      | True     | int     | 137                  | True   | 110        | MinVal = 1 and MaxVal = 200          |              |
| locker_combination | True     | string  | 37-68-98             | False  | "12-12-12" | custom regex format                  |              |
| good_student       | True     | boolean | True                 | False  | True       | None                                 |              |
| subjects            | True     | MtM     | [1,2,3]              | False  | None       | 0 < x < 8                            | students     |

- Methods:
  - add_subject method: ensures the student has less than 8 subjects before adding a subject
    - Parameter: subject_id (Subject class PK)
    - Exception: "This students class schedule is full!"
  - remove_subject method: ensures the student has at least 1 class before removing the class.
    - Parameter: subject_id (Subject class PK)
    - Exception: "This students class schedule is empty!"

## Subject Model

In this assignment we will implement the Subject Model to allow Students to take classes.

| field     | required | type   | example data    | unique | default   | validator/s         |
| --------- | -------- | ------ | --------------- | ------ | --------- | ------------------- |
| subject_name   | True     | string | Intro to Python | True   | None      | custom regex format |
| professor | True     | string | Mr. Cahan       | False  | Mr. Cahan | custom regex format |
| students  | True     | MtM    | [1,2,3]         | False  | None      | 0 > x < 31          |

- Validators

  - validate_subject_format: Ensures only string in Title() format is accepted
    - Exception: "Subject must be in title case format."
  - validate_professor_name: Ensures only string in the following format "Professor John" is accepted
    - Exception: 'Professor name must be in the format "Professor Adam".'

- Methods:
  - \_\_str\_\_ : returns "{subject} - {professor} - {students count}"
  - add_a_student: Takes in a Students pk||id and adds it to the students relationship if the subject has less than 31 students
    - Exception: "This subject is full!"
  - drop_a_student: Takes in a Students pk||id and drops it from the students relationship along with the students grade if subject has at least 1 student within it
    - Exception: "This subject is empty!"

## Grade Model

In this assignment we will implement the Grade Model to give each student taking a class and a Grade.

| field   | required | type    | example data | unique | default | validator/s                |
| ------- | -------- | ------- | ------------ | ------ | ------- | -------------------------- |
| grade   | True     | decimal | 100          | False  | 100     | MaxVal = 100.00 && MinVal = 0.00 |
| a_subject | False     | FKR     | 1            | False  | None    | None                       |
| student | False     | FKR     | 1            | False  | None    | None                       |

## Creating New Apps

In this assignment we will create 2 new apps:

- subject_app
- grade_app

```bash
  python manage.py start_app <name_of_app>
```

**Don't forget to add apps into the `INSTALLED_APPS` section in the projects settings.py**

## Running Tests

Delete all the test files inside of each individual application. Add the `tests` folder inside of this repository to your projects ROOT directory.

```bash
  python manage.py test tests
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run

## Considerations

You just made some changes to your student model, meaning you may have to adjust your tests regarding `serializers` to match the new output. Ensure to write serializers and validators to the best of your ability for all apps.




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