# NYC AirBnB Price Analysis

A web application built with Flask to explore New York City's Airbnb pricing trends across neighborhoods, room types, and availability patterns. The analysis is presented through an embedded Jupyter Notebook, giving a clean and interactive way to walk through the data.

---

## What this project does

The app loads a dataset of NYC Airbnb listings and lets you explore the data visually. From the home page, clicking the Jupyter logo takes you directly to the notebook where all the analysis lives — covering price distributions, neighborhood breakdowns, and listing patterns across the city.

---

## Project Structure

```
Data_Analysis/
├── app.py                  # Flask application
├── airbnb_data.csv         # Dataset
├── requirements.txt        # Python dependencies
├── Procfile                # For deployment on Render
└── templates/
    ├── index.html          # Landing page
    └── notebook.html       # Notebook viewer
```

---

## Running it locally

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then start the app:

```bash
python3 app.py
```

Open your browser and go to `http://127.0.0.1:5000`.

---

## Deploying to Render

1. Push the project to GitHub
2. Go to [render.com](https://render.com) and create a new Web Service
3. Connect your GitHub repository
4. Use these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Hit Deploy — your app will be live at `https://yourapp.onrender.com`

---

## Built with

- Python and Flask for the backend
- Pandas for data handling
- HTML and CSS for the frontend
- NYC Airbnb Open Data dataset

---

## About

Built as part of a Python for Data Science course.
