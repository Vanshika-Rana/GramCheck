from gingerit.gingerit import GingerIt
import streamlit as st
from PIL import Image
st.set_page_config(page_title='GramCheck', page_icon="./icon.png")

st.title("GramCheck : Easy Way To Get Your English Sentences Corrected.")
header = Image.open('illus.png')
st.image(header, width=500)
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


