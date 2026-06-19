import pandas as pd
import numpy as np

def generate_sales_data():
    months = ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-06',
              '2024-07', '2024-08', '2024-09', '2024-10', '2024-11', '2024-12']
    
    categories = ['文学小说', '科技科普', '儿童读物', '教育考试', '经管励志', '生活艺术']
    
    data = []
    for month in months:
        for category in categories:
            base_sales = {
                '文学小说': 85000,
                '科技科普': 62000,
                '儿童读物': 48000,
                '教育考试': 72000,
                '经管励志': 55000,
                '生活艺术': 38000
            }
            seasonal_factor = {
                '2024-01': 0.9, '2024-02': 1.1, '2024-03': 1.0,
                '2024-04': 1.05, '2024-05': 1.02, '2024-06': 1.15,
                '2024-07': 1.3, '2024-08': 1.25, '2024-09': 1.1,
                '2024-10': 1.08, '2024-11': 1.2, '2024-12': 1.4
            }
            sales = int(base_sales[category] * seasonal_factor[month] * (0.9 + np.random.random() * 0.2))
            quantity = int(sales / (30 + np.random.random() * 70))
            data.append({
                '月份': month,
                '类别': category,
                '销售额': sales,
                '销售数量': quantity
            })
    
    return pd.DataFrame(data)

def generate_customer_data():
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = []
    
    for date in dates:
        weekday = date.weekday()
        base_count = 800 if weekday < 5 else 1200
        customers = int(base_count * (0.7 + np.random.random() * 0.6))
        members = int(customers * (0.3 + np.random.random() * 0.2))
        new_members = int(members * (0.05 + np.random.random() * 0.05))
        avg_spending = round(60 + np.random.random() * 40, 2)
        
        data.append({
            '日期': date.strftime('%Y-%m-%d'),
            '星期': ['周一', '周二', '周三', '周四', '周五', '周六', '周日'][weekday],
            '客流量': customers,
            '会员数': members,
            '新增会员': new_members,
            '客单价': avg_spending
        })
    
    return pd.DataFrame(data)

def generate_inventory_data():
    categories = ['文学小说', '科技科普', '儿童读物', '教育考试', '经管励志', '生活艺术']
    locations = ['A区-一楼', 'B区-二楼', 'C区-三楼', 'D区-四楼']
    
    data = []
    for category in categories:
        for location in locations:
            stock = int(200 + np.random.random() * 500)
            min_stock = int(100 + np.random.random() * 100)
            max_stock = int(500 + np.random.random() * 300)
            turnover_days = round(15 + np.random.random() * 20, 1)
            data.append({
                '类别': category,
                '存放区域': location,
                '当前库存': stock,
                '最低库存': min_stock,
                '最高库存': max_stock,
                '周转天数': turnover_days
            })
    
    return pd.DataFrame(data)

def generate_employee_data():
    departments = ['销售部', '采购部', '仓储部', '客服部', '财务部', '运营部']
    positions = ['经理', '主管', '专员', '实习生']
    
    data = []
    for dept in departments:
        for pos in positions:
            count = {
                '经理': 1,
                '主管': 2,
                '专员': [8, 6, 10, 5, 4, 3][departments.index(dept)],
                '实习生': 2
            }[pos]
            
            avg_salary = {
                '经理': 15000,
                '主管': 10000,
                '专员': 6000,
                '实习生': 2500
            }[pos]
            
            data.append({
                '部门': dept,
                '职位': pos,
                '人数': count,
                '平均薪资': avg_salary
            })
    
    return pd.DataFrame(data)

def generate_book_ranking():
    categories = ['文学小说', '科技科普', '儿童读物', '教育考试', '经管励志', '生活艺术']
    book_names = {
        '文学小说': ['人间失格', '百年孤独', '活着', '围城', '三体', '红楼梦'],
        '科技科普': ['时间简史', '自私的基因', '宇宙的琴弦', '枪炮病菌与钢铁', '人类简史', '未来简史'],
        '儿童读物': ['小王子', '夏洛的网', '窗边的小豆豆', '草房子', '格林童话', '安徒生童话'],
        '教育考试': ['考研英语真题', '公务员行测', '教师资格证', 'CPA会计', '司法考试', '四六级真题'],
        '经管励志': ['穷查理宝典', '原则', '思考快与慢', '刻意练习', '高效能人士', '黑天鹅'],
        '生活艺术': ['断舍离', '小王子', '深夜食堂', '小森林', '面包与玫瑰', '人间草木']
    }
    
    data = []
    for category in categories:
        for i, book in enumerate(book_names[category], 1):
            sales = int(1000 + np.random.random() * 5000)
            rating = round(4.0 + np.random.random() * 1.0, 1)
            price = round(20 + np.random.random() * 60, 2)
            data.append({
                '排名': i,
                '书名': book,
                '类别': category,
                '销量': sales,
                '评分': rating,
                '价格': price
            })
    
    return pd.DataFrame(data)

def generate_monthly_metrics():
    months = ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-06',
              '2024-07', '2024-08', '2024-09', '2024-10', '2024-11', '2024-12']
    
    data = []
    for month in months:
        data.append({
            '月份': month,
            '总销售额': int(350000 + np.random.random() * 200000),
            '订单数': int(4000 + np.random.random() * 2000),
            '客户满意度': round(85 + np.random.random() * 10, 1),
            '库存周转率': round(2.5 + np.random.random() * 1.5, 2),
            '退货率': round(2 + np.random.random() * 2, 2),
            '促销活动次数': int(np.random.random() * 5)
        })
    
    return pd.DataFrame(data)

def load_all_data():
    return {
        'sales': generate_sales_data(),
        'customers': generate_customer_data(),
        'inventory': generate_inventory_data(),
        'employees': generate_employee_data(),
        'book_ranking': generate_book_ranking(),
        'monthly_metrics': generate_monthly_metrics()
    }