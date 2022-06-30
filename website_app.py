import streamlit as st
from streamlit_option_menu import option_menu
#import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
#import streamlit.components.v1 as components
import base64
from streamlit_text_rating.st_text_rater import st_text_rater

with st.sidebar:
    choose = option_menu("Main Menu", ["About", "Projects", "Blog","Apps", "Contact"],
                         icons=['house', 'bar-chart-line','file-slides','app-indicator','person lines fill'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#24A608"},
    }
    )

logo = Image.open('demo_image1.png')
profile = Image.open('demo_image2.png')
if choose == "About":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Creator</p>', unsafe_allow_html=True)    
    with col2:               # To display brand log
        st.image(logo, width=130 )
  
     # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    
 contact_form = """
    <form action="https://formsubmit.co/dominica.hewett@uwforsyth.org" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

#<div class="container">
  #<form action="action_page.php">

    #<label for="fname">First Name</label>
    #<input type="text" id="fname" name="firstname" placeholder="Your name..">

    #<label for="lname">Last Name</label>
    #<input type="text" id="lname" name="lastname" placeholder="Your last name..">

    #<label for="country">Country</label>
    #<select id="country" name="country">
      #<option value="australia">Australia</option>
      #<option value="canada">Canada</option>
      #<option value="usa">USA</option>
    #</select>

    #<label for="subject">Subject</label>
    #<textarea id="subject" name="subject" placeholder="Write something.." style="height:200px"></textarea>

    #<input type="submit" value="Submit">

  #</form>
#</div>
    
    st.write("Sharone Li is a data science practitioner, enthusiast, and blogger. She writes data science articles and tutorials about Python, data visualization, Streamlit, etc. She is also an amateur violinist who loves classical music.\n\nTo read Sharone's data science posts, please visit her Medium blog at: https://medium.com/@insightsbees")    
    st.image(profile, width=400 )

elif choose == "Blog": 
        topic = option_menu(None, ["Streamlit", "Pandas","Plotly", "Folium"],
                         icons=['book', 'book','book','book'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#080000"},
        },orientation='horizontal'
        ) 

        st.write('')
        def show_pdf(file_path):
            with open(file_path,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
        
        if topic=='Pandas':
            feature_image1 = Image.open('demo_image2.png')
            with st.container():
                image_col, text_col = st.columns((1,3))
                with image_col:
                    st.image(feature_image1,caption='Image by Pixabay')
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Clean a ‘Numeric’ ID Column in Pandas Dataframe</p>', unsafe_allow_html=True)    
                    st.markdown("By Sharone Li - As a data scientist, you must have encountered this problem at least once in your data science journey: you import your data into a Pandas dataframe... [Continue to Read on Towards Data Science](https://docs.google.com/document/d/e/2PACX-1vSp_1zm6iAvep64Ib8Nw5MN8lRsDynr4g2NaAe21o_8umNX88RRgEsRt83Y3oEicfpFRL0dgR56h7_P/pub)")

            col1, col2,col3= st.columns(3)
            with col1:  
                if st.button('Read PDF Tutorial',key='1'):            
                    show_pdf('post1-compressed.pdf')
            with col2:
                st.button('Close PDF Tutorial',key='2')                   
            with col3:
                with open("post1-compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Tutorial", key='3',
                        data=PDFbyte,
                        file_name="pandas-clean-id-column.pdf",
                        mime='application/octet-stream')

            for text in ["Is this tutorial helpful?"]:
                    response = st_text_rater(text=text, key='1')

            st.write('---')
            feature_image2 = Image.open('demo_image2.png')
            with st.container():
                image_col, text_col = st.columns((1,3))
                with image_col:
                    st.image(feature_image2,caption='Image by Pixabay')

                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">How to Batch Rename Columns in Pandas Based on Patterns</p>', unsafe_allow_html=True)    
                    st.markdown("By Sharone Li - If you have been following my Medium blog for some time, you may notice that I usually like to share... [Continue to Read on CodeX](https://docs.google.com/document/d/e/2PACX-1vSp_1zm6iAvep64Ib8Nw5MN8lRsDynr4g2NaAe21o_8umNX88RRgEsRt83Y3oEicfpFRL0dgR56h7_P/pub)")
                   
            col1, col2,col3 = st.columns(3)
            with col1: 
                #st.button('Read PDF Tutorial', key='1')
 
                if st.button('Read PDF Tutorial',key='7'): 
                  show_pdf('post3.pdf')
            with col2:
                st.button('Close PDF Tutorial',key='8')                   
            with col3:
                with open("post3.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()

                st.download_button(label="Download PDF Tutorial",key='9',
                        data=PDFbyte,
                        file_name="pandas-rename-columns.pdf",
                        mime='application/octet-stream')
            for text in ["Is this tutorial helpful?"]:
                    response = st_text_rater(text=text, key='2')

            st.write('---')
            feature_image3 = Image.open('demo_image2.png')
            with st.container():
                image_col, text_col = st.columns((1,3))
                with image_col:
                    st.image(feature_image3,caption='Image by Pixabay')

                with text_col:
                    st.markdown('<p class="font">Why and How to Reshape a Pandas Dataframe from Wide to Long</p>', unsafe_allow_html=True)    
                    st.markdown("By Sharone Li - As data scientists, we know that data does not always come to us with the most desirable format... [Continue to Read on Towards Data Science](https://towardsdatascience.com/clean-a-numeric-id-column-in-pandas-dataframe-fbe03c11e330)")
                           
            col1, col2,col3 = st.columns(3)
            with col1:
                if st.button('Read PDF Tutorial',key='4'): 
                    show_pdf('post1-compressed.pdf')
            with col2:
                st.button('Close PDF Tutorial',key='5')                   
            with col3:
                with open("post1-compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()

                st.download_button(label="Download PDF Tutorial",key='6',
                        data=PDFbyte,
                        file_name="pandas-reshape-dataframe.pdf",
                        mime='application/octet-stream')
            for text in ["Is this tutorial helpful?"]:
                response = st_text_rater(text=text, key='3')


