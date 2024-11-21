# ShopSphere-Backend

ShopSphere Backend: Backend codebase for ShopSphere, an e-commerce platform for small business. Built on Flask

ecommerce-backend/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   └── config.py
├── migrations/
├── tests/
│   ├── __init__.py
│   ├── test_routes.py
│   ├── test_models.py
│   ├── test_forms.py
├── venv/
├── .gitignore
├── README.md
├── requirements.txt
└── run.py



| Filename             | Description                                                       |
|----------------------|-------------------------------------------------------------------|
| app/                 | Main application folder                                          |
| &nbsp;&nbsp;&nbsp;__init__.py | Initializes the Flask app and sets up configurations          |
| &nbsp;&nbsp;&nbsp;routes.py   | Contains route definitions for your application                |
| &nbsp;&nbsp;&nbsp;models.py   | Defines the database models                                   |
| &nbsp;&nbsp;&nbsp;forms.py    | Contains form definitions using Flask-WTF                      |
| &nbsp;&nbsp;&nbsp;static/     | Holds static files like CSS and JavaScript                     |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;css/    | Folder for CSS files                                           |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;js/     | Folder for JavaScript files                                     |
| &nbsp;&nbsp;&nbsp;templates/  | Holds HTML templates                                         |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base.html | Base template                                                |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index.html | Index page template                                          |
| &nbsp;&nbsp;&nbsp;config.py   | Contains configuration variables for the application          |
| migrations/           | Folder for database migration files (if using Flask-Migrate)      |
| tests/                | Contains unit tests for your application                          |
| &nbsp;&nbsp;&nbsp;__init__.py | Initializes the test package                                |
| &nbsp;&nbsp;&nbsp;test_routes.py | Tests for routes                                        |
| &nbsp;&nbsp;&nbsp;test_models.py | Tests for models                                        |
| &nbsp;&nbsp;&nbsp;test_forms.py  | Tests for forms                                         |
| venv/                 | Virtual environment folder (can be created using `python -m venv venv`) |
| .gitignore            | File to specify which files and directories Git should ignore     |
| README.md             | Project documentation                                             |
| requirements.txt      | File listing the project's dependencies (use `pip freeze > requirements.txt` to generate) |
| run.py                | Entry point to run the application                                |

