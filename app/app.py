from flask import Flask, render_template, request, send_file
from io import BytesIO
from reportlab.pdfgen import canvas

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    course = request.form["course"]
    date = request.form["date"]

    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(300, 750, "Certificate of Completion")
    c.setFont("Helvetica", 18)
    c.drawCentredString(300, 700, f"This certificate is proudly presented to")
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(300, 650, name)
    c.setFont("Helvetica", 16)
    c.drawCentredString(300, 600, f"For completing: {course}")
    c.drawCentredString(300, 560, f"Date: {date}")
    c.showPage()
    c.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="certificate.pdf", mimetype="application/pdf")

if __name__ == "__main__":
    app.run(debug=True)
