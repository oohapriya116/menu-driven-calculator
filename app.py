from flask import Flask, request, jsonify

app = Flask(__name__)


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

@app.route('/calculate', methods=['POST'])
def calculate():
    

    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Missing request body. Please provide JSON data."}), 400
        
    operation = data.get('operation')
    
   
    try:
        a = float(data.get('a'))
        b = float(data.get('b'))
    except (TypeError, ValueError):
        return jsonify({"error": "Inputs 'a' and 'b' must be valid numbers."}), 400

    if operation == 'add':
        result = add(a, b)
        return jsonify({"operation": "addition", "a": a, "b": b, "result": result}), 200
        
    elif operation == 'subtract':
        result = subtract(a, b)
        return jsonify({"operation": "subtraction", "a": a, "b": b, "result": result}), 200
        
    else:
        return jsonify({"error": "Invalid choice. Operation must be 'add' or 'subtract'."}), 400

if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port=5000, debug=True)
