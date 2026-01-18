from flask import Flask, render_template, request

app = Flask(__name__)

MENU = {
    "ku": [
        {"name": "پیتزا گوشت", "price": 6000},
        {"name": "پیتزا مریشک", "price": 5000},
        {"name": "برگر گوشت", "price": 3000},
        {"name": "برگر مریشک", "price": 2000},
        {"name": "شاورما گوشت", "price": 3500},
        {"name": "شاورما مریشک", "price": 2500},
        {"name": "فلافل", "price": 1000},
    ],
    "ar": [
        {"name": "بيتزا لحم", "price": 6000},
        {"name": "بيتزا دجاج", "price": 5000},
        {"name": "برغر لحم", "price": 3000},
        {"name": "برغر دجاج", "price": 2000},
        {"name": "شاورما لحم", "price": 3500},
        {"name": "شاورما دجاج", "price": 2500},
        {"name": "فلافل", "price": 1000},
    ]
}

TEXT = {
    "ku": {
        "title": "Sandawich Shexa",
        "menu": "لیستی خواردنەکان",
        "total": "کۆی گشتی",
        "order": "ناردنی داواکاری",
        "switch": "العربية"
    },
    "ar": {
        "title": "Sandawich Shexa",
        "menu": "قائمة الطعام",
        "total": "المجموع",
        "order": "إرسال الطلب",
        "switch": "كردي"
    }
}

@app.route("/")
def index():
    lang = request.args.get("lang", "ku")
    return render_template(
        "index.html",
        menu=MENU[lang],
        text=TEXT[lang],
        lang=lang
    )

if __name__ == "__main__":
    app.run(debug=True)