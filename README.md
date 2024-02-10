## Demo
![Demo](demo.gif)

Play around with the chatbot [Here](https://science-nlp-chatbot.streamlit.app/)

## Explanation Video
The explanation video can be found [Here](videolink)

## NLP Chatbot Setup Details

### Chatbot Development Strategies

When developing an NLP chatbot, there are several strategies to consider:

- **Rule-based Approach**: This method involves setting predefined rules and patterns to guide the chatbot's responses. While simple, it may struggle with complex queries.

- **Pretrained Model Utilization**: Utilizing pretrained models like DialoGPT from Hugging Face offers a quick deployment solution with minimal training. Fine-tuning these models for specific domains can significantly improve their performance.

- **Custom Model Training**: Training a custom model using frameworks like PyTorch or TensorFlow allows for precise customization of the chatbot's responses. However, it requires substantial time and resources for data collection and training.

### Preferred Approach

For the science-related chatbot development, I chose:

- **Fine-tuned Pretrained Model**: I opted to fine-tune a DialoGPT model on science-related data. This involved training the pretrained DialoGPT model on a custom dataset curated for science-related queries. Fine-tuning ensured that the model could understand and generate responses tailored to scientific topics, enhancing accuracy and relevance.

### Training and Data Insights

Training involves fine-tuning the DialoGPT model using a custom dataset crafted specifically for science-related inquiries. The Jupyter Notebook used for fine-tuning can be found in the [`/NOTEBOOKS`](notebooks/) directory. This dataset was meticulously designed to cover various science-related topics, ensuring the model's proficiency.

Following training, the fine-tuned model is stored in the [`/MODELS`](models/) directory for deployment. Additionally, original data used for training and validation is archived in the [`/DATA`](data/) directory for transparency.

Upon completion, insights and performance metrics are documented in the [`/RESULTS`](results/) directory, guiding further improvements.

### Execute Function Overview

The `execute` function in `main.py` is crucial for the chatbot's operation. It analyzes user input, applies relevant rules or models, and generates appropriate responses. Continuous refinement of this function enhances the chatbot's performance and accuracy over time.

### Development Guidelines

During development, I adhere to the following guidelines:

- 👎 Avoid External Services: I avoid reliance on external services like chatGPT to maintain control over the chatbot's functionality.

- 👎 Originality is Key: I prioritize originality and innovation to ensure my chatbot stands out.

- 👎 Reliability is Non-negotiable: I prioritize reliability to deliver a seamless user experience without critical failures.

## Initiating the Chatbot Application

To launch the chatbot locally, execute the `script.sh` file. Additionally, access the Streamlit user interface by running `streamlit run app.py`.

Feel free to reach out if you have any questions or need further assistance!
