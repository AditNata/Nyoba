import streamlit as st
import pandas as pd
import numpy as np

#untuk judul
st.title('SIMPLE VECTOR')

#untuk sidebar
with st.sidebar:
    tipe = st.radio('pilih tipe',['single vector', 'double matrix'])
   
#untuk expander(memilih ukuran)
with st.expander('pilih ukuran'):
    with st.form('pilih ukuran'):
        if tipe == 'single vector':
            size = st.number_input('ukuran dari vektor', min_value=2)
        elif tipe == 'double matrix':
            row1 = st.number_input('ukuran baris dari matrix pertama', min_value=2)
            col1 = st.number_input('ukuran kolom dari matrix pertama', min_value=2)
            row2 = st.number_input('ukuran baris dari matrix kedua', min_value=2)
            col2 = st.number_input('ukuran kolom dari matrix kedua', min_value=2)           
        st.form_submit_button('kirim ukuran')
        
#unntuk input data
if tipe == 'single vector':
    st.write('data untuk vektor')
    df = pd.DataFrame(columns=range(1,size+1), index=range(1,2), dtype=float) #untuk membuat tabel kosong
    df_input = st.experimental_data_editor(df, use_container_width=True)
    
    operasi = st.radio('piluh operasi',['A*B', 'A+B'])
    
elif tipe == 'double matrix':
    st.write('data untuk matriks pertama')
    df_1 = pd.DataFrame(columns=range(1,col1+1), index=range(1,row1+1), dtype=float) 
    df_1_input = st.experimental_data_editor(df_1, use_container_width=True, key=1)
    
    st.write('data untuk matriks kedua')
    df_2 = pd.DataFrame(columns=range(1,col2+1), index=range(1,row2+1), dtype=float) 
    df_2_input = st.experimental_data_editor(df_2, use_container_width=True, key=2)
    
    #convert table to matrix
    matrix1 = df_1_input.fillna(0).to_numpy()
    matrix2 = df_2_input.fillna(0).to_numpy()
    
    operasi = st.radio('pilih operasi',['A*B', 'A+B'])
    if operasi == 'A*B':
        hasil = np.matmul(matrix1,matrix2)
        st.write(hasil)
    elif operasi == "A+B":
        hasil = matrix1 + matrix2
        st.write(hasil)
    