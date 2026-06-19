import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

class VisualizationEngine:
    def __init__(self):
        self.color_palettes = {
            'primary': ['#00b4d8', '#0096c7', '#0077b6', '#023e8a', '#6c2bd9'],
            'success': ['#00f5d4', '#00c9a7', '#00a896', '#028090', '#05668d'],
            'warning': ['#ff6b35', '#f7931e', '#f7b731', '#ff9f1c', '#ffbf69'],
            'danger': ['#e63946', '#f94144', '#f3722c', '#f8961e', '#ffcdd2'],
            'dark': ['#080c1a', '#0f1428', '#1a1f36', '#2d3561', '#3d4571'],
            'viridis': px.colors.sequential.Viridis,
            'plasma': px.colors.sequential.Plasma,
            'rainbow': px.colors.qualitative.D3
        }
    
    def create_line_chart(self, df, x_col, y_col, title, **kwargs):
        fig = px.line(df, x=x_col, y=y_col, 
                     title=title,
                     color=kwargs.get('color_col'),
                     color_discrete_sequence=kwargs.get('colors', self.color_palettes['primary']),
                     labels=kwargs.get('labels', {}),
                     template='plotly_white',
                     markers=True)
        
        fig.update_layout(
            hovermode='x unified',
            title_font={'size': 16, 'color': '#e8e8f0'},
            xaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            yaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            legend_title_font={'size': 12, 'color': 'rgba(232,232,240,0.6)'},
            legend={'font': {'color': 'rgba(232,232,240,0.8)'}},
            paper_bgcolor='rgba(8,12,26,0)',
            plot_bgcolor='rgba(255,255,255,0.03)',
            height=kwargs.get('height', 400),
            margin=dict(l=40, r=40, t=60, b=40),
            font={'family': "'Microsoft YaHei', 'PingFang SC', sans-serif"}
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(108,43,217,0.15)', tickfont={'color': 'rgba(232,232,240,0.6)'})
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(108,43,217,0.15)', tickfont={'color': 'rgba(232,232,240,0.6)'})
        
        fig.update_traces(
            hovertemplate='<b>%{x}</b><br>%{yaxis.title.text}: %{y:,}<extra></extra>',
            line={'width': 3},
            marker={'size': 8, 'line': {'width': 2, 'color': '#6c2bd9'}},
            hoverlabel={'bgcolor': 'rgba(108,43,217,0.9)', 'font': {'color': 'white', 'size': 13}, 'bordercolor': '#6c2bd9'}
        )
        
        return fig
    
    def create_bar_chart(self, df, x_col, y_col, title, **kwargs):
        orientation = kwargs.get('orientation', 'v')
        
        if orientation == 'h':
            fig = px.bar(df, y=x_col, x=y_col,
                         title=title,
                         color=kwargs.get('color_col'),
                         color_discrete_sequence=kwargs.get('colors', self.color_palettes['primary']),
                         labels=kwargs.get('labels', {}),
                         template='plotly_white',
                         orientation='h')
        else:
            fig = px.bar(df, x=x_col, y=y_col,
                         title=title,
                         color=kwargs.get('color_col'),
                         color_discrete_sequence=kwargs.get('colors', self.color_palettes['primary']),
                         labels=kwargs.get('labels', {}),
                         template='plotly_white')
        
        fig.update_layout(
            hovermode='closest',
            title_font={'size': 16, 'color': '#e8e8f0'},
            xaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            yaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            legend_title_font={'size': 12, 'color': 'rgba(232,232,240,0.6)'},
            legend={'font': {'color': 'rgba(232,232,240,0.8)'}},
            paper_bgcolor='rgba(8,12,26,0)',
            plot_bgcolor='rgba(255,255,255,0.03)',
            height=kwargs.get('height', 400),
            margin=dict(l=40, r=40, t=60, b=40),
            font={'family': "'Microsoft YaHei', 'PingFang SC', sans-serif"}
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(108,43,217,0.15)', tickfont={'color': 'rgba(232,232,240,0.6)'})
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(108,43,217,0.15)', tickfont={'color': 'rgba(232,232,240,0.6)'})
        
        fig.update_traces(
            hovertemplate='<b>%{x}</b><br>%{yaxis.title.text}: %{y:,}<extra></extra>',
            marker={'opacity': 0.9, 'line': {'width': 1, 'color': '#ffffff'}}
        )
        
        return fig
    
    def create_pie_chart(self, df, values_col, names_col, title, **kwargs):
        hole = kwargs.get('hole', 0)
        
        fig = px.pie(df, values=values_col, names=names_col,
                     title=title,
                     color_discrete_sequence=kwargs.get('colors', self.color_palettes['rainbow']),
                     hole=hole,
                     template='plotly_white')
        
        fig.update_layout(
            title_font={'size': 16, 'color': '#e8e8f0'},
            legend_title_font={'size': 12, 'color': 'rgba(232,232,240,0.6)'},
            legend={'font': {'color': 'rgba(232,232,240,0.8)'}},
            paper_bgcolor='rgba(8,12,26,0)',
            height=kwargs.get('height', 400),
            margin=dict(l=20, r=20, t=60, b=20),
            font={'family': "'Microsoft YaHei', 'PingFang SC', sans-serif"}
        )
        
        fig.update_traces(
            hovertemplate='<b>%{label}</b><br>数量: %{value:,}<br>占比: %{percent}<extra></extra>',
            textinfo='label+percent',
            textposition='inside',
            textfont={'color': '#ffffff', 'size': 12}
        )
        
        return fig
    
    def create_scatter_chart(self, df, x_col, y_col, title, **kwargs):
        fig = px.scatter(df, x=x_col, y=y_col,
                         title=title,
                         color=kwargs.get('color_col'),
                         size=kwargs.get('size_col'),
                         color_discrete_sequence=kwargs.get('colors', self.color_palettes['primary']),
                         labels=kwargs.get('labels', {}),
                         template='plotly_white')
        
        fig.update_layout(
            hovermode='closest',
            title_font={'size': 16, 'color': '#e8e8f0'},
            xaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            yaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            legend_title_font={'size': 12, 'color': 'rgba(232,232,240,0.6)'},
            legend={'font': {'color': 'rgba(232,232,240,0.8)'}},
            paper_bgcolor='rgba(8,12,26,0)',
            plot_bgcolor='rgba(255,255,255,0.03)',
            height=kwargs.get('height', 400),
            margin=dict(l=40, r=40, t=60, b=40),
            font={'family': "'Microsoft YaHei', 'PingFang SC', sans-serif"}
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(108,43,217,0.15)', tickfont={'color': 'rgba(232,232,240,0.6)'})
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(108,43,217,0.15)', tickfont={'color': 'rgba(232,232,240,0.6)'})
        
        fig.update_traces(
            hovertemplate='<b>%{x}</b><br>%{yaxis.title.text}: %{y}<extra></extra>',
            marker={'opacity': 0.8, 'line': {'width': 1, 'color': '#0066cc'}}
        )
        
        return fig
    
    def create_heatmap(self, df, x_col, y_col, value_col, title, **kwargs):
        pivot_df = df.pivot(index=y_col, columns=x_col, values=value_col)
        
        fig = go.Figure(data=go.Heatmap(
            z=pivot_df.values,
            x=pivot_df.columns,
            y=pivot_df.index,
            colorscale=kwargs.get('colorscale', 'Blues'),
            hoverongaps=False,
            colorbar_title=value_col,
            text=pivot_df.values,
            texttemplate='%{text}',
            textfont={'size': 11, 'color': '#ffffff'}
        ))
        
        fig.update_layout(
            title=title,
            title_font={'size': 16, 'color': '#e8e8f0'},
            xaxis_title=x_col,
            yaxis_title=y_col,
            xaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            yaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            paper_bgcolor='rgba(8,12,26,0)',
            plot_bgcolor='rgba(255,255,255,0.03)',
            height=kwargs.get('height', 400),
            margin=dict(l=40, r=40, t=60, b=40),
            font={'family': "'Microsoft YaHei', 'PingFang SC', sans-serif"}
        )
        
        fig.update_xaxes(tickfont={'color': 'rgba(232,232,240,0.6)'})
        fig.update_yaxes(tickfont={'color': 'rgba(232,232,240,0.6)'})
        
        return fig
    
    def create_correlation_heatmap(self, corr_df, title):
        fig = go.Figure(data=go.Heatmap(
            z=corr_df.values,
            x=corr_df.columns,
            y=corr_df.columns,
            colorscale='RdBu',
            hoverongaps=False,
            colorbar_title='相关系数',
            text=corr_df.values.round(2),
            texttemplate='%{text}',
            textfont={'size': 11, 'color': '#ffffff'}
        ))
        
        fig.update_layout(
            title=title,
            title_font={'size': 16, 'color': '#e8e8f0'},
            paper_bgcolor='rgba(8,12,26,0)',
            plot_bgcolor='rgba(255,255,255,0.03)',
            height=400,
            margin=dict(l=40, r=40, t=60, b=40),
            font={'family': "'Microsoft YaHei', 'PingFang SC', sans-serif"}
        )
        
        fig.update_xaxes(tickfont={'color': 'rgba(232,232,240,0.6)'})
        fig.update_yaxes(tickfont={'color': 'rgba(232,232,240,0.6)'})
        
        return fig
    
    def create_gauge_chart(self, value, title, **kwargs):
        min_val = kwargs.get('min_val', 0)
        max_val = kwargs.get('max_val', 100)
        threshold = kwargs.get('threshold', max_val * 0.8)
        color = kwargs.get('color', '#0099ff')
        
        fig = go.Figure(go.Indicator(
            mode='gauge+number+delta',
            value=value,
            title={'text': title, 'font': {'size': 14, 'color': '#e8e8f0'}},
            gauge={
                'axis': {'range': [min_val, max_val], 
                         'tickwidth': 1, 
                         'tickcolor': '#e8e8f0',
                         'tickfont': {'color': '#e8e8f0'}},
                'bar': {'color': color},
                'steps': [
                    {'range': [min_val, max_val*0.5], 'color': '#ffebee'},
                    {'range': [max_val*0.5, max_val*0.75], 'color': '#fff3e0'},
                    {'range': [max_val*0.75, max_val], 'color': '#e8f5e9'}
                ],
                'threshold': {
                    'line': {'color': '#e53935', 'width': 4},
                    'value': threshold
                }
            },
            delta={'reference': threshold, 'font': {'color': '#e8e8f0'}}
        ))
        
        fig.update_layout(
            paper_bgcolor='rgba(8,12,26,0)',
            height=kwargs.get('height', 250),
            margin=dict(l=20, r=20, t=40, b=20),
            font={'family': "'Microsoft YaHei', 'PingFang SC', sans-serif"}
        )
        
        return fig
    
    def create_area_chart(self, df, x_col, y_col, title, **kwargs):
        fig = px.area(df, x=x_col, y=y_col,
                     title=title,
                     color=kwargs.get('color_col'),
                     color_discrete_sequence=kwargs.get('colors', self.color_palettes['primary']),
                     labels=kwargs.get('labels', {}),
                     template='plotly_white')
        
        fig.update_layout(
            hovermode='x unified',
            title_font={'size': 16, 'color': '#e8e8f0'},
            xaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            yaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            legend_title_font={'size': 12, 'color': 'rgba(232,232,240,0.6)'},
            legend={'font': {'color': 'rgba(232,232,240,0.8)'}},
            paper_bgcolor='rgba(8,12,26,0)',
            plot_bgcolor='rgba(255,255,255,0.03)',
            height=kwargs.get('height', 400),
            margin=dict(l=40, r=40, t=60, b=40),
            font={'family': "'Microsoft YaHei', 'PingFang SC', sans-serif"}
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(108,43,217,0.15)', tickfont={'color': 'rgba(232,232,240,0.6)'})
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(108,43,217,0.15)', tickfont={'color': 'rgba(232,232,240,0.6)'})
        
        return fig
    
    def create_histogram(self, df, x_col, title, **kwargs):
        fig = px.histogram(df, x=x_col,
                          title=title,
                          color=kwargs.get('color_col'),
                          color_discrete_sequence=kwargs.get('colors', self.color_palettes['primary']),
                          labels=kwargs.get('labels', {}),
                          template='plotly_white')
        
        fig.update_layout(
            hovermode='closest',
            title_font={'size': 16, 'color': '#e8e8f0'},
            xaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            yaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            legend_title_font={'size': 12, 'color': 'rgba(232,232,240,0.6)'},
            legend={'font': {'color': 'rgba(232,232,240,0.8)'}},
            paper_bgcolor='rgba(8,12,26,0)',
            plot_bgcolor='rgba(255,255,255,0.03)',
            height=kwargs.get('height', 400),
            margin=dict(l=40, r=40, t=60, b=40),
            font={'family': "'Microsoft YaHei', 'PingFang SC', sans-serif"}
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(108,43,217,0.15)', tickfont={'color': 'rgba(232,232,240,0.6)'})
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(108,43,217,0.15)', tickfont={'color': 'rgba(232,232,240,0.6)'})
        
        return fig
    
    def create_box_plot(self, df, x_col, y_col, title, **kwargs):
        fig = px.box(df, x=x_col, y=y_col,
                    title=title,
                    color=kwargs.get('color_col'),
                    color_discrete_sequence=kwargs.get('colors', self.color_palettes['primary']),
                    labels=kwargs.get('labels', {}),
                    template='plotly_white')
        
        fig.update_layout(
            hovermode='closest',
            title_font={'size': 16, 'color': '#e8e8f0'},
            xaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            yaxis_title_font={'size': 14, 'color': 'rgba(232,232,240,0.6)'},
            legend_title_font={'size': 12, 'color': 'rgba(232,232,240,0.6)'},
            legend={'font': {'color': 'rgba(232,232,240,0.8)'}},
            paper_bgcolor='rgba(8,12,26,0)',
            plot_bgcolor='rgba(255,255,255,0.03)',
            height=kwargs.get('height', 400),
            margin=dict(l=40, r=40, t=60, b=40),
            font={'family': "'Microsoft YaHei', 'PingFang SC', sans-serif"}
        )
        
        fig.update_xaxes(tickfont={'color': 'rgba(232,232,240,0.6)'})
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(108,43,217,0.15)', tickfont={'color': 'rgba(232,232,240,0.6)'})
        
        return fig
    
    def create_subplot(self, specs, titles, **kwargs):
        fig = make_subplots(rows=kwargs.get('rows', 1), 
                          cols=kwargs.get('cols', 1),
                          subplot_titles=titles,
                          specs=specs)
        
        fig.update_layout(
            title=kwargs.get('title', ''),
            title_font={'size': 18, 'color': '#1a1f36'},
            paper_bgcolor='rgba(8,12,26,0)',
            plot_bgcolor='rgba(255,255,255,0.03)',
            height=kwargs.get('height', 600),
            margin=dict(l=40, r=40, t=80, b=40),
            font={'family': "'Microsoft YaHei', 'PingFang SC', sans-serif"}
        )
        
        return fig