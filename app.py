# -*- coding: UTF-8 -*-
import streamlit as st 
import pandas as pd 
import matplotlib as mpl
import seaborn as sns 
import plotly 
import sklearn 
import numpy as np 

# Fxns

def main():
    """코드 작성"""
    st.title("streamlit 버전: " + str(st.__version__))
    st.title("pandas 버전: " + str(pd.__version__))
    st.title("matplotlib 버전: " + str(mpl.__version__))
    st.title("seaborn 버전: " + str(sns.__version__))
    st.title("sklearn 버전: " + str(sklearn.__version__))
    st.title("numpy 버전: " + str(np.__version__))
    st.title("plotly 버전: " + str(plotly.__version__))

if __name__ == "__main__":
    main()