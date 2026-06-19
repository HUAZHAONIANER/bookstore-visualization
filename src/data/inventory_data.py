import pandas as pd
import numpy as np

def generate_inventory_data():
    categories = ['文学小说', '科技科普', '儿童读物', '教育考试', '经管励志', '生活艺术']
    sub_categories = {
        '文学小说': ['中国文学', '外国文学', '网络小说', '古典文学'],
        '科技科普': ['计算机', '科普读物', '人工智能', '自然科学'],
        '儿童读物': ['绘本', '童话', '科普百科', '学习辅导'],
        '教育考试': ['考研', '公务员', '职业资格', '语言学习'],
        '经管励志': ['管理学', '投资理财', '成功学', '经济学'],
        '生活艺术': ['烹饪美食', '旅行摄影', '家居生活', '艺术鉴赏']
    }
    
    stores = ['S1-总店', 'S2-东区分店', 'S3-西区分店', 'S4-南区分店']
    
    inventory = []
    product_id = 10000
    
    for cat in categories:
        for sub in sub_categories[cat]:
            for _ in range(10):
                product_id += 1
                base_stock = np.random.randint(50, 500)
                
                for store in stores:
                    stock = int(base_stock * (0.6 + np.random.random() * 0.8))
                    min_stock = int(base_stock * 0.2)
                    max_stock = int(base_stock * 1.5)
                    
                    inventory.append({
                        'product_id': f"P{str(product_id).zfill(5)}",
                        'category': cat,
                        'sub_category': sub,
                        'product_name': f"{sub}精选书籍{_+1}",
                        'store_id': store,
                        'current_stock': stock,
                        'min_stock': min_stock,
                        'max_stock': max_stock,
                        'unit_cost': round(10 + np.random.random() * 50, 2),
                        'unit_price': round(20 + np.random.random() * 100, 2),
                        'supplier': f"供应商{np.random.randint(1, 20)}",
                        'last_restock': pd.date_range('2024-01-01', '2024-12-31', periods=100)[np.random.randint(100)],
                        'expiry_date': pd.date_range('2025-01-01', '2027-12-31', periods=100)[np.random.randint(100)]
                    })
    
    df = pd.DataFrame(inventory)
    df['stock_status'] = np.where(df['current_stock'] < df['min_stock'], '库存不足',
                                 np.where(df['current_stock'] > df['max_stock'], '库存过多', '正常'))
    df['stock_utilization'] = (df['current_stock'] / df['max_stock'] * 100).round(1)
    df['days_to_expiry'] = (df['expiry_date'] - pd.Timestamp.now()).dt.days
    
    return df

def generate_inventory_movement():
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    categories = ['文学小说', '科技科普', '儿童读物', '教育考试', '经管励志', '生活艺术']
    stores = ['S1-总店', 'S2-东区分店', 'S3-西区分店', 'S4-南区分店']
    
    movements = []
    for date in dates:
        for cat in categories:
            for store in stores:
                if np.random.random() > 0.3:
                    movement_type = np.random.choice(['入库', '出库', '调拨'], p=[0.3, 0.5, 0.2])
                    quantity = np.random.randint(10, 200)
                    cost = round(quantity * (15 + np.random.random() * 40), 2)
                    
                    movements.append({
                        'movement_id': f"MV{date.strftime('%Y%m%d')}{str(np.random.randint(1000)).zfill(4)}",
                        'date': date,
                        'category': cat,
                        'store_id': store,
                        'movement_type': movement_type,
                        'quantity': quantity if movement_type != '调拨' else np.random.randint(-100, 100),
                        'cost': cost,
                        'reason': np.random.choice(['常规补货', '促销备货', '滞销处理', '门店调拨', '破损退货'])
                    })
    
    return pd.DataFrame(movements)