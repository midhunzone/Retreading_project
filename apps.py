from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html_content = open('templates/index.html').read()  # Ensure the path to your HTML file is correct
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
