# 大型图书城数据可视化系统

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.32.0-red.svg)
![Plotly](https://img.shields.io/badge/plotly-5.18.0-green.svg)

基于Python数据可视化课程的结课项目，以大型图书城为业务背景，开发的一套完整的数据可视化系统。

## 功能特性

### 🎯 前台用户界面
- **数据概览卡片**：展示关键运营指标（销售额、订单数、满意度、周转率）
- **销售趋势分析**：月度销售趋势折线图，支持类别筛选
- **品类分析**：品类销售占比饼图、各类别销售额对比柱状图
- **客户分析**：一周客流量变化、会员到店情况、日均客单价分析
- **畅销排行**：Top N畅销书籍排行，支持类别筛选和评分关系分析

### 🛠️ 后台管理界面
- **数据概览**：关键指标相关性热力图、库存状态分布
- **库存管理**：库存数据表格展示，支持区域筛选
- **员工管理**：部门人员分布、薪资总额分析
- **数据关联分析**：销售数量与销售额关系、库存利用率热力图
- **可视化配置**：图表配色、刷新间隔、显示设置等配置项
- **系统状态监控**：健康度、数据完整性、服务可用性仪表盘

## 技术栈

- **框架**: Streamlit 1.32.0
- **数据处理**: Pandas 2.2.1, NumPy 1.26.4
- **可视化**: Plotly 5.18.0, Matplotlib 3.8.3, Seaborn 0.13.2
- **运行环境**: Python 3.8+

## 快速开始

### 环境要求
- Python 3.8 及以上版本
- 建议使用虚拟环境

### 安装步骤

```bash
# 进入项目目录
cd bookstore_visualization

# 创建虚拟环境（可选）
python -m venv venv

# 激活虚拟环境
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 运行方式

```bash
# 启动Streamlit应用
streamlit run app.py
```

运行成功后，打开浏览器访问显示的本地地址（通常是 http://localhost:8501）

## 项目结构

```
├── app.py                    # 主应用入口
├── config/                   # 配置文件目录
│   └── config.py             # 系统配置
├── docs/                     # 文档目录
│   └── PROJECT_DOCUMENT.md   # 项目文档
├── requirements.txt          # 依赖清单
└── src/                      # 源代码目录
    ├── data/                 # 数据模块
    │   ├── __init__.py
    │   ├── customer_data.py
    │   ├── employee_data.py
    │   ├── inventory_data.py
    │   ├── mock_data.py
    │   └── sales_data.py
    ├── modules/              # 核心模块
    │   ├── __init__.py
    │   ├── data_analyzer.py
    │   └── visualization_engine.py
    └── ui/                   # 用户界面
        ├── backend.py
        └── frontend.py
```

## 可视化功能

| 图表类型 | 应用场景 |
|----------|----------|
| 折线图 | 销售趋势、客流量变化 |
| 柱状图 | 品类对比、库存分布、薪资分析 |
| 饼图 | 销售占比、库存状态分布 |
| 散点图 | 价格销量关系、库存周转关系 |
| 热力图 | 指标相关性、库存利用率 |
| 仪表盘 | 系统状态监控 |

## 项目亮点

1. **模块化设计**: 清晰的分层架构，代码易于维护和扩展
2. **交互式可视化**: 丰富的交互功能，提升用户体验
3. **响应式布局**: 使用Streamlit实现自适应界面
4. **数据模拟**: 完整的模拟数据生成，无需数据库支持
5. **专业图表**: 符合企业级应用标准的可视化效果

## 扩展建议

- 数据库集成：接入真实数据库
- 用户认证：添加登录系统
- 数据导出：支持Excel/PDF导出
- 邮件报告：定时发送数据报告
- 地图可视化：门店分布展示

## 使用说明

### 前台界面操作
1. 在首页查看数据概览卡片，了解实时运营指标
2. 使用侧边栏筛选条件查看不同维度的数据
3. 点击图表可查看详细数据点信息
4. 支持导出图表为PNG/PDF格式

### 后台管理操作
1. 点击侧边栏"后台管理"切换到管理界面
2. 查看库存状态和员工分布情况
3. 通过热力图分析指标相关性
4. 调整可视化配置项自定义展示效果

## 故障排除

### 常见问题

**Q: Streamlit启动失败？**
- 确保Python版本 >= 3.8
- 检查端口8501是否被占用
- 尝试重新安装依赖：`pip install --upgrade -r requirements.txt`

**Q: 图表不显示？**
- 检查网络连接
- 确保Plotly版本正确
- 清除浏览器缓存后重试

**Q: 数据显示异常？**
- 检查mock_data.py是否正常生成数据
- 确认data目录下的文件完整

## 贡献指南

欢迎贡献代码！请遵循以下流程：

1. Fork本仓库
2. 创建特性分支：`git checkout -b feature-name`
3. 提交更改：`git commit -m 'Add some feature'`
4. 推送到分支：`git push origin feature-name`
5. 提交Pull Request

## License

MIT License

## 作者

HUAZHAONIANER

---

**项目版本**: v1.0  
**创建日期**: 2026年  
**开发工具**: Python + Streamlit + Plotly  
**联系邮箱**: 1487610440@qq.com