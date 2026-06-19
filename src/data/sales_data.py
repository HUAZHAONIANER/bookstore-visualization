import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data(ttl=300, show_spinner=False)
def generate_sales_transactions():
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='H')
    
    categories = ['文学小说', '科技科普', '儿童读物', '教育考试', '经管励志', '生活艺术']
    sub_categories = {
        '文学小说': ['中国文学', '外国文学', '网络小说', '古典文学'],
        '科技科普': ['计算机', '科普读物', '人工智能', '自然科学'],
        '儿童读物': ['绘本', '童话', '科普百科', '学习辅导'],
        '教育考试': ['考研', '公务员', '职业资格', '语言学习'],
        '经管励志': ['管理学', '投资理财', '成功学', '经济学'],
        '生活艺术': ['烹饪美食', '旅行摄影', '家居生活', '艺术鉴赏']
    }
    
    products = []
    for cat in categories:
        for sub in sub_categories[cat]:
            for i in range(5):
                products.append({
                    'product_id': f"{cat[:2]}{sub[:2]}{str(i+1).zfill(3)}",
                    'category': cat,
                    'sub_category': sub,
                    'name': f"{sub}书籍{i+1}",
                    'price': round(20 + np.random.random() * 100, 2),
                    'author': f"作者{i+1}",
                    'publisher': f"出版社{i+1}"
                })
    
    transactions = []
    for date in dates:
        hour = date.hour
        base_trans = 5 if (hour >= 9 and hour <= 12) or (hour >= 14 and hour <= 20) else 2
        
        for _ in range(int(base_trans * (0.5 + np.random.random()))):
            product = products[np.random.randint(len(products))]
            quantity = np.random.randint(1, 5)
            discount = np.random.choice([0, 0.05, 0.1, 0.15, 0.2], p=[0.6, 0.15, 0.15, 0.05, 0.05])
            total = product['price'] * quantity * (1 - discount)
            
            transactions.append({
                'transaction_id': f"TX{date.strftime('%Y%m%d%H%M%S')}{str(np.random.randint(1000)).zfill(4)}",
                'datetime': date,
                'product_id': product['product_id'],
                'category': product['category'],
                'sub_category': product['sub_category'],
                'product_name': product['name'],
                'quantity': quantity,
                'unit_price': product['price'],
                'discount': discount,
                'total_amount': round(total, 2),
                'payment_method': np.random.choice(['现金', '支付宝', '微信支付', '会员卡']),
                'member_id': f"M{np.random.randint(10000, 99999)}" if np.random.random() > 0.3 else None,
                'store_id': f"S{np.random.randint(1, 5)}"
            })
    
    return pd.DataFrame(transactions)

def generate_daily_sales_summary():
    transactions = generate_sales_transactions().copy()
    transactions['date'] = transactions['datetime'].dt.date
    
    daily_summary = transactions.groupby(['date', 'category', 'store_id']).agg({
        'total_amount': 'sum',
        'quantity': 'sum',
        'transaction_id': 'nunique'
    }).reset_index()
    
    daily_summary.columns = ['date', 'category', 'store_id', 'sales_amount', 'sales_quantity', 'order_count']
    return daily_summary

def generate_monthly_sales_report():
    transactions = generate_sales_transactions().copy()
    transactions['month'] = transactions['datetime'].dt.to_period('M')
    
    monthly_report = transactions.groupby(['month', 'category']).agg({
        'total_amount': 'sum',
        'quantity': 'sum',
        'transaction_id': 'nunique',
        'discount': 'mean'
    }).reset_index()
    
    monthly_report['avg_order_value'] = (monthly_report['total_amount'] / monthly_report['transaction_id']).round(2)
    monthly_report['month'] = monthly_report['month'].astype(str)
    return monthly_report