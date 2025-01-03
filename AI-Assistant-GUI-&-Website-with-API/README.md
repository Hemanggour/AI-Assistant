# AI Assistant Project

This project is an AI Assistant that can perform various tasks such as opening applications, playing music, fetching news, and more. It consists of a server-side component and a client-side GUI.

## Project Structure

    -AI-Assistant-GUI-&-Website-With-API
        - requirements.txt
        - README.txt

        - client/
            - apps.py
            - client.py
            - getPath.py
            - history.txt
            - log.json
            - main.py
            - MusicLib.py
            - parseCommand.py

        - server/
            - APIs.json
            - APIs.py
            - authentication.py
            - ChatAI.py
            - ChatHistory.txt
            - database.py
            - getPath.py
            - news.py
            - newsTopic.py
            - registration.py
            - wiki.py
            - youtube.py
            - search.py
            - server.py
            - static/
                - css/
                    - styles.css
                - js/
                - media/
            - templates/
                - base.html
                - chat.html

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- MySQL
- Other dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Hemanggour/AI-Assistant/tree/main/AI-Assistant-GUI-%26-Website-with-API
    cd AI-Assistant-GUI-&-Website-with-API
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up the MySQL database and update the connection details in [database.py](/AI-Assistant-GUI-&-Website-with-API/server/database.py).

4. Add your API keys in APIs.json [Get API Key](https://ai.google.dev/gemini-api/docs/api-key).

### Running the Server

To start the server, run the following command from the [server](/AI-Assistant-GUI-&-Website-with-API/server/server.py) directory:
```sh
python server/server.py
```

Running the Client
To start the GUI client, run the following command from the client directory:
```sh
python client/main.py
```
Accessing the Web Interface
After starting the server, open your web browser and go to http://localhost:5000 to access the web interface.

**_Features_**

_Open Applications: Open various applications like Notepad, Calculator, Paint, etc._

_Play Music: Play songs from a predefined music library._

_Fetch News: Get the latest news on various topics._

_Chat with AI: Interact with the AI assistant through a web interface or GUI client._

_User Authentication: Sign up, log in, and manage user accounts._

**_File Descriptions_**

_client/apps.py: Functions to open various applications._

_client/client.py: Functions to send requests to the server._

_client/getPath.py: Utility to get the absolute path of a file._

_client/main.py: GUI client for the AI assistant._

_client/MusicLib.py: Functions to play songs from a music library._

_client/parseCommand.py: Functions to parse user commands._

_server/AI.py: Functions to generate content using AI._

_server/APIs.py: Functions to get API keys from APIs.json._

_server/authentication.py: Functions for user authentication._

_server/ChatAI.py: Functions to handle chat interactions with AI._

_server/database.py: Functions to interact with the MySQL database._

_server/news.py: Functions to fetch news using the News API._

_server/registration.py: Functions for user registration and password management._

_server/search.py: Functions to perform Google searches._

_server/server.py: Flask server to handle API requests and render web pages._

_server/wiki.py: Functions to search Wikipedia._

_server/youtube.py: Functions to search YouTube videos._

## Notes
### This project is currently under development, so some functions might not work or have bugs.
For any issues or contributions, please create a pull request or open an issue on the repository.

## License
### This project is licensed under the MIT License.

### Feel free to customize this README file as per your project's specific details and requirements.