# Code Blog

A Django-based blogging platform name `Code Blog` inspired by Dev.to, where users can publish article,
engage with the community and bookmark their favorite posts.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Support](#⭐️-support)
- [License](#license)

## Features

- **User Authentication:** Users can create accounts, log-in, and log-out. Authorship is associated with user accounts.
- **Create and Edit Posts:** Users can create new posts and edit their existing posts.
- **Commenting:** Users can leave comments on posts.
- **Like and Bookmark:** Users can like and bookmark posts.
- **Dashboard:** Users have a personalized dashboard to manage their posts and view post analytics.
- **Categories:** Posts can be categorized for easy navigation.
- **Search:** Users can search for posts based on titles.
- **Profile Pages:** Each user has a dedicated profile page displaying their posts.
- **Markdown Support**: Write your blog posts using Markdown to add formatting, images, links, and more.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/yourproject.git
    ```

2. Navigate to the project directory:

    ```bash
    cd yourproject
    ```

3. Create a virtual Environment and activate it:
    ```bash
    python -m venv venv

    # Activate the virtual env on linux with
    source venv/bin/activate

    # On Windows
    venv\Scripts\activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Visit [http://localhost:8000/](http://localhost:8000/) to view the application.

9. Visit [http://localhost:8000/admin/](http://localhost:8000/admin/) to log in as the superuser and manage the application, blog posts, categories, and other site content.

**Note:** Using a virtual environment is a good practice to isolate project dependencies and avoid conflicts with other projects.

## Usage

### Create Categories

The first thing after starting and project and creating a superuser is to create categories for the blog post otherwise no new post can be published as every post should belong to a category. To create categories, follow these steps:

1. visit ```http://localhost:8000/admin/```
2. Login with your superuser id and in the admin dashboard, click on ```Categories```
3. Click ```Add Category``` and give it a name. For example, you can create different category based on different coding languages like python, c++, etc.

### Create Your first post
1. Visit ```http://localhost:8000``` and register or login if you havent yet.
2. Click on ```New Post``` in the top navigation.
3. Give your post title, snippet, body (in the body you can use markdown language), post featured image and category.
4. Published your post or you can save it as Draft.

### Next Step

1. Explore blog posts, categories, and user profiles.
2. Setup your profile by visiting settings from the dropdown navigation.
2. Create your first post by clicking ```Create Post```
4. Go to the dashboard to manage your blog posts.
5. You can leave comments on the blog posts, like or bookmark it.

## 🤝 Contributing

Contributions, issues and feature requests are welcome! Any changes are welcome, Please submit an Issue or even better a PR and I'll review :)


## ⭐️ Support

Give a ⭐️  if this project helped you!


## License

[The MIT License](LICENSE)