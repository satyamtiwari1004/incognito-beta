# 🕵️‍♂️ Incognito

Welcome to Incognito, a user-friendly platform designed to help individuals become cybersecurity experts with guidance from professionals. Incognito features easy navigation, a portfolio builder for creating and sharing portfolios in under 5 minutes, and global courses that users can utilize to learn and track their progress.

![Incognito Screenshot](https://satyam-portfolio-24.s3.ap-south-1.amazonaws.com/img/projects/incognito-mockup.png)

## 🌟 Features

- **Professional Guidance:** Learn from cybersecurity experts.
- **Easy Navigation:** User-friendly interface for a seamless experience.
- **Portfolio Builder:** Create and share your portfolio in under 5 minutes.
- **Global Courses:** Access a wide range of courses and track your learning progress.

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Deployment:** AWS (EC2, S3, RDS)

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip
- virtualenv

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/incognito.git
   cd incognito
   
2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  
   
3. **Install the dependencies:**

   ```bash 
   pip install -r requirements.txt

4. **Set up the .env file:**

   Create a .env file in the root directory of the project and add the following variables with your specific details:

   ```bash 
   SECRET_KEY=your_secret_key
   DATABASE_NAME=your_database_name
   DATABASE_USER=your_database_user
   DATABASE_PASSWORD=your_database_password
   DATABASE_HOST=your_database_host
   DATABASE_PORT=your_database_port
   EMAIL_HOST=your_email_host
   EMAIL_PORT=your_email_port
   EMAIL_HOST_USER=your_email_user
   EMAIL_HOST_PASSWORD=your_email_password
   
5. **Apply the migrations:**

   ```bash
   python manage.py migrate

6. **Create a superuser (optional, for accessing the Django admin interface):**

   ```bash
   python manage.py createsuperuser

7. **Run the development server:**

   ```bash
   python manage.py runserver

8. **Access the application:**
Open your web browser and go to http://127.0.0.1:8000/ to view the application.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

1.	Fork the repository
2.	Create your feature branch (git checkout -b feature/your-feature)
3.	Commit your changes (git commit -am 'Add some feature')
4.	Push to the branch (git push origin feature/your-feature)
5.	Create a new Pull Request
	
## License   

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE file for details.
