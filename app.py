import streamlit as st
from src import palette


st.title('My palette generator')
uploaded_image = st.file_uploader(
    'Upload a image', 
    type=['jpg','jpeg']
)
col1, col2 = st.columns(2)
if uploaded_image:
    with col1:
        st.image(uploaded_image)
    with col2:
        #st.button('Download')
        n_clusters = st.slider('Number of colors', 2, 8, 5)
        if st.button('Generate palette'):
            with st.spinner('Generating palette...'):
                cores,cores_hex = palette.get(uploaded_image, n_clusters)
            
            figura = palette.show(cores)
            st.pyplot(figura)
            st.code(cores_hex)
    
            btn = st.download_button(
               label="Download image",
               data=palette.save(figura),
               file_name='palette.png',
               mime="image/png"
            )
