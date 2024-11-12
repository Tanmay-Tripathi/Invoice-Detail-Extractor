# Gemini Image Analysis for Invoices - Flask Web Application

Welcome to the **Gemini Image Analysis for Invoices** project! This web application allows users to upload an image of an invoice and ask questions related to the invoice. The app processes the image using the **Gemini AI Model** from Google, extracting valuable insights and returning a response based on the input query.

## Features

- **Invoice Image Upload**: Allows users to upload images in JPG, JPEG, or PNG format.
- **AI-Powered Query Handling**: Users can ask specific questions related to the invoice, and the Gemini model processes the image to provide relevant answers.
- **Beautiful User Interface**: A clean and modern UI built with **Flask**, **Bootstrap**, and custom CSS animations.
- **Responsive Design**: Works seamlessly across desktops and mobile devices.
  
## Tech Stack

- **Backend**: Flask (Python Web Framework)
- **AI Model**: Google Gemini AI Model for text generation
- **Frontend**: HTML, CSS (with Bootstrap for styling)
- **Image Processing**: Python Image Library (PIL)
- **Environment Management**: `.env` file for API keys using `dotenv`
- **Deployment**: Localhost for development

## Setup Instructions

Follow these steps to get the project up and running locally:

### Prerequisites

- Python 3.7 or higher
- Google API Key for accessing Gemini AI (set in the `.env` file)

### How it works

- Upload Image: The user uploads an image of an invoice.
- Input Query: The user enters a text query about the uploaded invoice.
- AI Processing: The app sends the image and query to the Google Gemini API for analysis.
- Response: The AI model processes the image and returns an appropriate response to the user.

### Clone the Repository

```bash
git clone https://github.com/your-username/gemini-image-analysis.git
cd gemini-image-analysis
