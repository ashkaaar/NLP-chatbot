# Import necessary libraries
import os
import warnings
from typing import Dict
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Import necessary modules from openfabric_pysdk
from openfabric_pysdk.utility import SchemaUtil
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass

# Define the path to the model
model_path = "./models/finetuned-science"

# Try to load the model and tokenizer
try:
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
    # Load the model
    model = AutoModelForCausalLM.from_pretrained(model_path)
except Exception as e:
    # If there's an error, raise an exception
    raise Exception(f"No model or tokenizer: {e}")

############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    """
    This function is called when the configuration is updated.
    Currently, it does nothing, but you can add code here to handle configuration updates.
    """
    pass

############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    """
    This function is called on each execution pass.
    It takes a request of type SimpleText, a ray, and a state, and returns a SimpleText response.
    """
    # Initialize chat history
    chat_history_ids = torch.tensor([])

    # Initialize output list
    output = []

    # Loop over each text in the request
    for user_input in request.text:
        # Turn input into tokens
        new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

        # Add input to chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids.shape[0] > 0 else new_user_input_ids

        # Generate response using the model
        chat_history_ids = model.generate(
            bot_input_ids, max_length=1000,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=1.0
        )

        # Decode the chat response
        chat_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

        # Append the response to the output list
        output.append(chat_response)

    # Return a SimpleText object with the output text
    return SchemaUtil.create(SimpleText(), dict(text=output))