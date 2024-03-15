import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np
import datetime as dt
from PIL import Image
import joblib
import warnings
warnings.filterwarnings('ignore')

def predict_price(test_data):
    
    loaded_model = joblib.load(r'C:\pythan\DATA SCEINCE\final project\Weekly Sales Price.joblib.gz')
    data=loaded_model.predict(test_data)[0]

    return data
    
store_value = [i for i in range(1, 46)]

Type = {'A':1, "B":2, 'C':3}

dept = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
         33, 34, 35, 36, 37, 38, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 58, 59, 60, 67, 71, 72, 74, 79, 80, 81, 82, 
         83, 85, 87, 90, 91, 92, 93, 94, 95, 97, 78, 96, 99, 39, 77, 50, 43, 65, 98]

Size_value = [151315, 202307,  37392, 205863,  34875, 202505,  70713, 155078, 125833, 126512, 207499, 112238, 219622, 200898, 123737,  
              57197, 93188, 120653, 203819, 203742, 140167, 119557, 114533, 128107, 152513, 204184, 206302,  93638,  42988, 203750,
                203007,  39690, 158114, 103681,  39910, 184109, 155083, 196321,  41062, 118221]

IsHoliday= {'No Holiday':0, 'Super Bowl':1, 'Labor Day':2, 'Thanksgiving':3, 'Christmas':4}
    
# SETTING PAGE CONFIGURATIONS
st.set_page_config(page_title= "Walmart Retail Sales Prediction",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This Walmart Retail Sales Prediction app is created by R.AJITH KUMAR!"""})
st.markdown("<h1 style='text-align: center; color: white;'> Walmart Retail Sales Prediction Application</h1>", unsafe_allow_html=True)

# SETTING-UP BACKGROUND IMAGE
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right,#cfd8dc, #90a4ae, #607d8b, #37474f, #263238);
            background-size: cover;
        }
    </style>
""", unsafe_allow_html=True)

# CREATING OPTION MENU
selected = option_menu(None, ["HOME","PREDICT SELLING PRICE"], 
                       icons=["house","dollar-sign"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"nav-link": {"font-size": "25px", "text-align": "centre", "margin": "0px", "--hover-color": "#90a4ae"},
                               "icon": {"color": "red","font-size": "25px"},
                               "container" : {"max-width": "6000px"},
                               "nav-link-selected": {"background-color": " #37474f"}})

if selected == "HOME":
    col1,col2 = st.columns(2, gap = 'small')
    with col1:
       st.markdown("## :green[**Project:**] Walmart Retail Sales Prediction")
       st.markdown("## :green[**Overview :**] Walmart is an American multinational retail corporation that operates a chain of hypermarkets (also called supercenters), discount department stores, and grocery stores in the United States, headquartered in Bentonville")
       st.markdown("## :green[**BUSINESS OBJECTIVES:**]  This project aims to develop machine learning model for the Walmart Retail shop to address the challenges of predicting selling price and lead classification. Manual predictions can be time-consuming and may not result in optimal pricing decisions or accurately capture leads. The models will utilize advanced techniques such as data normalization, outlier detection and handling, handling data in the wrong format, identifying the distribution of features, and leveraging tree-based models, specifically the decision tree algorithm, to predict the selling price and leads accurately.")
       st.markdown("## :green[**Technologies Used :**]")
       st.markdown("## * Python")
       st.markdown("## * Pandas")
       st.markdown("## * Scikit-learn")
       st.markdown("## * Streamlit")
       st.markdown("## *  joblib")
      
    with col2:
       image= Image.open(r'C:\pythan\DATA SCEINCE\final project\OIP.jpg')
       st.image(image)

       image= Image.open(r'C:\pythan\DATA SCEINCE\final project\download (2).jpg')
       st.image(image)
       st.markdown("## :green[**REGRESION MODEL:**]")
       st.markdown("## Regression is a statistical method used in finance, investing, and other disciplines that attempts to determine the strength and character of the relationship between one dependent variable (usually denoted by Y) and a series of other variables (known as independent variables)")
       st.markdown("## :green[**STORE:**] The store number")
       st.markdown("## :green[**SIZE:**] Size of the Store")
       st.markdown("## :green[**TYPE:**] Type of the Store")
       st.markdown("## :green[**DEPT:**] Department of the Store")
       st.markdown("## :green[**ISHOLIDAY:**]  Whether the week is a special holiday week")
       st.markdown("## :green[**TEMPERATURE:**] Average temperature in the region (in ℉)")
       st.markdown("## :green[**:FUEL PRICE**] Cost of fuel in the region")
       st.markdown("## :green[**MarkDown1-5:**] Anonymized data related to promotional markdowns that Walmart is running.")
     

if selected == "PREDICT SELLING PRICE":
    col1, col2 = st.columns(2, gap= 'large')

    with col1:
        date_ = st.date_input('Select the **Date**',  dt.date(2012, 12,5), min_value= dt.date(2010, 2,5), max_value= dt.date.today())

        Store = st.selectbox('Select the **Store Number**', store_value)

        type = st.selectbox('Select the **Store Type**', ['A', 'B', 'C'])

        Size = st.selectbox('Select the **Store Size** in square meter', Size_value)

        Dept = st.selectbox('Select the **Deparment**', dept, index = 80)

        holiday = st.selectbox('Select the **IsHoliday**', ['No Holiday', 'Super Bowl', 'Labor Day', 'Thanksgiving', 'Christmas'])

        Temperature = st.number_input('Enter the **Temperature** in Celsius', value =42.34, min_value= 5.10, max_value= 90.42)

        Fuel_Price= st.number_input('Enter the **Fuel Price** in Dollar', value =3.408, min_value= 1.5, max_value= 10.00)


    with col2:

        CPI = st.number_input('Enter the **CPI**', value =172.57, min_value= 126.00, max_value= 250.00)

        Unemployment = st.number_input('Enter the **Unempolyment** in Percentage', value =7.66, min_value= 2.00, max_value= 15.00)

        MarkDown1 = st.number_input('Enter the **MarkDown1** in Dollar', value = 7437.49)

        MarkDown2 = st.number_input('Enter the **MarkDown2** in Dollar', value = 2517.4)

        MarkDown3 = st.number_input('Enter the **MarkDown3** in Dollar', value = 1310.9)

        MarkDown4 = st.number_input('Enter the **MarkDown4** in Dollar', value = 10.00)

        MarkDown5 = st.number_input('Enter the **MarkDown5** in Dollar', value = 3318)
    
        Year= date_.year
        Month= date_.month
        Week= date_.day

    test_data = np.array([[ Store, Type[type], Size, Dept,  IsHoliday[holiday], Temperature, Fuel_Price, MarkDown1, MarkDown2, MarkDown3, MarkDown4, MarkDown5,
                  CPI, Unemployment, Year, Month, Week]])


    st.markdown('Click below button to predict the **Predict Weekly Price**')
    pred = st.button('Predict Weekly Sales')

    if pred:
    # Perform prediction and display result
        predicted_sales = predict_price(test_data)
        st.markdown(f"### :blue[Weekly Sales Price is] :green[$ {predicted_sales}]")
