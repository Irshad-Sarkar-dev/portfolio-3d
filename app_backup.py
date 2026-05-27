from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')

PORTFOLIO_DATA = {
    "name": "Your Name",
    "title": "Developer & Problem Solver",
    "bio": "Building intelligent solutions with code. Passionate about AI/ML, data analysis, and creating seamless user experiences.",
    "email": "your.email@example.com",
    "github": "https://github.com/yourusername",
    "linkedin": "https://linkedin.com/in/yourusername",
    "projects": [
        {
            "id": 1,
            "title": "Question Pattern Predictor",
            "description": "An intelligent system that analyzes educational content and predicts question patterns with probability calculations.",
            "tags": ["Python", "ML", "Data Analysis", "NLP"],
            "github": "https://github.com/yourusername/question-predictor",
        },
        {
            "id": 2,
            "title": "PDF Question Extractor",
            "description": "Extract and analyze questions from PDF documents automatically.",
            "tags": ["Python", "PDF Processing"],
            "github": "https://github.com/yourusername/pdf-extractor",
        }
    ],
    "skills": ["Python", "JavaScript", "Machine Learning", "Data Analysis", "Web Development", "Flask", "Three.js"]
}

@app.route('/')
def index():
    return render_template('index.html', data=PORTFOLIO_DATA)

@app.route('/api/portfolio')
def api_portfolio():
    return jsonify(PORTFOLIO_DATA)

if __name__ == '__main__':
    print("Portfolio Website running at http://localhost:5000")
    app.run(debug=True, host='localhost', port=5000)
