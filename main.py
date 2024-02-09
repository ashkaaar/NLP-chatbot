import os
import warnings
from typing import Dict
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from openfabric_pysdk.utility import SchemaUtil
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass

# model stuff
model_path = "./models/finetuned-science"

# gettin' the model and tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
    model = AutoModelForCausalLM.from_pretrained(model_path)
except Exception as e:
    raise Exception(f"No model or tokenizer: {e}")

############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    # TODO Add code here
    pass

############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    # Initialize chat history
    chat_history_ids = torch.tensor([])

    output = []
    for user_input in request.text:
        # turn input into tokens
        new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        # add input to chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids.shape[0] > 0 else new_user_input_ids

        # generate response
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

        output.append(chat_response)

    return SchemaUtil.create(SimpleText(), dict(text=output))