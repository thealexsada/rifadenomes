# Rifa de Nomes

#### Video Demo:[ Alex Sada's CS50x Final Project Demo - Rifa de Nomes ](https://youtu.be/C6YYP9Bi650)
#### Application URL: [https://escolhanomes.up.railway.app/](https://escolhanomes.up.railway.app/)  

#### Description:  

Rifa de Nomes is a Flask-based web application created as part of my CS50x final project. This project was inspired by the need for a virtual celebration to involve my family in Brazil in a special baby name reveal event for my baby boy, while I am based in New Zealand. The app enables friends and family to participate in a raffle by selecting names from a pre-defined list.  

The main idea is simple: participants select a name they believe we've chosen for our baby, register their choice along with their own name, and submit their guess. Once the results are revealed, the winner is announced and awarded a special prize.  

The app also includes an admin API endpoint to display all registrants and their chosen names in JSON format for administrative purposes.

---

## Project Structure  

### Files and Directories  

- **`app.py`**: The main Flask application that handles all backend functionality, including routes for registering and displaying results.  
- **`templates/`**: Contains the HTML templates rendered by Flask using Jinja:  
  - **`index.html`**: Displays the list of names and the registration form.  
  - **`failure.html`**: Displays error messages when invalid inputs are submitted.  
- **`static/`**: Reserved for static files (e.g., CSS, JavaScript). This project doesn’t include such files but the directory is ready for future use.  
- **`tmp/`**: Contains the SQLite database file (`rifadenomes.db`) that stores registrant details.  
- **`requirements.txt`**: Lists the Python dependencies required to run the app.

---

## Key Features  

1. **Name Registration**: Participants choose a name from the provided list, enter their own name, and submit their selection.  
2. **Privacy by Design**: The app ensures vote privacy; participants cannot see the choices of others unless they have access to the admin API.  
3. **Admin API**: Administrators can view a JSON list of all registrants and their selected names via the `/admin/registrants` endpoint.  

---

## Technical Details  

### Database  
The app uses SQLite for storing registrant data securely. The database is initialized automatically when the app is first launched, ensuring it is ready for use without manual setup. When hosted on Railway, the database is configured with a persistent volume to maintain data integrity across deployments.  

### Hosting  
The project is hosted on [Railway](https://railway.app), which provides free hosting and storage solutions. This setup guarantees data persistence and a seamless user experience.  

### Development Tools  
- **Python 3.10**: Used for implementing the core functionality.  
- **Flask**: A lightweight web framework for building the app.  
- **Jinja**: For rendering dynamic HTML templates.  
- **Visual Studio Code**: My primary code editor for development.  
- **Git**: For version control, with the repository hosted on GitHub.  

---

## How It Works  

1. Users visit the app and see a list of names.  
2. They select one or more names from the list, enter their own name, and submit their choice.  
3. The app ensures vote privacy by not displaying other participants’ choices.  
4. The admin can use the `/admin/registrants` API endpoint to view the list of registrants and their selected names in JSON format.  

---

## Design Choices  

1. **Vote Privacy**: Ensuring participants cannot see other votes was a core design choice to maintain fairness and privacy. Only administrators can access the full list of registrants via the admin API.  
2. **Data Persistence**: Leveraging Railway’s volume persistence ensures that no data is lost during app redeployments.  
3. **Validation**: The app validates user input to ensure only names from the predefined list are accepted. Invalid or duplicate submissions are flagged, and the user is notified with an appropriate error message.  

---

## Repository and Contact  

- **GitHub Repository**: [Rifa de Nomes](https://github.com/thealexsada/rifadenomes)  
- **Author**: Alex Sada  
  - Based in Auckland, New Zealand (originally from Monterrey, Mexico).  
- **Submission Date**: December 30, 2024  

Thank you for taking the time to review my project! 🎉  
