# 🤖 AI Outreach Message Generator

This project is a user-friendly Flask web application that generates **personalized outreach messages** using OpenAI's GPT-4o model. It allows users to upload a `.csv` file, and for each row in the CSV, a tailored message is created based on the available data and compiled into a downloadable **PDF file**.

---

## 📌 Key Features

- Upload any `.csv` file (no strict column requirements)
- Automatically parses rows and generates a message per entry
- Uses OpenAI GPT-4o to generate concise, context-aware outreach messages
- Outputs a downloadable PDF with messages and original data
- Clean and modern UI built using Bootstrap

---

## 🚀 How It Works

1. User visits the web page.
2. Uploads a CSV file with business or lead data.
3. The app reads each row and sends it to OpenAI’s GPT-4o model with a prompt to generate a personalized message.
4. It combines all messages and data into a styled PDF.
5. The user can download the resulting PDF file.

---

## 🧪 Example CSV File Format

You can upload a CSV with any number of columns. Example structure:

account,sector,year_established,revenue,employees,office_location,subsidiary_of
Acme Corp,Manufacturing,1995,$50M,500,Chicago,Global Holdings
DataWave Inc,IT Services,2010,$25M,200,New York,
BrightLogix,Healthcare,2005,$40M,350,Boston,MedTech Group
---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, Bootstrap
- **AI Integration:** OpenAI GPT-4o via `openai` Python SDK
- **PDF Generator:** xhtml2pdf
- **CSV Parser:** pandas
- **Environment Handling:** python-dotenv

---

## 📁 Project Structure

lead-bot-app/
├── app.py # Main Flask app
├── templates/
│ └── index.html # Frontend form UI
├── .env # Your OpenAI API key (not to be committed)
├── requirements.txt # Python dependencies
└── README.md # Documentation


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/lead-bot-app.git
cd lead-bot-app

---
