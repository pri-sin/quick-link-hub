# Quick Link Hub 🚀

A simple, self-contained personal startpage built with Flask. Manage a dynamic list of your favorite websites from a clean and modern interface.

This single-file web application allows you to add and delete links that are saved to your browser session, giving you a persistent and personalized launchpad for the web.



## Features ✨

-   **Dynamic Link Management**: Add and delete links on the fly without refreshing the page.
-   **Session-Based Persistence**: Your custom link list is saved in your browser session.
-   **Minimalist & Self-Contained**: The entire application (backend and frontend) is in a single Python file.
-   **Clean UI**: A modern, dark-themed interface that's easy on the eyes.

---

## Local Setup & Usage ⚙️

### Prerequisites

-   Python 3.6+

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/pri-sin/quick-link-hub.git]
    cd quick-link-hub
    ```

2.  **Create a `requirements.txt` file** with the following content:
    ```
    Flask
    ```

3.  **Set up a Virtual Environment & Install Dependencies:**
    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install the required package
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    python web_3.py
    ```
    Open your browser and navigate to `http://127.0.0.1:5000`.
