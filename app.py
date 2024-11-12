from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
import os
import io

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Function to get the response from the Gemini model
def get_gemini_response(input_text, image_data, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    try:
        response = model.generate_content([input_text, image_data[0], prompt])
        return {"response": response.text}  # Return response as JSON
    except Exception as e:
        print("Error fetching response:", e)
        return {"error": "Unexpected response format"}  # Return error message as JSON

# Function to prepare the image data for API
def prepare_image_data(image_file):
    if image_file:
        bytes_data = image_file.read()
        return [
            {
                "mime_type": image_file.mimetype,
                "data": bytes_data
            }
        ]
    return None

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the input prompt and uploaded image
        input_text = request.form.get("input_prompt")
        uploaded_file = request.files.get("uploaded_image")
        
        if not uploaded_file or not input_text:
            flash("Please provide both an input prompt and an image.", "warning")
            return redirect(url_for("index"))

        # Process the image for Gemini API
        image_data = prepare_image_data(uploaded_file)
        
        # Define the invoice-related prompt for the Gemini model
        gemini_prompt = """
            You are an expert in understanding invoices.
            You will receive input images as invoices &
            you will have to answer questions based on the input image.
            """
        
        # Get response from Gemini model
        response = get_gemini_response(gemini_prompt, image_data, input_text)
        return jsonify(response)  # Return response as JSON for front-end handling

    return render_template("index.html", response=None)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
