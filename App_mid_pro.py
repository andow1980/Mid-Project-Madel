import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(layout='wide')

# title 
st.title('EPSILON AI Pharmaceuticals Company')
# header
st.header('Commercial Sector'.title() ,divider = True )
# markdown
st.markdown('Data Analysis Management')
# subheader
st.subheader('2024 Sales Report')

data1 = pd.read_excel("Mid_Project_Madel.xlsx") 

#df = st.dataframe(data1)

def page1(df):  
    tab1, tab2, tab3 = st.tabs(['MONTHS', 'QUARTERS','SEASONS'])

    form_options = [''] + df['Form'].unique().tolist()
    Form = st.sidebar.selectbox('Select Form', form_options)

    if Form:
        filtered_groups = df[df['Form'] == Form]['Group'].unique().tolist()
        group_options = [''] + filtered_groups
    else:
        group_options = [''] + df['Group'].unique().tolist()

    Group = st.sidebar.selectbox('Select Group', group_options)
    
    #Group_options = [''] + df['Group'].unique().tolist()
    #Group = st.sidebar.selectbox('Select Group', Group_options)

    if Form and Group:
        filtered_df = df[(df['Form'] == Form) & (df['Group'] == Group)]
    elif Form:
        filtered_df = df[df['Form'] == Form]
    elif Group:
        filtered_df = df[df['Group'] == Group]
    else:
        filtered_df = df.copy()

    with tab1 :

        col1 , col2 = st.columns(2)
        with col1 :
            Total_Amount_month_name_sum = filtered_df.groupby('month_name')['Amount'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Total_Amount_month_name_sum, x=Total_Amount_month_name_sum.index, y=Total_Amount_month_name_sum.values,
                                   color_discrete_sequence=['green'], title='Total Amount by Month') , key = 1 )
            Net_Value_month_name_sum = filtered_df.groupby('month_name')['Net_Value'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Net_Value_month_name_sum, x=Net_Value_month_name_sum.index, y=Net_Value_month_name_sum.values,
                                   color_discrete_sequence=['green'],title='Net Value by Month') , key = 2 )   
        with col2 :
            Total_Cost_month_name_sum = filtered_df.groupby('month_name')['Total_Cost'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Total_Cost_month_name_sum, x=Total_Cost_month_name_sum.index, y=Total_Cost_month_name_sum.values,
                                   color_discrete_sequence=['green'], title='Total Cost by Month') , key = 3 )
            Net_Profit_month_name_sum = filtered_df.groupby('month_name')['Net_Profit'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Net_Profit_month_name_sum, x=Net_Profit_month_name_sum.index, y=Net_Profit_month_name_sum.values,
                                   color_discrete_sequence=['green'], title='Net Profit by Month') , key = 4 )

# ------------------------------------------------------------------------------

    with tab2 :

        col1 , col2 = st.columns(2)
        with col1 :
            Total_Amount_quarter_name_sum = filtered_df.groupby('quarter')['Amount'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Total_Amount_quarter_name_sum, x=Total_Amount_quarter_name_sum.index, y=Total_Amount_quarter_name_sum.values,
                                   color_discrete_sequence=['green'], title='Total Amount by Quarter') , key = 5 )
            Net_Value_quarter_name_sum = filtered_df.groupby('quarter')['Net_Value'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Net_Value_quarter_name_sum, x=Net_Value_quarter_name_sum.index, y=Net_Value_quarter_name_sum.values,
                                   color_discrete_sequence=['green'],title='Net Value by Quarter') , key = 6 ) 
        with col2 :
            Total_Cost_quarter_sum = filtered_df.groupby('quarter')['Total_Cost'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Total_Cost_quarter_sum, x=Total_Cost_quarter_sum.index, y=Total_Cost_quarter_sum.values,
                                   color_discrete_sequence=['green'], title='Total Cost by Quarter') , key = 7 )
            Net_Profit_quarter_sum = filtered_df.groupby('quarter')['Net_Profit'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Net_Profit_quarter_sum, x=Net_Profit_quarter_sum.index, y=Net_Profit_quarter_sum.values,
                                   color_discrete_sequence=['green'], title='Net Profit by Quarter') , key = 8 )
#--------------------------------------------------------------------------------

    with tab3 :

        col1 , col2 = st.columns(2)
        with col1 :
            Total_Amount_season_name_sum = filtered_df.groupby('season')['Amount'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Total_Amount_season_name_sum, x=Total_Amount_season_name_sum.index, y=Total_Amount_season_name_sum.values,
                                   color_discrete_sequence=['green'], title='Total Amount by Season') , key = 9 )
            Net_Value_season_name_sum = filtered_df.groupby('season')['Net_Value'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Net_Value_season_name_sum, x=Net_Value_season_name_sum.index, y=Net_Value_season_name_sum.values,
                                   color_discrete_sequence=['green'],title='Net Value by Season') , key = 10 ) 
        with col2 :
            Total_Cost_season_sum = filtered_df.groupby('season')['Total_Cost'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Total_Cost_season_sum, x=Total_Cost_season_sum.index, y=Total_Cost_season_sum.values,
                                   color_discrete_sequence=['green'], title='Total Cost by Season') , key = 11 )
            Net_Profit_season_sum = filtered_df.groupby('season')['Net_Profit'].sum().sort_values(ascending=False)
            st.plotly_chart(px.bar(Net_Profit_season_sum, x=Net_Profit_season_sum.index, y=Net_Profit_season_sum.values,
                                   color_discrete_sequence=['green'], title='Net Profit by Season') , key = 12 )

def page2(df):
    Top_Quantity_Form = df.groupby('Form')['Quantity'].sum().sort_values(ascending=False)
    st.plotly_chart(px.bar(Top_Quantity_Form, y=Top_Quantity_Form.index,x=Top_Quantity_Form.values,color_discrete_sequence=['green']
                           , title='Top Quantity By Form'))
    
    Total_Cost_Form = df.groupby('Form')['Total_Cost'].sum().sort_values(ascending=False)
    st.plotly_chart(px.bar(Total_Cost_Form, y=Total_Cost_Form.index,x=Total_Cost_Form.values,color_discrete_sequence=['green']
                           , title='Total Cost By Form'))

    top_values_Form = df.groupby('Form')['Net_Value'].sum().sort_values(ascending=False)
    st.plotly_chart(px.bar(top_values_Form, y=top_values_Form.index,x=top_values_Form.values,color_discrete_sequence=['green']
                           , title='Total Sales By Form'))

    Net_Profit_Form = df.groupby('Form')['Net_Profit'].sum().sort_values(ascending=False)
    st.plotly_chart(px.bar(Net_Profit_Form, y=Net_Profit_Form.index,x=Net_Profit_Form.values,color_discrete_sequence=['green']
                           , title='Net Profit By Form'))

def page3(df):
    Top_Quantity_Group = df.groupby('Group')['Quantity'].sum().sort_values(ascending=False).head(15)
    st.plotly_chart(px.bar(Top_Quantity_Group, y=Top_Quantity_Group.index,x=Top_Quantity_Group.values,color_discrete_sequence=['green']
                           , title='Top Quantity By Group'))
    
    Total_Cost_Group = df.groupby('Group')['Total_Cost'].sum().sort_values(ascending=False).head(15)
    st.plotly_chart(px.bar(Total_Cost_Group, y=Total_Cost_Group.index,x=Total_Cost_Group.values,color_discrete_sequence=['green']
                           , title='Total Cost By Group'))

    top_values_Group = df.groupby('Group')['Net_Value'].sum().sort_values(ascending=False).head(15)
    st.plotly_chart(px.bar(top_values_Group, y=top_values_Group.index,x=top_values_Group.values,color_discrete_sequence=['green']
                           , title='Total Sales By Group'))

    Net_Profit_Group = df.groupby('Group')['Net_Profit'].sum().sort_values(ascending=False).head(15)
    st.plotly_chart(px.bar(Net_Profit_Group, y=Net_Profit_Group.index,x=Net_Profit_Group.values,color_discrete_sequence=['green']
                           , title='Net Profit By Group'))
def page4(df):
    Top_Quantity_Alt_Name = df.groupby('Alt_Name')['Quantity'].sum().sort_values(ascending=False).head(15)
    st.plotly_chart(px.bar(Top_Quantity_Alt_Name, y=Top_Quantity_Alt_Name.index,x=Top_Quantity_Alt_Name.values,color_discrete_sequence=['green']
                           , title='Top Quantity By Alt Name'))
    
    Total_Cost_Alt_Name = df.groupby('Alt_Name')['Total_Cost'].sum().sort_values(ascending=False).head(15)
    st.plotly_chart(px.bar(Total_Cost_Alt_Name, y=Total_Cost_Alt_Name.index,x=Total_Cost_Alt_Name.values,color_discrete_sequence=['green']
                           , title='Total Cost By Alt Name'))

    top_values_Alt_Name = df.groupby('Alt_Name')['Net_Value'].sum().sort_values(ascending=False).head(15)
    st.plotly_chart(px.bar(top_values_Alt_Name, y=top_values_Alt_Name.index,x=top_values_Alt_Name.values,color_discrete_sequence=['green']
                           , title='Total Sales By Alt Name'))

    Net_Profit_Alt_Name = df.groupby('Alt_Name')['Net_Profit'].sum().sort_values(ascending=False).head(15)
    st.plotly_chart(px.bar(Net_Profit_Alt_Name, y=Net_Profit_Alt_Name.index,x=Net_Profit_Alt_Name.values,color_discrete_sequence=['green']
                           , title='Net Profit By Alt Name'))

def page5(df):
    
    Market_Category = st.sidebar.radio('Select Market Category', df['Market_Category'].unique())
    df = df[df['Market_Category']== Market_Category]

    top_values_Market = df.groupby('Market')['Net_Value'].sum().sort_values(ascending=False)
    st.plotly_chart(px.histogram(top_values_Market, x=top_values_Market.index,y=top_values_Market.values, color_discrete_sequence=['green']
                                 , title='Total Sales By Market'))
    
    top_Profit_Market = df.groupby('Market')['Net_Profit'].sum().sort_values(ascending=False)
    st.plotly_chart(px.histogram(top_Profit_Market, x=top_Profit_Market.index,y=top_Profit_Market.values, color_discrete_sequence=['green']
                                 , title='Top Profit By Market'))

def page5(df):
    
    Market_Category = st.sidebar.radio('Select Market Category', df['Market_Category'].unique())
    df = df[df['Market_Category']== Market_Category]

    Net_Value_Customer_Name_sum = df.groupby('Customer_Name')['Net_Value'].sum().sort_values(ascending=False).head(15)
    st.plotly_chart(px.histogram(Net_Value_Customer_Name_sum, y=Net_Value_Customer_Name_sum.index, x=Net_Value_Customer_Name_sum.values
                                 , color_discrete_sequence=['green'], title='Net Value by Customer'))
    
    Net_Profit_Customer_Name_sum = df.groupby('Customer_Name')['Net_Profit'].sum().sort_values(ascending=False).head(15)
    st.plotly_chart(px.histogram(Net_Profit_Customer_Name_sum, y=Net_Profit_Customer_Name_sum.index, x=Net_Profit_Customer_Name_sum.values
                                 , color_discrete_sequence=['green'], title='Net Profit by Customer'))

def page6(df):
    
    Market_Category = st.sidebar.radio('Select Market Category', df['Market_Category'].unique())
    df = df[df['Market_Category']== Market_Category]

    top_values_Market = df.groupby('Market')['Net_Value'].sum().sort_values(ascending=False)
    st.plotly_chart(px.histogram(top_values_Market, x=top_values_Market.index,y=top_values_Market.values, color_discrete_sequence=['green']
                                 , title='Total Sales By Market'))
    
    top_Profit_Market = df.groupby('Market')['Net_Profit'].sum().sort_values(ascending=False)
    st.plotly_chart(px.histogram(top_Profit_Market, x=top_Profit_Market.index,y=top_Profit_Market.values, color_discrete_sequence=['green']
                                 , title='Top Profit By Market'))



def page7(df):
    st.header("Top Sales by Month & Quarter & Year")

    # اعلى شهر  
    top_month = df.groupby('month_name')['Net_Value'].sum().idxmax()
    top_month_Sales = df.groupby('month_name')['Net_Value'].sum().max()
    top_month_year = df[df['month_name'] == top_month]['year'].unique()[0] 

    # اعلى كوارتر
    top_quarter = df.groupby('quarter')['Net_Value'].sum().idxmax()
    top_quarter_Sales = df.groupby('quarter')['Net_Value'].sum().max()
    top_quarter_year = df[df['quarter'] == top_quarter]['year'].unique()[0] 

    # اعلى سنة
    top_year_Sales = df.groupby('year')['Net_Value'].sum().idxmax()
    top_year_Sales_by_year_value = df.groupby('year')['Net_Value'].sum().max()
    #top_month_profit_by_month_year = df[df['month'] == top_month_profit_by_month]['year'].unique()[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Top Month Sales", value=f"{top_month_Sales:.2f}", delta=f"{top_month} ({top_month_year})")  

    with col2:
        st.metric(label="Top Quarter Sales", value=f"{top_quarter_Sales:.2f}", delta=f"{top_quarter} ({top_quarter_year})")

    with col3:
        st.metric(label="Top Year Sales", value=f"{top_year_Sales_by_year_value:.2f}", delta=f"{top_year_Sales}")
        
def page8(df):
    st.header("Top Profit by Month & Quarter & Year")

    # اعلى شهر  
    top_month = df.groupby('month_name')['Net_Profit'].sum().idxmax()
    top_month_profit = df.groupby('month_name')['Net_Profit'].sum().max()
    top_month_year = df[df['month_name'] == top_month]['year'].unique()[0] 

    # اعلى كوارتر
    top_quarter = df.groupby('quarter')['Net_Profit'].sum().idxmax()
    top_quarter_profit = df.groupby('quarter')['Net_Profit'].sum().max()
    top_quarter_year = df[df['quarter'] == top_quarter]['year'].unique()[0] 

    # اعلى شهر من حيث الربح
    top_year_profit = df.groupby('year')['Net_Profit'].sum().idxmax()
    top_year_profit_by_year_value = df.groupby('year')['Net_Profit'].sum().max()
    #top_month_profit_by_month_year = df[df['month'] == top_month_profit_by_month]['year'].unique()[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Top Month Profit", value=f"{top_month_profit:.2f}", delta=f"{top_month} ({top_month_year})")  

    with col2:
        st.metric(label="Top Quarter Profit", value=f"{top_quarter_profit:.2f}", delta=f"{top_quarter} ({top_quarter_year})")

    with col3:
        st.metric(label="Top Year Profit", value=f"{top_year_profit_by_year_value:.2f}", delta=f"{top_year_profit}")

pgs= {
    'TIME PERIOD' : page1,
    'FORMS' : page2,
    'TOP 15 GROUPS' : page3,
    'TOP 15 MARKET NAME' : page4,
    'TOP 15 CUSTOMERS' : page5,
    'MARKET CATEGORY' : page6,
    'TOP SALES' : page7,
    'TOP PROFIT' : page8
}

pg = st.sidebar.radio('Navigate Pages', options= pgs.keys())
pgs[pg](data1) 
