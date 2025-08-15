from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import sys
import os

app = Flask(__name__)
CORS(app)  # Enable CORS to allow cross-origin requests

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    code = data.get('script', '')

    try:
        # Write the code to a temporary file
        with open('temp.py', 'w') as f:
            f.write(code)

        # Execute the code using subprocess
        result = subprocess.run(
            [sys.executable, 'temp.py'],
            capture_output=True,
            text=True,
            timeout=5  # Timeout after 5 seconds
        )

        # Return the output or error
        if result.stdout:
            return jsonify({'output': result.stdout})
        elif result.stderr:
            return jsonify({'error': result.stderr})
        else:
            return jsonify({'error': 'No output produced.'})
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Execution timed out.'})
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        # Clean up the temporary file
        if os.path.exists('temp.py'):
            os.remove('temp.py')

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run on a different port than the code generation server