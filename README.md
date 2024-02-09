## NLP Chatbot Setup Details

### Chatbot Development Strategies

When creating an NLP chatbot, there are several strategies to consider:

- **Rule-based Approach**: This strategy involves defining rules and patterns to guide the chatbot's responses. While straightforward, it may lack adaptability to handle complex queries effectively.

- **Pretrained Model Utilization**: Leveraging pretrained models like DialoGPT from Hugging Face allows for quick deployment with minimal training. Fine-tuning such models to specific domains can significantly enhance their performance.

- **Custom Model Training**: Training a custom model using frameworks like PyTorch or TensorFlow offers the flexibility to tailor the chatbot's responses precisely. However, it requires substantial time and resources for data collection, training, and evaluation.

### Preferred Approach

Given the task of developing a chatbot to address science-related inquiries, we opted for:

- **Fine-tuned Pretrained Model**: We fine-tuned a DialoGPT model on science-related data to ensure contextually relevant responses.

### Execute Function Overview

The `execute` function in `main.py` serves as the backbone of our chatbot. It analyzes user input, applies relevant rules or models, and generates appropriate responses. This function undergoes continuous refinement to enhance the chatbot's performance and accuracy.

### Development Guidelines

During the development process, we strictly adhere to the following guidelines:

- 👎 Avoid External Services: We refrain from relying on external services like chatGPT to maintain autonomy and control over the chatbot's functionality.

- 👎 Originality is Key: We prioritize originality and innovation, avoiding plagiarism and ensuring that our solutions stand out in the field.

- 👎 Reliability is Non-negotiable: We prioritize the reliability and robustness of our chatbot, aiming to deliver a seamless user experience without any critical failures.

### Training and Data Insights

Our training process involves fine-tuning the DialoGPT model using a custom dataset crafted specifically for science-related inquiries. This dataset, stored in the `/NOTEBOOKS` directory, encompasses a diverse range of conversational scenarios, ensuring the model's adaptability and effectiveness.

Following rigorous training and validation, the fine-tuned model is stored in the `/MODELS` directory, ready for deployment. Additionally, the original data used for training and validation purposes is archived in the `/DATA` directory, facilitating transparency and reproducibility.

Upon completion of the fine-tuning process, comprehensive insights and performance metrics are documented in the `/RESULTS` directory, guiding further optimization and refinement efforts.

## Initiating the Chatbot Application

To launch the chatbot locally, execute the `script.sh` file. Additionally, the Streamlit user interface can be accessed by running `streamlit run app.py`.
