# Task Manager using Python 🗂️

A simple command-line based Task Manager built in Python that allows users to manage tasks with full CRUD operations, mark tasks as completed, view pending tasks, and sort tasks based on priority.

---

## 📋 Features

- Create new tasks
- Read and display existing tasks
- Update task attributes (title, deadline, priority)
- Delete tasks
- Mark tasks as completed
- View only pending tasks
- Sort tasks by:
  - **Priority** (High → Low)
  - **Deadline** (Recent first)

---

## 🏃‍♂️ How to Run

From your terminal:

```bash
python main.py
````

Make sure you're running this from the root directory of the project.

---

## 📂 Required Setup

This project requires a `task.json` file in the **same directory** as `main.py`.

Example format of `task.json`:

```json
[
    {
        "id": 1,
        "title": "Finish Python project",
        "deadline": "2025-05-13",
        "priority": "Low",
        "completed": true
    }
]
```
---

## 🐍 Python Requirements

* Python 3.x (Tested on latest version as of install)
* No external packages required – uses only built-in modules:

  * `datetime`
  * `json`
  * `os`

---

## ✍️ Author

> Developed and maintained with ❤️ by [Minhaj AP](https://github.com/minhaj-ap)  

[![GitHub](https://img.shields.io/badge/GitHub-Minhaj%20AP-181717?style=for-the-badge&logo=github)](https://github.com/minhaj-ap)

---

---

## 📌 Notes

* Dates should be entered in `YYYY-MM-DD` format.
* Make sure `task.json` has read/write permission for data persistence.

---
