## NLP Chatbot Setup Details

### Approaches and Methodologies

When developing an NLP chatbot, there are various approaches one can take. These include:

1. **Rule-based Systems**: These systems rely on predefined rules and patterns to understand and respond to user queries. While they can be effective for simple interactions, they often lack the flexibility and adaptability of more advanced methods.

2. **Generative Models**: Generative models, such as DialoGPT, are trained to generate human-like responses based on input text. By fine-tuning a pre-trained model like DialoGPT, we can tailor its responses to specific domains and improve its performance on specialized tasks.

3. **Retrieval-based Models**: Retrieval-based models retrieve predefined responses from a database based on similarity to the user's input. While they can be efficient for retrieving factual information, they may struggle with generating creative or contextually relevant responses.

Given the task of creating a chatbot to master science-related questions, we opted to fine-tune a pre-trained DialoGPT model. This approach offers several advantages:

- **Utilization of Pre-trained Model**: Leveraging a pre-trained model provides a strong starting point, saving time and computational resources.
- **Domain Specificity**: Fine-tuning allows us to tailor the model specifically for science-related inquiries, enhancing its understanding of scientific terminology and context.
- **Efficiency and Effectiveness**: Fine-tuning is often more efficient than training a model from scratch, achieving impressive performance improvements with less data and computing power.
- **Quality Control**: Building upon an existing model reduces the risk of training from insufficient data and ensures a higher starting point for quality.
- **Community Support and Validation**: Fine-tuning benefits from the collective expertise of the research community, with access to best practices and troubleshooting resources.

### Execute Function

The `execute` function within `main.py` serves as the core logic for the AI chatbot. It takes user input, processes it using the fine-tuned model, and generates a response tailored to science education. This function is called on each execution pass, ensuring timely and accurate responses to user queries.

### Rules

When developing the chatbot, we adhered to the following rules:

- 👎 External services like chatGPT are off-limits. Stand on your own.
- 👎 Plagiarism is for the weak. Forge your own path.
- 👎 A broken app equals failure. Non-negotiable.

The custom dataset used for fine-tuning the ChatGPT model is located in the [`/NOTEBOOKS`](notebooks/) directory. This dataset was meticulously crafted to capture a wide range of conversational scenarios, ensuring the model's adaptability to diverse user inputs.

Following rigorous training, the fine-tuned model is stored in the [`/MODELS`](models/) directory, optimized to deliver precise and contextually relevant responses tailored to science-related inquiries.

The original data used for training and validation purposes is stored in the [`/DATA`](data/) directory, forming the foundation upon which the model learns and refines its understanding of the conversational domain.

Upon completion of the fine-tuning process, the results are documented in the [`/RESULTS`](results/) directory, providing insights into the performance and effectiveness of the model and guiding further refinement efforts.

## Starting the Chatbot Application

To start the app locally, run the `script.sh` file. Additionally, the Streamlit UI can be set up using the command `streamlit run app.py`.
