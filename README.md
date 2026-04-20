# Expense Tracker (Flask + MySQL)

A simple and clean web-based Expense Tracker built using **Flask** and **MySQL**.
This project allows users to manage their daily expenses with full CRUD functionality and a user-friendly interface.

---

## Features

* Add new expenses
* View all expenses
* Update existing expenses
* Delete expenses
* View total expense summary
* Clean and responsive UI using custom CSS

---

## Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Flask (Python)
* **Database:** MySQL
* **Templating Engine:** Jinja2

---

## Project Structure

```
expense-tracker/
│
├── app.py
├── static/
│   └── style.css
├── templates/
│   ├── home.html
│   ├── add.html
│   ├── view.html
│   ├── update.html
│   ├── delete.html
│   └── total.html
```

---

## Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

### 2. Install dependencies

```
pip install flask flask-mysqldb
```

### 3. Setup MySQL Database

Create a database named `ET` and run:

```sql
CREATE TABLE expensetracker1 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount FLOAT NOT NULL,
    category VARCHAR(50),
    date DATE
);
```

### 4. Configure Database in `app.py`

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your-username'
app.config['MYSQL_PASSWORD'] = 'your-password'
app.config['MYSQL_DB'] = 'ET'
```

### 5. Run the application

```
python app.py
```

---

## Usage

* Open browser and go to: `http://127.0.0.1:5000/`
* Navigate through options:

  * Add Expense
  * View Expenses
  * Update Expense
  * Delete Expense
  * Total Expense

---


## 🔮 Future Improvements

* User authentication (login/signup)
* Category-wise expense charts
* Date filtering (weekly/monthly reports)
* Export data to CSV/PDF
* React frontend integration

---

## Author

**Ashi Sinha**

---

## Acknowledgements

This project was built as part of learning full-stack development using Flask and MySQL.

---

## Note

This is a beginner-friendly project and can be extended into a full-fledged finance management system.
