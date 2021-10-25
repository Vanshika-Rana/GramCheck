from gingerit.gingerit import GingerIt
import streamlit as st
from PIL import Image
st.set_page_config(page_title='GramCheck', page_icon="./icon.png")
header = Image.open('illus.jpg')
st.image(header)
st.title("GramCheck : Easy Way To Get Your English Sentences Corrected.")

sentence = st.text_area(label="Enter Your Sentence Here ...")
parser = GingerIt()

if st.button('Correct Now!'):
    if sentence == '':
        st.write('No Sentence given..')
    else:
        result=parser.parse(sentence)
        st.subheader(result["result"])
else:
    pass


