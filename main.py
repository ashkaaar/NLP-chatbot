from transformers import AutoModelForCausalLM, AutoTokenizer
import streamlit as st
import torch
import pandas as pd
# model stuff
model_path = "./models/finetuned-science"

# gettin' the model and tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-small')
    model = AutoModelForCausalLM.from_pretrained(model_path)
except Exception as e:
    st.error(f'No model or tokenizer: {e}')
    raise

# chat history
chat_history_ids = torch.tensor([])

conversation_df = pd.DataFrame(columns=['User', 'Chatbot'])


#This following is how we can execute the chatbot with the exectutre function but may not be suitable for intereacting with the chatbot locally, that's why I have commented it out


# ############################################################
# # Callback function called on update config
# ############################################################
# def config(configuration: Dict[str, ConfigClass], state: State):
#     # TODO Add code here
#     pass


# ############################################################
# # Callback function called on each execution pass
# ############################################################
# def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
#     output = []
#     for user_input in request.text:
#         # turn input into tokens
#         new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
#         # add input to chat history
#         bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids.shape[0] > 0 else new_user_input_ids

#         # generate response
#         chat_history_ids = model.generate(
#             bot_input_ids, max_length=1000,
#             pad_token_id=tokenizer.eos_token_id,  
#             no_repeat_ngram_size=3,       
#             do_sample=True, 
#             top_k=50,  
#             top_p=0.95, 
#             temperature=1.0  
#         )
        
#         # Decode the chat response
#         chat_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        
#         output.append(chat_response)

#     return SchemaUtil.create(SimpleText(), dict(text=output))


#This following is the streamlit UI code that will be used to interact with the chatbot

# Set page title
st.set_page_config(page_title='NLP-Chatbot')

# Title
st.title('NLP-Chatbot')

# User input
user_input = st.text_input('Enter your message here')

# Submit button
if st.button('Submit'):
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
    
    # Display chat response
    st.text_area('Response', chat_response, height=200)