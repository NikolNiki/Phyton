from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

SENDER_EMAIL = "nikinikol1610@icloud.com"
SENDER_PASSWORD = "kzhg-nygs-jzsn-sbzj"

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        name = request.form.get("name").strip()
        text = request.form.get("text").strip()
        receiver = request.form.get("email").strip()

        length = len(text)

        html_message = render_template(
            "string.html",
            name=name,
            text=text,
            length=length
        )

        msg = MIMEMultipart("alternative")
        msg["Subject"] = SENDER_EMAIL
        msg["To"] = receiver

        msg.attach(MIMEText(html_message, "html"))

        try:
            server = smtplib.SMTP_SSL(
                "smtp.icloud.com",
                465
            )


            server.login(SENDER_EMAIL, SENDER_PASSWORD)

            server.sendmail(
                SENDER_EMAIL,
                receiver,
                msg.as_string()
            )

            server.quit()

            return f"""
            <h2>Лист успішно відправлено на {receiver}</h2>
            """

        except Exception as e:
            return f"Помилка: {e}"

    return """
    <h2>Відправка електронного листа</h2>

    <form method="POST">
        
        <p>Ім`я:</p>
        <input type="text" name="name" required>

        <p>Строка:</p>
        <input type="text" name="text" required>

        <p>Email:</p>
        <input type="email" name="email" required>

        <br><br>

        <button type="submit">
            Відправити
        </button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)