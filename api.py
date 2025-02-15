from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route to handle requests to "/"
@app.route('/')
def home():
    return "Welcome to the API! Use /run or /read endpoints."

@app.route('/run', methods=['POST','GET'])
def run_task():
    task_description = request.args.get('task')
    # Implement logic to parse and execute tasks here.
    return jsonify({"status": "success", "message": "Task executed"}), 200

@app.route('/read', methods=['GET'])
def read_file():
    file_path = request.args.get('path')
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content, 200
    except FileNotFoundError:
        return "", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
