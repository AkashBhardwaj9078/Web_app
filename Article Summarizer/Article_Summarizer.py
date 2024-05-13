
import openai
import  streamlit as st



openai.api_key=st.secrets["api_key"]

st.title("OpenAi Text Summarizer")

def response(prompt):
    responses=openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        # prompt="please summarize the scientific aritcle  containing all their intricate details while maintainig its tone and purpose, for quick readers, inorder to comprehend it with a glance ",
        # temperature=0.3,
     
       
        # max_tokens=512,        
        )
    return responses.choices[0].text
    
article=st.text_area("Enter the article that you want to summarize")

if len(article)>100:
    
    temp=st.slider(value=0.3,min_value=0.0,max_value=1.0,label="temperature")
    if st.button("Generate Summary"):
        responses=openai.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":article}],
        prompt="please summarize the scientific aritcle  containing all their intricate details while maintainig its tone and purpose, for quick readers, inorder to comprehend it with a glance ",
        temperature=temp,
     
       
        max_tokens=512,        
        )
        msg=responses.choices[0].text
        st.info(msg)
        print()
else:
    st.warning("The article is not long enough")

if __name__=="__main__":
    inp=input("you :")
    print("chatbot :",response(inp))



