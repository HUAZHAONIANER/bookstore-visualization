# -*- coding: utf-8 -*-
import streamlit as st
import sys
import os as _os

sys.path.append(_os.path.dirname(_os.path.abspath(__file__)))

from src.ui.frontend import frontend_main
from src.ui.backend import backend_main


def load_global_css():
    return """
    <style>
    * { font-family: 'Microsoft YaHei', 'PingFang SC', 'Hiragino Sans GB', sans-serif; }

    /* Deep Space Background */
    .stApp {
        background: linear-gradient(160deg, #080c1a 0%, #0f1428 30%, #1a0a2e 60%, #080c1a 100%);
        min-height: 100vh;
    }
    .reportview-container { background: transparent; min-height: 100vh; }

    /* Parallax Scroll */
    .main > div { perspective: 1px; overflow-x: hidden; scroll-behavior: smooth; }
    .main > div > div { transform-style: preserve-3d; }

    /* Sidebar - Dark Glass */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, rgba(15,20,40,0.95) 0%, rgba(26,10,46,0.95) 50%, rgba(8,12,26,0.95) 100%);
        border-right: 1px solid rgba(108,43,217,0.3);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
    }
    .sidebar .sidebar-content .block-container { padding: 20px; }

    /* Frosted Glass Panels */
    .glass-panel {
        background: rgba(255,255,255,0.04);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(108,43,217,0.2);
        border-radius: 12px;
        padding: 20px;
        transition: all 0.3s ease;
    }
    .glass-panel:hover {
        border-color: rgba(108,43,217,0.4);
        box-shadow: 0 8px 32px rgba(108,43,217,0.15);
    }

    /* KPI Cards */
    .metric-card {
        position: relative;
        background: rgba(255,255,255,0.04);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(0,180,216,0.2);
        border-radius: 12px;
        padding: 20px;
        overflow: hidden;
        transition: all 0.3s ease;
        animation: fadeInUp 0.5s ease-out both;
    }
    .metric-card::before {
        content: '';
        position: absolute; top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, #6c2bd9, #00b4d8, #00f5d4);
    }
    .metric-card:hover {
        transform: translateY(-4px);
        border-color: rgba(108,43,217,0.4);
        box-shadow: 0 12px 40px rgba(108,43,217,0.2), inset 0 0 30px rgba(0,180,216,0.05);
    }

    /* Section Title */
    .section-title {
        color: #e8e8f0; font-size: 18px; font-weight: 600;
        margin-bottom: 16px; padding-bottom: 8px;
        border-bottom: 2px solid transparent;
        border-image: linear-gradient(90deg, #6c2bd9, #00b4d8) 1;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #6c2bd9 0%, #00b4d8 100%);
        color: white; border-radius: 8px; border: none;
        padding: 10px 24px; font-weight: 600; font-size: 14px;
        box-shadow: 0 4px 15px rgba(108,43,217,0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #7c3bff 0%, #00c4e8 100%);
        box-shadow: 0 6px 20px rgba(108,43,217,0.5);
        transform: translateY(-2px);
    }

    /* Selectbox */
    .stSelectbox>div>div>select {
        background: rgba(255,255,255,0.06); color: #e8e8f0;
        border-radius: 8px; border: 1px solid rgba(108,43,217,0.3);
        padding: 8px 12px;
    }
    .stSelectbox>div>div>select:hover { border-color: #00b4d8; }

    /* Slider */
    .stSlider>div>div>div>div { background: linear-gradient(90deg, #6c2bd9, #00b4d8); }

    /* Animations */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes fadeInScale {
        from { opacity: 0; transform: scale(0.95); }
        to { opacity: 1; transform: scale(1); }
    }
    @keyframes ripple {
        0% { box-shadow: 0 0 0 0 rgba(108,43,217,0.4); }
        100% { box-shadow: 0 0 0 20px rgba(108,43,217,0); }
    }
    @keyframes glowPulse {
        0%, 100% { box-shadow: 0 0 5px rgba(0,180,216,0.2); }
        50% { box-shadow: 0 0 20px rgba(0,180,216,0.4); }
    }

    .animate-fade-in { animation: fadeInUp 0.5s ease-out both; }
    .animate-slide-in { animation: slideInRight 0.3s ease-out both; }
    .animate-scale-in { animation: fadeInScale 0.4s ease-out both; }
    .animate-ripple { animation: ripple 1s ease-out; }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px; background: rgba(255,255,255,0.03);
        border-radius: 10px; padding: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px; padding: 8px 16px;
        color: rgba(232,232,240,0.6); transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(108,43,217,0.3), rgba(0,180,216,0.2));
        color: #e8e8f0 !important;
        box-shadow: 0 0 15px rgba(108,43,217,0.2);
    }

    /* Dataframe */
    .stDataFrame { background: rgba(255,255,255,0.03); border-radius: 12px; }
    .stDataFrame table { color: #e8e8f0; }

    /* Status Boxes */
    .status-box { border-radius: 8px; padding: 12px 16px; border-left: 4px solid; }
    .status-success { background: rgba(0,245,212,0.08); border-color: #00f5d4; color: #00f5d4; }
    .status-warning { background: rgba(255,107,53,0.08); border-color: #ff6b35; color: #ff6b35; }
    .status-danger { background: rgba(230,57,70,0.08); border-color: #e63946; color: #e63946; }

    hr { border-color: rgba(108,43,217,0.15); opacity: 0.5; margin: 16px 0; }

    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: rgba(8,12,26,0.5); }
    ::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #6c2bd9, #00b4d8); border-radius: 4px; }

    .stCheckbox>label { color: rgba(232,232,240,0.8); }

    h1, h2, h3, h4, h5, h6, p, li, span, label { color: #e8e8f0; }
    </style>
    """


def main():
    st.set_page_config(
        page_title="大型图书城数据可视化系统",
        page_icon="\U0001F4DA",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.markdown(load_global_css(), unsafe_allow_html=True)

    st.sidebar.markdown(
        '<div style="text-align: center; padding: 20px 0;">'
        '<div style="font-size: 36px; margin-bottom: 8px;">\U0001F4DA</div>'
        '<h3 style="color: #e8e8f0; font-size: 18px; font-weight: bold; margin: 0; '
        'background: linear-gradient(90deg, #6c2bd9, #00b4d8); '
        '-webkit-background-clip: text; '
        '-webkit-text-fill-color: transparent; background-clip: text;">'
        '图书城数据可视化系统</h3>'
        '<p style="color: rgba(232,232,240,0.5); font-size: 12px; margin: 4px 0 0;">'
        '实时监控 \u00b7 智能分析 \u00b7 数据驱动</p>'
        '</div>',
        unsafe_allow_html=True
    )
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    page = st.sidebar.selectbox(
        "选择界面",
        ["前台用户界面", "后台管理界面"],
        index=0,
        key="main_page_selector",
        format_func=lambda x: "\U0001F465 " + x if x == "前台用户界面" else "\U0001F4E1 " + x,
    )

    if page == "前台用户界面":
        frontend_main()
    else:
        backend_main()


if __name__ == "__main__":
    main()
