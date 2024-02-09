## NLP Chatbot Setup Details

The `main.py` file serves as the core logic for the AI chatbot.

The chatbot utilizes a pre-trained DialoGPT model fine-tuned specifically for science-related inquiries. This fine-tuning process ensures that the model is optimized to generate contextually relevant responses to science-related questions.

The `execute` function, called on each execution pass, takes user input, processes it using the fine-tuned model, and generates a response tailored to science education.

The chatbot leverages techniques such as tokenization and generation to ensure accurate and comprehensive answers.

Additionally, the `app.py` file contains the Streamlit user interface for accessing the `execute` function defined in `main.py`, in accordance with the project requirements.

## Training and Data Details

The Jupyter Notebook used to fine-tune the ChatGPT model in the Google Colab free tier can be found in the [`/NOTEBOOKS`](notebooks/) directory.
This dataset was meticulously crafted to cover a wide range of science-related topics, ensuring the model's proficiency in generating relevant responses.

Following rigorous training, the fine-tuned model is stored in the [`/MODELS`](models/) directory. This model has been optimized to deliver precise and contextually relevant responses, tailored specifically to the domain of the provided dataset.

The original data used for training and validation purposes is stored in the [`/DATA`](data/) directory. This data forms the foundation upon which the model learns and refines its understanding of the conversational domain.

Upon completion of the fine-tuning process, the results are documented in the [`/RESULTS`](results/) directory. These results provide insights into the performance and effectiveness of the fine-tuned model, serving as a valuable resource for evaluation and further refinement.

## Approach and Methodology

For fine-tuning the model, a custom dataset was created through interactions with ChatGPT in the Jupyter Notebook available in the [`/NOTEBOOKS`](notebooks/) directory. This dataset was meticulously crafted to cover a wide range of science-related topics, ensuring the model's proficiency in generating relevant responses.

Training the model involved extensive iterations, with performance evaluation conducted using the original data stored in the [`/DATA`](data/) directory. The fine-tuned model's effectiveness was measured and documented in the [`/RESULTS`](results/) directory, guiding further refinement efforts.

## Starting the Chatbot Application

To start the app locally, run the `script.sh` file. Additionally, the Streamlit UI can be set up using the command `streamlit run app.py`.
