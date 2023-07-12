import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
st.title('Nupur World')

st.header('By Nupur Sahoo')
st.text('This is a tutorial on Streamlit Library')
if(mymenu=='Home'):
    
    
    st.video('https://youtu.be/sVPYIRF9RCQ')
    st.image('https://th.bing.com/th?id=OSK.51053f2608887c85ccaf7038d1e46985&w=116&h=156&c=7&o=6&pid=SANGAM')
    st.image('https://th.bing.com/th?id=OIP.RG58DaO7kXIPA2oTSLS6kAHaE8&w=306&h=204&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2')

elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter Name ')
        dob=st.date_input('Choose date of birth')
        marks=st.slider('Choose Marks')
        k=st.form_submit_button('Submit Form')
        if k:
            st.write('Name:',name,'DOB:',dob,'Marks:',marks)
elif(mymenu=='Downloads'):
    st.header('Downloads')
    st.download_button('Download Now','Hello This is the downloaded data','nupur.txt')
