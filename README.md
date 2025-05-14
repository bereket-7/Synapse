# TaskMaster Pro - Flask Task Management System

A full-featured task management web application built with Flask, featuring user authentication, task organization, and productivity tools.

## Features

### Core Functionality

- 🔐 User authentication (Register/Login/Logout)
- 📝 Create, read, update, and delete tasks
- 🏷️ Task categorization and prioritization
- 📅 Due date tracking with calendar view
- 🔍 Search and filter tasks

### Advanced Features

- 📧 Email notifications for due tasks
- 📁 File attachments for tasks
- 📊 Productivity dashboard with statistics
- 🔄 Drag-and-drop task reorganization
- 📱 Responsive mobile-friendly design

## Technology Stack

### Backend

- **Framework**: Flask 2.0+
- **Database**: SQLAlchemy (SQLite/PostgreSQL)
- **Authentication**: Flask-Login with password hashing
- **Forms**: Flask-WTF with CSRF protection
- **Templates**: Jinja2 with template inheritance

### Frontend

- **Styling**: Bootstrap 5 + custom CSS
- **JavaScript**: Vanilla JS + HTMX for interactivity
- **Icons**: Font Awesome

### DevOps

- **Environment Management**: python-dotenv
- **Testing**: pytest with 85%+ coverage
- **CI/CD**: GitHub Actions (optional)

## Installation

### Prerequisites

- Python 3.8+
- pip package manager
- (Optional) PostgreSQL for production

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/bereket-7/TaskMasterPro.git
   cd TaskMaskterPro
   ```

````

2. Create and activate virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment:

   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. Initialize database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application:
   ```bash
   flask run
   ```

## Project Structure

```
taskmaster-pro/
├── app/                  # Main application package
│   ├── auth/             # Authentication blueprints
│   ├── tasks/            # Task management blueprints
│   ├── static/           # CSS, JS, images
│   ├── templates/        # Jinja2 templates
│   ├── __init__.py       # Application factory
│   ├── models.py         # Database models
│   └── extensions.py     # Flask extensions
├── tests/                # Unit and integration tests
├── migrations/           # Database migration scripts
├── config.py             # Configuration settings
├── requirements.txt      # Production dependencies
├── requirements-dev.txt  # Development dependencies
└── README.md            # This file
```

## API Documentation

The application provides RESTful endpoints for future mobile integration:

| Endpoint          | Method | Description     |
| ----------------- | ------ | --------------- |
| `/api/tasks`      | GET    | List all tasks  |
| `/api/tasks`      | POST   | Create new task |
| `/api/tasks/<id>` | PUT    | Update task     |
| `/api/tasks/<id>` | DELETE | Remove task     |

View interactive API docs at `/swagger` when running in development mode.

## Deployment

### Production Deployment

1. **Recommended Hosting**:

   - AWS Elastic Beanstalk
   - DigitalOcean App Platform
   - Heroku (free tier available)

2. **Docker Setup**:
   ```bash
   docker build -t taskmaster-pro .
   docker run -d -p 5000:5000 --env-file .env taskmaster-pro
   ```

### Environment Variables

| Variable       | Required | Default            | Description             |
| -------------- | -------- | ------------------ | ----------------------- |
| `FLASK_ENV`    | Yes      | `development`      | Runtime environment     |
| `SECRET_KEY`   | Yes      | -                  | Flask secret key        |
| `DATABASE_URL` | No       | `sqlite:///app.db` | Database connection URL |
| `MAIL_SERVER`  | No       | -                  | SMTP server for emails  |

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Maintainer: Bereket honelign
Email: berekethonelign@gmail.com
Issue Tracker: [GitHub Issues](https://github.com/bereket-7/TaskMasterPro/issues)
````
