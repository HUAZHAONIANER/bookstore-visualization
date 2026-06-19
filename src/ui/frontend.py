# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

from src.data import load_all_data
from src.modules.data_analyzer import SalesAnalyzer, CustomerAnalyzer
from src.modules.visualization_engine import VisualizationEngine


@st.cache_resource
def get_sales_analyzer():
    return SalesAnalyzer(load_all_data())


@st.cache_resource
def get_customer_analyzer():
    return CustomerAnalyzer(load_all_data())


@st.cache_resource
def get_viz_engine():
    return VisualizationEngine()


def frontend_main():
    sales_analyzer = get_sales_analyzer()
    customer_analyzer = get_customer_analyzer()
    viz = get_viz_engine()

    # Title
    st.markdown(
        "<h1 style='color:#e8e8f0;font-size:28px;font-weight:bold;margin-bottom:0;'>"
        "\U0001F4F1 图书城运营数据总览</h1>"
        "<p style='color:rgba(232,232,240,0.6);font-size:14px;margin-top:4px;'>"
        "实时监控 \u00b7 智能分析 \u00b7 数据驱动</p><hr>",
        unsafe_allow_html=True,
    )

    # ===== Phase 1: Core KPIs =====
    monthly_sales = sales_analyzer.get_sales_trend(period="month")
    latest_sales = monthly_sales.iloc[-1]["sales_amount"]
    prev_sales = monthly_sales.iloc[-2]["sales_amount"]
    sales_growth = ((latest_sales - prev_sales) / prev_sales * 100).round(1)

    customer_behavior = customer_analyzer.get_customer_behavior_summary()
    latest_customers = customer_behavior.iloc[-1]["visit_type"]
    avg_satisfaction = customer_behavior.iloc[-1]["satisfaction_score"]
    avg_order_value = monthly_sales.iloc[-1]["avg_order_value"]

    top_products = sales_analyzer.get_top_products(5)
    total_orders = top_products["transaction_id"].sum()

    col1, col2, col3, col4, col5 = st.columns(5)

    kpi_data = [
        (col1, latest_sales, "月度销售额", "\u00a5{:,.0f}", True, sales_growth),
        (col2, latest_customers, "月度客流", "{:,}", False, None),
        (col3, avg_satisfaction, "客户满意度", "{}", False, None),
        (col4, avg_order_value, "客单价", "\u00a5{:.0f}", False, None),
        (col5, total_orders, "热销订单", "{:,}", False, None),
    ]

    for col, value, label, fmt, show_growth, growth in kpi_data:
        with col:
            growth_html = ""
            if show_growth and growth is not None:
                arrow = "\u25b4" if growth >= 0 else "\u25be"
                gcolor = "#00f5d4" if growth >= 0 else "#e63946"
                growth_html = (
                    f'<p style="color:{gcolor};font-size:12px;font-weight:500;">'
                    f"{arrow} {abs(growth)}%</p>"
                )
            st.markdown(
                '<div class="metric-card">'
                f'<p style="color:rgba(232,232,240,0.6);font-size:12px;margin-bottom:8px;">{label}</p>'
                f'<p style="color:#e8e8f0;font-size:24px;font-weight:bold;margin-bottom:4px;">'
                f"{fmt.format(value)}</p>{growth_html}</div>",
                unsafe_allow_html=True,
            )

    st.markdown("<hr>", unsafe_allow_html=True)

    # ===== Phase 2: Charts =====
    tab1, tab2, tab3, tab4 = st.tabs([
        "\U0001F4F0 销售趋势",
        "\U0001F465 客户分析",
        "\U0001F4F1 畅销排行",
        "\U0001F4F1 品类分析",
    ])

    with tab1:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("<h3 class='section-title'>销售趋势分析</h3>", unsafe_allow_html=True)

        col_filter = st.columns(2)
        with col_filter[0]:
            category_filter = st.selectbox(
                "选择图书类别",
                ["全部"]
                + list(
                    sales_analyzer.get_category_sales_distribution()["category"].unique()
                ),
                key="sales_category_filter",
            )
        with col_filter[1]:
            store_filter = st.selectbox(
                "选择门店",
                ["全部", "S1-总店", "S2-东区分店", "S3-西区分店", "S4-南区分店"],
                key="sales_store_filter",
            )

        trend_data = sales_analyzer.get_sales_trend(
            period="month",
            category=category_filter if category_filter != "全部" else None,
            store_id=store_filter if store_filter != "全部" else None,
        )
        sales_fig = viz.create_line_chart(
            trend_data,
            x_col="period",
            y_col="sales_amount",
            title="月度销售额趋势",
            labels={"period": "月份", "sales_amount": "销售额"},
            height=400,
        )
        st.plotly_chart(sales_fig, use_container_width=True)

        col_a, col_b = st.columns(2)
        with col_a:
            growth_data = sales_analyzer.calculate_sales_growth()
            growth_fig = viz.create_bar_chart(
                growth_data,
                x_col="period",
                y_col="growth_rate",
                title="销售增长率",
                labels={"period": "月份", "growth_rate": "增长率(%)"},
                colors=[
                    "#00f5d4" if x >= 0 else "#e63946"
                    for x in growth_data["growth_rate"]
                ],
                height=350,
            )
            st.plotly_chart(growth_fig, use_container_width=True)
        with col_b:
            payment_dist = sales_analyzer.get_payment_method_distribution()
            payment_fig = viz.create_pie_chart(
                payment_dist,
                values_col="total_amount",
                names_col="payment_method",
                title="支付方式分布",
                hole=0.4,
                height=350,
            )
            st.plotly_chart(payment_fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("<h3 class='section-title'>客户数据分析</h3>", unsafe_allow_html=True)

        visit_pattern = customer_analyzer.get_visit_pattern()
        visit_fig = viz.create_line_chart(
            visit_pattern,
            x_col="weekday",
            y_col="visit_type",
            title="一周客流量变化",
            labels={"weekday": "星期", "visit_type": "客流量"},
            height=400,
        )
        st.plotly_chart(visit_fig, use_container_width=True)

        col_c, col_d = st.columns(2)
        with col_c:
            demographics = customer_analyzer.get_customer_demographics()
            gender_fig = viz.create_pie_chart(
                demographics["gender"],
                values_col="count",
                names_col="gender",
                title="会员性别分布",
                hole=0.4,
                height=350,
            )
            st.plotly_chart(gender_fig, use_container_width=True)
        with col_d:
            age_fig = viz.create_bar_chart(
                demographics["age"],
                x_col="age_group",
                y_col="count",
                title="会员年龄分布",
                labels={"age_group": "年龄段", "count": "人数"},
                height=350,
            )
            st.plotly_chart(age_fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab3:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("<h3 class='section-title'>畅销书籍排行</h3>", unsafe_allow_html=True)

        top_n = st.slider("展示数量", min_value=5, max_value=20, value=10, key="top_n_slider")
        top_books = sales_analyzer.get_top_products(top_n)

        ranking_fig = viz.create_bar_chart(
            top_books,
            x_col="product_name",
            y_col="total_amount",
            title=f"Top {top_n} 畅销书籍",
            color_col="category",
            labels={"product_name": "书名", "total_amount": "销售额"},
            orientation="h",
            height=500,
        )
        st.plotly_chart(ranking_fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab4:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("<h3 class='section-title'>品类销售分析</h3>", unsafe_allow_html=True)

        category_dist = sales_analyzer.get_category_sales_distribution()

        col_e, col_f = st.columns(2)
        with col_e:
            category_pie = viz.create_pie_chart(
                category_dist,
                values_col="sales_amount",
                names_col="category",
                title="品类销售占比",
                hole=0.4,
                height=400,
            )
            st.plotly_chart(category_pie, use_container_width=True)
        with col_f:
            category_bar = viz.create_bar_chart(
                category_dist,
                x_col="category",
                y_col="sales_amount",
                title="各分类销售额",
                labels={"category": "类别", "sales_amount": "销售额"},
                height=400,
            )
            st.plotly_chart(category_bar, use_container_width=True)

        st.markdown(
            "<h4 style='color:rgba(232,232,240,0.6);font-size:14px;margin-top:16px;'>详细数据</h4>",
            unsafe_allow_html=True,
        )
        st.dataframe(category_dist, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
