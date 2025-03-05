# app.py (Flask Backend)
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_material')
def get_material():
    selected_class = request.args.get('class')
    selected_region = request.args.get('region')
    
    # Dummy content - Replace with actual database query or file fetch
    content = f"Study material for Class {selected_class}, {selected_region} region coming soon!"
    return jsonify({"content": content})

if __name__ == '__main__':
    app.run(debug=True)
