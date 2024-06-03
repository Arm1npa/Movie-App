# MovieApp

MovieApp is a web application built with Django and React that allows users to browse, search, and watch trailers for movies and TV shows. The app utilizes The Movie Database (TMDb) API to fetch and display data.

## Features

- **Trending Movies**: View a list of currently trending movies.
- **Movie Section**: Browse movies and filter them by genre.
- **TV Show Section**: Browse TV shows and filter them by genre.
- **Search Functionality**: Search for movies and TV shows by title.
- **Trailers**: Watch trailers for each movie and TV show.
- **Details**: View short descriptions and cast information for movies and TV shows.

## Installation

### Prerequisites

- Python 3.x
- Node.js
- npm or yarn
- Django
- React

### Backend Setup (Django)

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/MovieApp.git
    cd MovieApp
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your TMDb API key:**

    - Create a `.env` file in the root directory of the project.
    - Add your TMDb API key to the `.env` file:

      ```plaintext
      API_KEY=your_api_key_here
      ```

5. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

### Frontend Setup (React)

1. **Navigate to the frontend directory:**

    ```bash
    cd frontend
    ```

2. **Install the required Node packages:**

    ```bash
    npm install  # or `yarn install`
    ```

3. **Start the React development server:**

    ```bash
    npm start  # or `yarn start`
    ```

## Usage

1. **Open your web browser and go to:**

    ```
    http://localhost:3000
    ```

2. **Explore the app:**
    - Browse through trending movies on the homepage.
    - Navigate to the Movies section to filter movies by genre.
    - Navigate to the TV Shows section to filter TV shows by genre.
    - Use the search bar to find specific movies or TV shows.
    - Click on any movie or TV show to view its trailer, description, and cast information.

## Project Structure

- **backend/**: Contains the Django backend code.
- **frontend/**: Contains the React frontend code.
- **.env**: Environment variables file for sensitive data like API keys.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License.

---

Feel free to reach out if you have any questions or need further assistance. Enjoy using MovieApp!

---

### Acknowledgements

- [TMDb API](https://www.themoviedb.org/documentation/api) for providing movie and TV show data.
- 
