# 🌍 CO₂ Emissions Analysis App

An interactive **Streamlit web app** for exploring CO₂ emissions across African countries.  
This project uses a reduced sample dataset (`metadata_small.csv`) for faster loading and smoother analysis.

---

## ✨ Features
- 📊 **Interactive Data Exploration** – filter and view CO₂ emissions by country, sector, and year.
- 📈 **Visual Insights** – dynamic charts to understand trends and top emitters.
- 🔎 **Search & Compare** – quickly find country-specific details and compare multiple countries.

---

## 📂 Project Structure
Frameworks_Assignment/
├─ raw_data/ # (Optional) original large dataset
├─ metadata_small.csv # cleaned & reduced dataset for the app
├─ app.py # Streamlit web application
├─ analysis.ipynb # Jupyter analysis notebook
└─ README.md # this file

yaml
Copy code

---

## ⚡ Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/frameworks-assignment.git
cd frameworks-assignment
2️⃣ Install dependencies
(Use a virtual environment if possible)

bash
Copy code
pip install -r requirements.txt
3️⃣ Run the app
bash
Copy code
streamlit run app.py
Then open your browser and go to 👉 http://localhost:8501

🛠️ Tech Stack
Tool	Purpose
Python 3	Programming language
Pandas	Data manipulation
Matplotlib / Seaborn	Visualizations
Streamlit	Web app framework

📊 Dataset
Name: metadata_small.csv

Source: Reduced sample from the original CORD-19 metadata dataset.

Why Reduced? To improve performance on personal machines while retaining analytical value.

💡 Notes
The large dataset is optional and stored in raw_data/ (ignored in .gitignore for GitHub).

Always load metadata_small.csv in your code for smooth performance.

👩‍💻 Author
Faith Jaher
Data Science & Writing Enthusiast • Girls' Education Activist

“Small steps lead to big impact.”

📜 License
This project is licensed under the MIT License – feel free to use and modify.

markdown
Copy code

✅ **How to use:**  
1. In VS Code, right-click your project folder → **New File** → name it `README.md`.  
2. Paste the ENTIRE block above.  
3. Save (`Ctrl+S` / `Cmd+S`).  
GitHub will render this beautifully with emojis, headings, and tables.