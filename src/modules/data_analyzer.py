import pandas as pd
import numpy as np
from functools import lru_cache

class SalesAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def get_sales_trend(self, period='month', category=None, store_id=None):
        df = self.data['daily_sales_summary']
        df['date'] = pd.to_datetime(df['date'])
        
        if category:
            df = df[df['category'] == category]
        if store_id:
            df = df[df['store_id'] == store_id]
        
        if period == 'month':
            df['period'] = df['date'].dt.to_period('M').astype(str)
        elif period == 'week':
            df['period'] = df['date'].dt.isocalendar().week
        else:
            df['period'] = df['date']
        
        trend = df.groupby('period').agg({
            'sales_amount': 'sum',
            'sales_quantity': 'sum',
            'order_count': 'sum'
        }).reset_index()
        
        trend['avg_order_value'] = (trend['sales_amount'] / trend['order_count']).round(2)
        return trend
    
    def get_category_sales_distribution(self, date_range=None):
        df = self.data['daily_sales_summary']
        df['date'] = pd.to_datetime(df['date'])
        
        if date_range:
            df = df[(df['date'] >= date_range[0]) & (df['date'] <= date_range[1])]
        
        distribution = df.groupby('category').agg({
            'sales_amount': 'sum',
            'sales_quantity': 'sum',
            'order_count': 'sum'
        }).reset_index()
        
        distribution['percentage'] = (distribution['sales_amount'] / distribution['sales_amount'].sum() * 100).round(1)
        return distribution.sort_values('sales_amount', ascending=False)
    
    def get_store_performance(self, period='month'):
        df = self.data['daily_sales_summary']
        df['date'] = pd.to_datetime(df['date'])
        df['period'] = df['date'].dt.to_period('M').astype(str)
        
        performance = df.groupby(['store_id', 'period']).agg({
            'sales_amount': 'sum',
            'sales_quantity': 'sum',
            'order_count': 'sum'
        }).reset_index()
        
        performance['avg_order_value'] = (performance['sales_amount'] / performance['order_count']).round(2)
        return performance
    
    def get_top_products(self, top_n=10):
        df = self.data['sales_transactions'].copy()
        top_products = df.groupby(['product_id', 'product_name', 'category']).agg({
            'total_amount': 'sum',
            'quantity': 'sum',
            'transaction_id': 'nunique'
        }).reset_index()
        
        return top_products.sort_values('total_amount', ascending=False).head(top_n)
    
    def get_payment_method_distribution(self):
        df = self.data['sales_transactions'].copy()
        distribution = df.groupby('payment_method').agg({
            'total_amount': 'sum',
            'transaction_id': 'nunique'
        }).reset_index()
        
        distribution['percentage'] = (distribution['total_amount'] / distribution['total_amount'].sum() * 100).round(1)
        return distribution
    
    def calculate_sales_growth(self):
        monthly = self.get_sales_trend(period='month')
        monthly['growth_rate'] = monthly['sales_amount'].pct_change() * 100
        monthly['growth_rate'] = monthly['growth_rate'].round(2)
        return monthly

class InventoryAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def get_inventory_summary(self):
        df = self.data['inventory'].copy()
        
        summary = df.groupby('category').agg({
            'current_stock': 'sum',
            'min_stock': 'sum',
            'max_stock': 'sum',
            'unit_cost': 'mean',
            'unit_price': 'mean'
        }).reset_index()
        
        summary['stock_utilization'] = (summary['current_stock'] / summary['max_stock'] * 100).round(1)
        summary['total_value'] = (summary['current_stock'] * summary['unit_cost']).round(2)
        return summary
    
    def get_stock_status_distribution(self):
        df = self.data['inventory'].copy()
        status = df.groupby('stock_status').size().reset_index(name='count')
        status['percentage'] = (status['count'] / status['count'].sum() * 100).round(1)
        return status
    
    def get_low_stock_alert(self, threshold=30):
        df = self.data['inventory'].copy()
        low_stock = df[df['stock_utilization'] < threshold].sort_values('stock_utilization')
        return low_stock[['product_id', 'product_name', 'category', 'store_id', 'current_stock', 'min_stock', 'stock_utilization']]
    
    def get_inventory_turnover(self):
        df = self.data['inventory_movement'].copy()
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M').astype(str)
        
        turnover = df.groupby(['month', 'category']).agg({
            'quantity': 'sum',
            'cost': 'sum'
        }).reset_index()
        
        return turnover
    
    def get_expiry_alert(self, days_threshold=90):
        df = self.data['inventory'].copy()
        expiry = df[df['days_to_expiry'] < days_threshold].sort_values('days_to_expiry')
        return expiry[['product_id', 'product_name', 'category', 'store_id', 'current_stock', 'expiry_date', 'days_to_expiry']]

class CustomerAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def get_customer_demographics(self):
        df = self.data['customers'].copy()
        
        gender_dist = df.groupby('gender').size().reset_index(name='count')
        gender_dist['percentage'] = (gender_dist['count'] / gender_dist['count'].sum() * 100).round(1)
        
        age_dist = df.groupby('age_group').size().reset_index(name='count')
        age_dist['percentage'] = (age_dist['count'] / age_dist['count'].sum() * 100).round(1)
        
        level_dist = df.groupby('member_level').agg({
            'total_spent': 'sum',
            'points': 'sum',
            'member_id': 'count'
        }).reset_index()
        level_dist['avg_spent'] = (level_dist['total_spent'] / level_dist['member_id']).round(2)
        
        return {'gender': gender_dist, 'age': age_dist, 'level': level_dist}
    
    def get_customer_behavior_summary(self):
        df = self.data['customer_behavior'].copy()
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M').astype(str)
        
        summary = df.groupby('month').agg({
            'spend_amount': 'sum',
            'items_count': 'sum',
            'stay_duration': 'mean',
            'satisfaction_score': 'mean',
            'visit_type': 'count'
        }).reset_index()
        
        summary['avg_spend'] = (summary['spend_amount'] / summary['visit_type']).round(2)
        summary['satisfaction_score'] = summary['satisfaction_score'].round(1)
        summary['stay_duration'] = summary['stay_duration'].round(1)
        
        return summary
    
    def get_visit_pattern(self):
        df = self.data['customer_behavior'].copy()
        pattern = df.groupby('weekday').agg({
            'visit_type': 'count',
            'spend_amount': 'sum',
            'satisfaction_score': 'mean'
        }).reset_index()
        
        pattern = pattern.set_index('weekday').reindex(['周一', '周二', '周三', '周四', '周五', '周六', '周日']).reset_index()
        pattern['avg_spend'] = (pattern['spend_amount'] / pattern['visit_type']).round(2)
        pattern['satisfaction_score'] = pattern['satisfaction_score'].round(1)
        
        return pattern
    
    def get_member_retention(self):
        df = self.data['customers'].copy()
        df['register_month'] = df['register_date'].dt.to_period('M').astype(str)
        df['last_visit_month'] = df['last_visit'].dt.to_period('M').astype(str)
        
        retention = df.groupby('register_month').agg({
            'member_id': 'count',
            'total_spent': 'sum',
            'points': 'sum'
        }).reset_index()
        
        return retention

class EmployeeAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def get_employee_summary(self):
        df = self.data['employees'].copy()
        
        dept_summary = df.groupby('department').agg({
            'employee_id': 'count',
            'salary': ['sum', 'mean']
        }).reset_index()
        dept_summary.columns = ['department', 'count', 'total_salary', 'avg_salary']
        dept_summary['avg_salary'] = dept_summary['avg_salary'].round(0)
        
        position_summary = df.groupby('position').agg({
            'employee_id': 'count',
            'salary': 'mean',
            'performance_score': 'mean'
        }).reset_index()
        position_summary['salary'] = position_summary['salary'].round(0)
        position_summary['performance_score'] = position_summary['performance_score'].round(1)
        
        return {'department': dept_summary, 'position': position_summary}
    
    def get_attendance_summary(self):
        df = self.data['attendance'].copy()
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M').astype(str)
        
        summary = df.groupby(['month', 'status']).size().unstack(fill_value=0).reset_index()
        
        numeric_cols = summary.select_dtypes(include=['int', 'float']).columns
        summary['total'] = summary[numeric_cols].sum(axis=1)
        summary['attendance_rate'] = (summary['正常'] / summary['total'] * 100).round(1)
        
        return summary
    
    def get_performance_ranking(self, top_n=10):
        df = self.data['employees'].copy()
        return df[df['status'] == '在职'].sort_values('performance_score', ascending=False).head(top_n)
    
    def get_workload_analysis(self):
        df = self.data['attendance'].copy()
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M').astype(str)
        
        workload = df.groupby(['month', 'employee_id']).agg({
            'work_hours': 'sum',
            'overtime_hours': 'sum'
        }).reset_index()
        
        workload['total_hours'] = workload['work_hours'] + workload['overtime_hours']
        monthly_avg = workload.groupby('month').agg({
            'work_hours': 'mean',
            'overtime_hours': 'mean',
            'total_hours': 'mean'
        }).reset_index()
        
        return monthly_avg.round(1)