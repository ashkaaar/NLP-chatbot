## NLP Chatbot Setup Details

The `main.py` file serves as the core logic for the AI chatbot.

The chatbot utilizes a pre-trained DialoGPT model fine-tuned specifically for science-related inquiries. This fine-tuning process ensures that the model is optimized to generate contextually relevant responses to science-related questions. 

The `execute` function, called on each execution pass, takes user input, processes it using the fine-tuned model, and generates a response tailored to science education. 

The chatbot leverages techniques such as tokenization and generation to ensure accurate and comprehensive answers.

Additionally, the `app.py` file contains the Streamlit user interface for accessing the `execute` function defined in `main.py`, in accordance with the project requirements.

## Training and Data Details

The custom dataset used for training the ChatGPT model is located in the `/NOTEBOOKS` directory. This dataset was meticulously crafted to capture a wide range of conversational scenarios, ensuring the model's adaptability to diverse user inputs.

Following rigorous training, the fine-tuned model is stored in the `/MODELS` directory. This model has been optimized to deliver precise and contextually relevant responses, tailored specifically to the domain of the provided dataset.

The original data used for training and validation purposes is stored in the `/DATA` directory. This data forms the foundation upon which the model learns and refines its understanding of the conversational domain.

Upon completion of the fine-tuning process, the results are documented in the `/RESULTS` directory. These results provide insights into the performance and effectiveness of the fine-tuned model, serving as a valuable resource for evaluation and further refinement.

## Starting the Chatbot Application

To start the app locally, run the `script.sh` file. Additionally, the Streamlit UI can be set up using the command `streamlit run app.py`.
