from flask import Flask, render_template, request, jsonify
from main import analyze_resumes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        repo_url = data.get('repository_url')
        experience_level = data.get('experience_level', 'mid')  # Default to mid-level
        keywords = data.get('keywords', [])  # Optional keywords filter
        
        if not repo_url:
            return jsonify({'success': False, 'error': 'No repository URL provided'})
        
        result = analyze_resumes(repo_url, experience_level, keywords)
        return jsonify({'success': True, 'result': str(result)})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
