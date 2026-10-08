from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>فصل الصوت - Kim Model</title>
        <style>
            body { font-family: Tahoma, sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; text-align: center; }
            .card { background: #1e293b; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); max-width: 400px; margin: auto; }
            input, button { width: 100%; padding: 12px; margin-top: 15px; border-radius: 8px; border: none; font-size: 16px; box-sizing: border-box; }
            button { background: #3b82f6; color: white; cursor: pointer; font-weight: bold; }
            button:hover { background: #2563eb; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>تطبيق فصل الصوت النقي</h2>
            <p>اختر ملف الصوت لمعالجته عبر نموذج Kim</p>
            <input type="file" id="audioFile" accept="audio/*">
            <button onclick="alert('جاري المعالجة وعزل الصوت...')">بدء الفصل الآن</button>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
