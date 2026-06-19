import pandas as pd
import numpy as np

def generate_customer_data():
    member_ids = [f"M{str(i).zfill(5)}" for i in range(10000, 99999)]
    
    customers = []
    for member_id in member_ids[:5000]:
        gender = np.random.choice(['男', '女'], p=[0.48, 0.52])
        age_group = np.random.choice(['18-25', '26-35', '36-45', '46-55', '55+'], 
                                    p=[0.2, 0.3, 0.25, 0.15, 0.1])
        register_date = pd.date_range('2020-01-01', '2024-12-31', periods=1000)[np.random.randint(1000)]
        member_level = np.random.choice(['普通会员', '银卡会员', '金卡会员', '钻石会员'],
                                       p=[0.5, 0.25, 0.15, 0.1])
        
        discount_rate = {'普通会员': 0.05, '银卡会员': 0.1, '金卡会员': 0.15, '钻石会员': 0.2}[member_level]
        total_spent = round(np.random.random() * 50000, 2)
        points = int(total_spent * 0.1)
        
        customers.append({
            'member_id': member_id,
            'name': f"会员{member_id[-4:]}",
            'gender': gender,
            'age_group': age_group,
            'register_date': register_date,
            'member_level': member_level,
            'discount_rate': discount_rate,
            'total_spent': total_spent,
            'points': points,
            'phone': f"1{np.random.randint(3, 10)}{str(np.random.randint(100000000, 999999999))}",
            'email': f"member{member_id[-4:]}@bookstore.com",
            'preferred_category': np.random.choice(['文学小说', '科技科普', '儿童读物', '教育考试', '经管励志', '生活艺术']),
            'last_visit': pd.date_range('2024-01-01', '2024-12-31', periods=365)[np.random.randint(365)]
        })
    
    return pd.DataFrame(customers)

def generate_customer_behavior():
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    member_ids = [f"M{str(i).zfill(5)}" for i in range(10000, 15000)]
    
    behaviors = []
    for date in dates:
        weekday = date.weekday()
        visit_count = int(200 + np.random.random() * 300) if weekday < 5 else int(400 + np.random.random() * 400)
        
        for _ in range(visit_count):
            member_id = member_ids[np.random.randint(len(member_ids))] if np.random.random() > 0.3 else None
            spend_amount = round(np.random.random() * 500, 2) if np.random.random() > 0.2 else 0
            
            behaviors.append({
                'date': date,
                'weekday': ['周一', '周二', '周三', '周四', '周五', '周六', '周日'][weekday],
                'member_id': member_id,
                'visit_type': np.random.choice(['到店', '线上', '电话订购']),
                'spend_amount': spend_amount,
                'items_count': np.random.randint(1, 10) if spend_amount > 0 else 0,
                'stay_duration': np.random.randint(10, 180),
                'satisfaction_score': round(3 + np.random.random() * 2, 1)
            })
    
    return pd.DataFrame(behaviors)