# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

from src.data import load_all_data
from src.modules.data_analyzer import (
    SalesAnalyzer,
    InventoryAnalyzer,
    CustomerAnalyzer,
    EmployeeAnalyzer,
)
from src.modules.visualization_engine import VisualizationEngine


@st.cache_resource
def get_sales_analyzer():
    return SalesAnalyzer(load_all_data())


@st.cache_resource
def get_inventory_analyzer():
    return InventoryAnalyzer(load_all_data())


@st.cache_resource
def get_customer_analyzer():
    return CustomerAnalyzer(load_all_data())


@st.cache_resource
def get_employee_analyzer():
    return EmployeeAnalyzer(load_all_data())


@st.cache_resource
def get_viz_engine():
    return VisualizationEngine()


def backend_main():
    sales_analyzer = get_sales_analyzer()
    inventory_analyzer = get_inventory_analyzer()
    customer_analyzer = get_customer_analyzer()
    employee_analyzer = get_employee_analyzer()
    viz = get_viz_engine()

    menu_options = [
        "\U0001F4F1 数据概览",
        "\U0001F4DD 库存管理",
        "\U0001F465 客户管理",
        "\U0001F464 员工管理",
        "\U0001F4F0 销售分析",
        "\u2699\ufe0f 系统配置",
    ]
    selected_menu = st.sidebar.selectbox("功能菜单", menu_options, index=0)

    categories = ["全部", "文学小说", "科技科普", "儿童读物", "教育考试", "经管励志", "生活艺术"]
    selected_category = st.sidebar.selectbox("筛选类别", categories)

    stores = ["全部", "S1-总店", "S2-东区分店", "S3-西区分店", "S4-南区分店"]
    selected_store = st.sidebar.selectbox("选择门店", stores)

    # --- Data Overview ---
    if selected_menu == "\U0001F4F1 数据概览":
        st.markdown(
            "<h1 style='color:#e8e8f0;font-size:28px;font-weight:bold;'>"
            "\U0001F4F1 数据概览</h1><hr>",
            unsafe_allow_html=True,
        )
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.plotly_chart(
                viz.create_gauge_chart(value=92, title="系统健康度", height=200),
                use_container_width=True,
            )
        with col2:
            st.plotly_chart(
                viz.create_gauge_chart(value=88, title="数据完整性", height=200),
                use_container_width=True,
            )
        with col3:
            st.plotly_chart(
                viz.create_gauge_chart(value=98, title="服务可用性", height=200),
                use_container_width=True,
            )
        with col4:
            st.plotly_chart(
                viz.create_gauge_chart(value=75, title="库存健康度", height=200),
                use_container_width=True,
            )

        st.markdown("<hr>", unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            stock_status = inventory_analyzer.get_stock_status_distribution()
            status_fig = viz.create_pie_chart(
                stock_status,
                values_col="count",
                names_col="stock_status",
                title="库存状态分布",
                hole=0.4,
                height=350,
            )
            st.plotly_chart(status_fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        with col_b:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            category_sales = sales_analyzer.get_category_sales_distribution()
            sales_bar = viz.create_bar_chart(
                category_sales,
                x_col="category",
                y_col="sales_amount",
                title="品类销售额",
                height=350,
            )
            st.plotly_chart(sales_bar, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    # --- Inventory Management ---
    elif selected_menu == "\U0001F4DD 库存管理":
        st.markdown(
            "<h1 style='color:#e8e8f0;font-size:28px;font-weight:bold;'>"
            "\U0001F4DD 库存管理</h1><hr>",
            unsafe_allow_html=True,
        )
        tab1, tab2, tab3 = st.tabs(["库存概览", "库存预警", "库存流水"])
        with tab1:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            inventory_summary = inventory_analyzer.get_inventory_summary()
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(
                    viz.create_bar_chart(
                        inventory_summary,
                        x_col="category",
                        y_col="current_stock",
                        title="各分类库存总量",
                        height=400,
                    ),
                    use_container_width=True,
                )
            with col2:
                st.plotly_chart(
                    viz.create_bar_chart(
                        inventory_summary,
                        x_col="category",
                        y_col="total_value",
                        title="各分类库存价值",
                        height=400,
                    ),
                    use_container_width=True,
                )
            st.markdown(
                "<h4 style='color:rgba(232,232,240,0.6);font-size:14px;margin-top:16px;'>库存详情</h4>",
                unsafe_allow_html=True,
            )
            st.dataframe(inventory_summary, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        with tab2:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            st.markdown(
                "<h3 style='color:#e63946;font-size:16px;font-weight:600;margin-bottom:16px;'>"
                "\u26a0\ufe0f 低库存预警</h3>",
                unsafe_allow_html=True,
            )
            st.dataframe(
                inventory_analyzer.get_low_stock_alert(threshold=30),
                use_container_width=True,
            )
            st.markdown(
                "<h3 style='color:#ff6b35;font-size:16px;font-weight:600;margin-bottom:16px;margin-top:24px;'>"
                "\u23f3 临期商品预警</h3>",
                unsafe_allow_html=True,
            )
            st.dataframe(
                inventory_analyzer.get_expiry_alert(days_threshold=90),
                use_container_width=True,
            )
            st.markdown("</div>", unsafe_allow_html=True)
        with tab3:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            movement_data = inventory_analyzer.get_inventory_turnover()
            movement_fig = viz.create_line_chart(
                movement_data,
                x_col="month",
                y_col="quantity",
                color_col="category",
                title="月度库存变动",
                height=400,
            )
            st.plotly_chart(movement_fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    # --- Customer Management ---
    elif selected_menu == "\U0001F465 客户管理":
        st.markdown(
            "<h1 style='color:#e8e8f0;font-size:28px;font-weight:bold;'>"
            "\U0001F465 客户管理</h1><hr>",
            unsafe_allow_html=True,
        )
        tab1, tab2, tab3 = st.tabs(["客户画像", "行为分析", "会员管理"])
        with tab1:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            demographics = customer_analyzer.get_customer_demographics()
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(
                    viz.create_pie_chart(
                        demographics["gender"],
                        values_col="count",
                        names_col="gender",
                        title="性别分布",
                        hole=0.4,
                        height=350,
                    ),
                    use_container_width=True,
                )
            with col2:
                st.plotly_chart(
                    viz.create_bar_chart(
                        demographics["age"],
                        x_col="age_group",
                        y_col="count",
                        title="年龄分布",
                        height=350,
                    ),
                    use_container_width=True,
                )
            st.markdown(
                "<h4 style='color:rgba(232,232,240,0.6);font-size:14px;margin-top:16px;'>会员等级分布</h4>",
                unsafe_allow_html=True,
            )
            st.dataframe(demographics["level"], use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        with tab2:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            behavior_summary = customer_analyzer.get_customer_behavior_summary()
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(
                    viz.create_line_chart(
                        behavior_summary,
                        x_col="month",
                        y_col="spend_amount",
                        title="月度消费趋势",
                        height=350,
                    ),
                    use_container_width=True,
                )
            with col2:
                st.plotly_chart(
                    viz.create_line_chart(
                        behavior_summary,
                        x_col="month",
                        y_col="satisfaction_score",
                        title="满意度趋势",
                        height=350,
                    ),
                    use_container_width=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)
        with tab3:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            retention = customer_analyzer.get_member_retention()
            retention_fig = viz.create_area_chart(
                retention,
                x_col="register_month",
                y_col="member_id",
                title="会员注册趋势",
                height=400,
            )
            st.plotly_chart(retention_fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    # --- Employee Management ---
    elif selected_menu == "\U0001F464 员工管理":
        st.markdown(
            "<h1 style='color:#e8e8f0;font-size:28px;font-weight:bold;'>"
            "\U0001F464 员工管理</h1><hr>",
            unsafe_allow_html=True,
        )
        tab1, tab2, tab3 = st.tabs(["员工概览", "考勤管理", "绩效分析"])
        with tab1:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            emp_summary = employee_analyzer.get_employee_summary()
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(
                    viz.create_bar_chart(
                        emp_summary["department"],
                        x_col="department",
                        y_col="count",
                        title="部门人数分布",
                        height=350,
                    ),
                    use_container_width=True,
                )
            with col2:
                st.plotly_chart(
                    viz.create_bar_chart(
                        emp_summary["department"],
                        x_col="department",
                        y_col="total_salary",
                        title="部门工资总额",
                        height=350,
                    ),
                    use_container_width=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)
        with tab2:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            attendance_summary = employee_analyzer.get_attendance_summary()
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(
                    viz.create_line_chart(
                        attendance_summary,
                        x_col="month",
                        y_col="attendance_rate",
                        title="月度出勤率",
                        height=350,
                    ),
                    use_container_width=True,
                )
            with col2:
                workload = employee_analyzer.get_workload_analysis()
                st.plotly_chart(
                    viz.create_line_chart(
                        workload,
                        x_col="month",
                        y_col="total_hours",
                        title="月度工作时长",
                        height=350,
                    ),
                    use_container_width=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)
        with tab3:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            top_performers = employee_analyzer.get_performance_ranking(10)
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(
                    viz.create_bar_chart(
                        top_performers,
                        x_col="name",
                        y_col="performance_score",
                        title="绩效排名 Top10",
                        orientation="h",
                        height=400,
                    ),
                    use_container_width=True,
                )
            with col2:
                pos_summary = emp_summary["position"]
                st.plotly_chart(
                    viz.create_scatter_chart(
                        pos_summary,
                        x_col="salary",
                        y_col="performance_score",
                        size_col="employee_id",
                        title="薪资与绩效关系",
                        height=400,
                    ),
                    use_container_width=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)

    # --- Sales Analysis ---
    elif selected_menu == "\U0001F4F0 销售分析":
        st.markdown(
            "<h1 style='color:#e8e8f0;font-size:28px;font-weight:bold;'>"
            "\U0001F4F0 销售分析</h1><hr>",
            unsafe_allow_html=True,
        )
        tab1, tab2, tab3 = st.tabs(["销售趋势", "门店对比", "商品分析"])
        with tab1:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            monthly_sales = sales_analyzer.get_sales_trend(period="month")
            sales_growth = sales_analyzer.calculate_sales_growth()
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(
                    viz.create_line_chart(
                        monthly_sales,
                        x_col="period",
                        y_col="sales_amount",
                        title="月度销售额",
                        height=350,
                    ),
                    use_container_width=True,
                )
            with col2:
                growth_colors = [
                    "#00f5d4" if x >= 0 else "#e63946"
                    for x in sales_growth["growth_rate"]
                ]
                st.plotly_chart(
                    viz.create_bar_chart(
                        sales_growth,
                        x_col="period",
                        y_col="growth_rate",
                        title="销售增长率",
                        colors=growth_colors,
                        height=350,
                    ),
                    use_container_width=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)
        with tab2:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            store_performance = sales_analyzer.get_store_performance()
            store_fig = viz.create_line_chart(
                store_performance,
                x_col="period",
                y_col="sales_amount",
                color_col="store_id",
                title="各门店销售对比",
                height=400,
            )
            st.plotly_chart(store_fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        with tab3:
            st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
            top_products = sales_analyzer.get_top_products(15)
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(
                    viz.create_bar_chart(
                        top_products,
                        x_col="product_name",
                        y_col="total_amount",
                        color_col="category",
                        orientation="h",
                        title="热销商品 Top15",
                        height=450,
                    ),
                    use_container_width=True,
                )
            with col2:
                payment_dist = sales_analyzer.get_payment_method_distribution()
                st.plotly_chart(
                    viz.create_pie_chart(
                        payment_dist,
                        values_col="transaction_id",
                        names_col="payment_method",
                        title="支付方式占比",
                        hole=0.4,
                        height=450,
                    ),
                    use_container_width=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)

    # --- System Config ---
    elif selected_menu == "\u2699\ufe0f 系统配置":
        st.markdown(
            "<h1 style='color:#e8e8f0;font-size:28px;font-weight:bold;'>"
            "\u2699\ufe0f 系统配置</h1><hr>",
            unsafe_allow_html=True,
        )
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h3 class='section-title'>可视化配置</h3>", unsafe_allow_html=True)
            color_scheme = st.selectbox(
                "配色方案", ["深蓝色系", "绿色系", "紫色系", "暖色系列"]
            )
            refresh_interval = st.slider(
                "数据刷新间隔(秒)", 10, 300, 60, 10
            )
            show_legend = st.checkbox("显示图例", True)
            show_hover = st.checkbox("显示悬停提示", True)
            animation_enabled = st.checkbox("启用动画效果", True)
        with col2:
            st.markdown("<h3 class='section-title'>数据管理</h3>", unsafe_allow_html=True)
            auto_refresh = st.checkbox("自动刷新数据", True)
            data_retention = st.slider("数据保留天数", 30, 365, 90)
            backup_enabled = st.checkbox("启用自动备份", True)

        if st.button("保存配置", key="save_config"):
            st.markdown(
                "<div class='status-box status-success'>配置已保存！</div>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            "<div class='glass-panel' style='margin-top:20px;'>", unsafe_allow_html=True
        )
        st.markdown("<h3 class='section-title'>系统状态</h3>", unsafe_allow_html=True)

        system_metrics = [
            {"label": "CPU使用率", "value": "23%", "status": "normal"},
            {"label": "内存使用", "value": "45%", "status": "normal"},
            {"label": "磁盘空间", "value": "68%", "status": "warning"},
            {"label": "网络延迟", "value": "12ms", "status": "normal"},
        ]

        metric_cols = st.columns(4)
        for metric in system_metrics:
            with metric_cols[system_metrics.index(metric)]:
                css_class = (
                    "status-success" if metric["status"] == "normal" else "status-warning"
                )
                st.markdown(
                    f"<div class='{css_class}' style='padding:12px;text-align:center;border-radius:8px;'>"
                    f"<p style='color:rgba(232,232,240,0.6);font-size:12px;margin-bottom:4px;'>{metric['label']}</p>"
                    f"<p style='font-size:18px;font-weight:bold;'>{metric['value']}</p>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
        st.markdown("</div>", unsafe_allow_html=True)
