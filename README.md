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

You can upload a CSV with any number of columns.

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

```

### 2.  Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create .env File

```bash
OPENAI_API_KEY=your_openai_key_here
```

## 🧑‍💻 Running the App
Once everything is set up, run the Flask app:

```bash
python app.py
```
Open your browser and go to http://localhost:5000

## 📄 Output

After uploading your CSV:

The app reads the file using pandas.

It generates personalized messages using OpenAI GPT-4o.

All content is compiled into a styled PDF.

You’ll receive a file named Outreach_Messages.pdf.

## ❓ Common Errors & Fixes
OpenAI Error: 429 – Quota Exceeded
You’ve exceeded your API quota. Check OpenAI billing or upgrade your plan.

CSV Parser Errors
Ensure your file is comma-separated. If not, try saving with proper delimiters from Excel.

No File Uploaded / Wrong Format
Make sure the file is .csv and not empty.

## 🏗 Future Improvements
Allow user-defined message templates

Add Excel support

Include preview before generating PDF

Multi-language support
