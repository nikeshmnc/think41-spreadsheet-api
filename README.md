# Think41 Spreadsheet API

This project is a **Flask-based REST API** for managing spreadsheet cells, dependencies, precedents, and recalculation order using topological sort, built as part of the **Think41 Full Stack AI interview preparation**.

---

## 🚀 Features

✅ Retrieve **dependents** of a specific cell  
✅ Retrieve **precedents** of a specific cell  
✅ Retrieve **recalculation order** using topological sorting  
✅ Clear, RESTful structure for easy extension

---

## 🛠️ Tech Stack

- **Python** with **Flask**
- JSON-based REST API
- Can be extended with SQLite/PostgreSQL for persistent storage

---

## 📦 Installation

1️⃣ Clone the repository:
```bash
git clone https://github.com/nikeshmnc/think41-spreadsheet-api.git
cd think41-spreadsheet-api
```

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Server

```bash
python app.py
```

Server will start at:
```
http://127.0.0.1:5000/
```

---

## 🧪 API Endpoints

### ✅ Check Server Status
**GET /**  
**Response:** `"Think41 Spreadsheet API is running."`

---

### ✅ Get Cell Dependents
**GET** `/spreadsheets/<spreadsheet_id>/cells/<cell_id>/dependents`

📌 **Example:**
```
http://127.0.0.1:5000/spreadsheets/1/cells/A1/dependents
```

---

### ✅ Get Cell Precedents
**GET** `/spreadsheets/<spreadsheet_id>/cells/<cell_id>/precedents`

📌 **Example:**
```
http://127.0.0.1:5000/spreadsheets/1/cells/A1/precedents
```

---

### ✅ Get Recalculation Order
**GET** `/spreadsheets/<spreadsheet_id>/recalculation-order`

📌 **Example:**
```
http://127.0.0.1:5000/spreadsheets/1/recalculation-order
```

---

## 🤝 Contributing

This project is built for learning and demonstration purposes during the Think41 Full Stack AI interview. Feel free to fork and build upon it.

---

## 📜 License

MIT License.

---

**Built with ❤️ by Nikhesh Meduri.**
