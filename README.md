 ## Flask Application Design for A tutor to teach me calculus at the AP Calculus BC level over 6 months.

### HTML Files

**1. index.html**
- This is the main HTML file that will serve as the landing page for the application.
- It will contain the necessary HTML elements to display the content of the application, such as headings, paragraphs, and links.
- It will also include a form to allow users to input their information and submit it to the application.

**2. results.html**
- This HTML file will display the results of the user's input.
- It will contain the necessary HTML elements to display the results, such as headings, paragraphs, and tables.

### Routes

**1. @app.route('/')**
- This route will handle the GET request for the main page of the application.
- It will render the index.html file.

**2. @app.route('/results', methods=['POST'])**
- This route will handle the POST request when the user submits the form on the index.html page.
- It will process the user's input and generate the results.
- It will then render the results.html file, displaying the results to the user.