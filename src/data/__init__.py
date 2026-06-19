import streamlit as st
from .sales_data import generate_sales_transactions, generate_daily_sales_summary, generate_monthly_sales_report
from .inventory_data import generate_inventory_data, generate_inventory_movement
from .customer_data import generate_customer_data, generate_customer_behavior
from .employee_data import generate_employee_data, generate_attendance_data

@st.cache_data(ttl=300, show_spinner="加载数据中...")
def load_all_data():
    return {
        'sales_transactions': generate_sales_transactions(),
        'daily_sales_summary': generate_daily_sales_summary(),
        'monthly_sales_report': generate_monthly_sales_report(),
        'inventory': generate_inventory_data(),
        'inventory_movement': generate_inventory_movement(),
        'customers': generate_customer_data(),
        'customer_behavior': generate_customer_behavior(),
        'employees': generate_employee_data(),
        'attendance': generate_attendance_data()
    }
