import sys
import os
import streamlit
sys.path.append('src')
sys.path.append(os.path.dirname(__file__))
from src.ui import run_app
from ui import run_app
#Run App Py 
if __name__ == '__main__':
    run_app()
