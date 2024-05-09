from flask import Flask, render_template, request
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI API with your API key
openai_api_key = "OPENAI_API_KEY"


# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for generating blog content
@app.route('/generator', methods=['POST'])
def generate():
  if request.method == 'POST':  
    prompt = PromptTemplate.from_template("Generate a blog on title {title}?")
    llm = OpenAI(temperature=0.3, openai_api_key=openai_api_key) 
    chain = LLMChain(llm=llm, prompt=prompt)
    prompt = request.json.get('prompt')
    output = chain.run(prompt)
    return output
  
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
