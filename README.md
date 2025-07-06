# 📝 Smart ToDo Web App by Rupali

Welcome to **Smart ToDo**, a powerful productivity-focused web app designed to help users manage tasks intelligently, stay organized, and boost efficiency. Built using **Flask (Python)** and **HTML/CSS with Jinja2 templating**, this app goes beyond traditional ToDo lists with smart features and elegant design.

---

## 🚀 Features

### 🔹 Core Features
- ✅ **Add, Update, and Delete tasks** in real-time.
- ✅ **Mark tasks as complete** and manage them effortlessly.
- ✅ **Deadline support** with date pickers.
- ✅ Simple and clean UI using **Jinja2 templates** and **HTML/CSS**.

---

### 💡 Unique & Interview-Worthy Features

#### 🔮 Smart Scheduler
> Calculates how many hours/day you need to finish a task before its deadline.
- Users enter estimated effort (e.g., 10 hours), and the app auto-schedules daily effort.
- Provides alerts if task pace is too slow.
- 🔧 *Tech used*: Python logic + datetime handling.

#### 🧠 AI Task Categorization (Coming Soon)
> Auto-categorizes tasks (e.g., "Buy milk" → Personal, "Prepare DSA Sheet" → Study)
- NLP-based suggestions (OpenAI API/Fine-tuned models)

#### 🏆 Productivity Gamification
> Turns productivity into a game 🎮
- Earn points for completing tasks
- Streak system for consecutive task completions
- Rank levels: Beginner → Master Planner 💼

#### 📊 Analytics Dashboard
> Visualize your productivity with graphs:
- Task completion trends
- Time allocation across categories
- 🔧 *Tech used*: Flask + Chart.js

#### 🎙️ Voice Task Input (Planned)
> Use speech to add tasks via **Web Speech API**
- “Add ‘Call mom’ for tomorrow” → Done!

#### 🎨 Live Theme Customizer
> Personalize your ToDo app’s look:
- Choose color palettes
- Save preferences per user

---

## 🛠 Tech Stack

| Tech         | Role                           |
|--------------|--------------------------------|
| Python       | Backend logic                  |
| Flask        | Web framework (routing, templates) |
| SQLite       | Lightweight local database     |
| HTML/CSS     | UI templating (Jinja2)         |
| Chart.js     | Visual dashboards              |
| JavaScript   | Interactivity + Voice Support (planned) |

---

## 📸 Preview (Screenshots Coming Soon)
_Add screenshots of your app UI here after styling is finalized!_

---

## 🧠 How It Works (Dev Summary)
- Flask handles routing, task CRUD, and smart scheduling logic.
- Tasks stored in SQLite with timestamps and status.
- Frontend rendered using Jinja2 and styled for simplicity + responsiveness.
- Productivity features modularized for easy expansion.

---

## 📦 Setup & Run Locally

```bash
# Clone the repo
git clone https://github.com/Rupali-1394/Todo-web-app.git
cd Todo-web-app

# Set up virtual environment
python -m venv env
source env/bin/activate  # For Windows: .\env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
