from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import RobertaTokenizer, T5ForConditionalGeneration
import torch  # Add this import

app = Flask(__name__)
CORS(app)  # Allow CORS for communication with the frontend

# Path to your fine-tuned model directory
MODEL_PATH = r"C:\Users\srima\Downloads\S4\Deep Learning\Project\Abhi_Project\Extracted_Datasets\User_Interface_Design\codet5_base_finetuned"

try:
    print("Loading tokenizer...")
    TOKENIZER = RobertaTokenizer.from_pretrained(MODEL_PATH)
    print("Tokenizer loaded successfully")
    
    print("Loading model...")
    model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
    model.eval()
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    TOKENIZER = None

def generate_code(prompt):
    if model is None or TOKENIZER is None:
        return "Error: Model not loaded properly."
    
    try:
        # Tokenize the input prompt using RobertaTokenizer
        print(f"Tokenizing prompt: {prompt}")
        inputs = TOKENIZER(prompt, return_tensors="pt", max_length=512, truncation=True)
        print("Tokenization successful")
        
        # Generate code using the T5 model
        print("Generating code...")
        with torch.no_grad():
            output_ids = model.generate(
                inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_length=512,
                num_beams=4,
                early_stopping=True
            )
        print("Code generation successful")
        
        # Decode the generated output using RobertaTokenizer
        generated_code = TOKENIZER.decode(output_ids[0], skip_special_tokens=True)
        print(f"Generated code: {generated_code}")
        return generated_code
    
    except Exception as e:
        print(f"Error generating code: {str(e)}")
        return f"Error generating code: {str(e)}"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    generated_code = generate_code(prompt)
    return jsonify({"response": generated_code})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)