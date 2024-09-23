import streamlit as st
from src.data_processing import load_data
from src.visualizations import plot_histogram, plot_scatter

# Run App
def run_app():
    st.title('Data Visualizer Interactive')
    
    uploaded_file = st.file_uploader("data/exemplo_dados.csv", type=["csv"])
    
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        if data is not None:
            st.write(data.head())
            columns = list(data.columns)
            
            st.sidebar.header('Visualizations')
            plot_type = st.sidebar.selectbox('Choose plot type', ['Histogram', 'Scatter Plot'])
            
            if plot_type == 'Histogram':
                column = st.sidebar.selectbox('Choose column for histogram', columns)
                plot_histogram(data, column)
            elif plot_type == 'Scatter Plot':
                x_column = st.sidebar.selectbox('Choose X axis', columns)
                y_column = st.sidebar.selectbox('Choose Y axis', columns)
                plot_scatter(data, x_column, y_column)
