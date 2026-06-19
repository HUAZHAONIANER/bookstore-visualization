import pandas as pd
import numpy as np

def generate_employee_data():
    departments = ['销售部', '采购部', '仓储部', '客服部', '财务部', '运营部', '人力资源部', '市场部']
    positions = {
        '销售部': ['销售经理', '销售主管', '销售员', '导购员'],
        '采购部': ['采购经理', '采购专员', '供应商管理'],
        '仓储部': ['仓库经理', '仓管员', '物流专员'],
        '客服部': ['客服经理', '客服专员', '售后专员'],
        '财务部': ['财务经理', '会计', '出纳', '审计'],
        '运营部': ['运营总监', '运营经理', '数据分析员', '系统管理员'],
        '人力资源部': ['HR经理', '招聘专员', '培训专员'],
        '市场部': ['市场经理', '品牌推广', '活动策划']
    }
    
    employees = []
    emp_id = 1000
    
    for dept in departments:
        for pos in positions[dept]:
            count = {'经理': 1, '总监': 1, '主管': 2, '专员': np.random.randint(3, 8), 
                     '销售员': np.random.randint(10, 20), '导购员': np.random.randint(5, 10),
                     '仓管员': np.random.randint(4, 8), '会计': 3, '出纳': 2, 
                     '审计': 2, '数据分析员': np.random.randint(2, 4), '系统管理员': 2,
                     '招聘专员': 2, '培训专员': 2, '品牌推广': np.random.randint(2, 4),
                     '活动策划': np.random.randint(2, 4), '售后专员': np.random.randint(3, 6),
                     '物流专员': np.random.randint(2, 4), '供应商管理': np.random.randint(2, 4)}.get(pos, np.random.randint(2, 5))
            
            for _ in range(count):
                emp_id += 1
                salary = {
                    '总监': 25000 + np.random.randint(5000, 10000),
                    '经理': 15000 + np.random.randint(3000, 5000),
                    '主管': 10000 + np.random.randint(2000, 3000),
                    '专员': 6000 + np.random.randint(1000, 2000),
                    '销售员': 4000 + np.random.randint(1000, 2000),
                    '导购员': 3000 + np.random.randint(500, 1000),
                    '仓管员': 3500 + np.random.randint(500, 1000),
                    '会计': 7000 + np.random.randint(1000, 2000),
                    '出纳': 5000 + np.random.randint(500, 1000),
                    '审计': 8000 + np.random.randint(1000, 2000),
                    '数据分析员': 7000 + np.random.randint(1000, 2000),
                    '系统管理员': 6000 + np.random.randint(1000, 2000),
                    '招聘专员': 5000 + np.random.randint(500, 1000),
                    '培训专员': 5000 + np.random.randint(500, 1000),
                    '品牌推广': 6000 + np.random.randint(1000, 2000),
                    '活动策划': 6000 + np.random.randint(1000, 2000),
                    '售后专员': 4000 + np.random.randint(500, 1000),
                    '物流专员': 4000 + np.random.randint(500, 1000),
                    '供应商管理': 6000 + np.random.randint(1000, 2000)
                }.get(pos, 5000)
                
                employees.append({
                    'employee_id': f"E{str(emp_id).zfill(4)}",
                    'name': f"员工{emp_id}",
                    'department': dept,
                    'position': pos,
                    'gender': np.random.choice(['男', '女'], p=[0.55, 0.45]),
                    'age': np.random.randint(22, 55),
                    'hire_date': pd.date_range('2018-01-01', '2024-12-31', periods=200)[np.random.randint(200)],
                    'salary': salary,
                    'performance_score': round(60 + np.random.random() * 35, 1),
                    'status': np.random.choice(['在职', '休假', '离职'], p=[0.95, 0.03, 0.02]),
                    'store_id': np.random.choice(['S1-总店', 'S2-东区分店', 'S3-西区分店', 'S4-南区分店', '总部'])
                })
    
    return pd.DataFrame(employees)

def generate_attendance_data():
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    employee_ids = [f"E{str(i).zfill(4)}" for i in range(1001, 1150)]
    
    attendance = []
    for date in dates:
        for emp_id in employee_ids[:80]:
            status = np.random.choice(['正常', '迟到', '早退', '请假', '旷工'], 
                                     p=[0.85, 0.05, 0.03, 0.06, 0.01])
            work_hours = 8 if status == '正常' else np.random.randint(4, 8)
            
            attendance.append({
                'date': date,
                'employee_id': emp_id,
                'status': status,
                'work_hours': work_hours,
                'overtime_hours': np.random.randint(0, 4) if np.random.random() > 0.7 else 0
            })
    
    return pd.DataFrame(attendance)