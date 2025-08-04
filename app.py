import os
from flask import Flask, render_template, request, send_file
import pandas as pd
from io import BytesIO
from xhtml2pdf import pisa
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load OpenAI API key from .env or environment
client = OpenAI(api_key="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")

def generate_outreach_message(row):
    # Dynamically create a message based on available columns
    parts = []
    for col, val in row.items():
        if pd.notna(val):
            parts.append(f"{col.replace('_', ' ').capitalize()}: {val}")
    context = "\n".join(parts)

    prompt = (
        f"Write a personalized, concise outreach message based on the following details:\n{context}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[OpenAI Error: {str(e)}]"

def generate_pdf(records):
    html = "<h1>Lead Outreach Messages</h1><ul>"
    for i, row in enumerate(records, 1):
        html += f"<li><strong>{i}.</strong><br>"
        for key, value in row.items():
            if key != "message":
                html += f"{key.capitalize()}: {value}<br>"
        html += f"<strong>Message:</strong> {row['message']}</li><br><br>"
    html += "</ul>"

    pdf = BytesIO()
    pisa.CreatePDF(BytesIO(html.encode("utf-8")), dest=pdf)
    pdf.seek(0)
    return pdf

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("csv_file")
        if not file or not file.filename.endswith(".csv"):
            return "Please upload a valid CSV file.", 400

        try:
            df = pd.read_csv(file, encoding="utf-8", skip_blank_lines=True)
        except pd.errors.ParserError:
            try:
                df = pd.read_csv(file, delimiter=";", encoding="utf-8")
            except Exception as e:
                return f"CSV Read Error: {str(e)}", 500
        except Exception as e:
            return f"CSV Read Error: {str(e)}", 500

        output_data = []
        for _, row in df.iterrows():
            row_data = row.to_dict()
            row_data["message"] = generate_outreach_message(row_data)
            output_data.append(row_data)

        pdf = generate_pdf(output_data)
        return send_file(pdf, as_attachment=True, download_name="Outreach_Messages.pdf", mimetype="application/pdf")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)