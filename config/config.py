import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, 'src', 'data')

STATIC_DIR = os.path.join(BASE_DIR, 'src', 'ui', 'static')

THEME_CONFIG = {
    'primary_color': '#2E7D32',
    'secondary_color': '#1B5E20',
    'background_color': '#FAFAFA',
    'text_color': '#333333',
    'accent_color': '#FF9800'
}

CHARTS_CONFIG = {
    'line_chart': {'title_font_size': 16, 'legend_position': 'bottom'},
    'bar_chart': {'title_font_size': 16, 'legend_position': 'right'},
    'pie_chart': {'title_font_size': 16, 'legend_position': 'right'},
    'scatter_chart': {'title_font_size': 16, 'legend_position': 'bottom'},
    'heatmap': {'title_font_size': 16, 'annotations': True}
}

TOUCH_CONFIG = {
    "min_touch_target": 44,
    "slider_step_size": 10,
    "padding": 12,
    "checkbox_size": 20
}
