#  Configuration for different plot themes

default_plot_theme: dict = {
    'background_color': '#292929',
    'graph_values_color': '#FF6100',
    'axis_value_color': '#D66C00',
    'grid_line_color': '#525252',
    'axis_title_color': '#DDDBFF',
    'fig_title_color': '#EEEEEE'
}

plotter_settings: dict = {
    'data_col1': 'Time',
    'data_col2': 'Pressure',
    'y_label': 'pressure (inHg)',
    'diff_labels': {
        'y_label': 'delta (inHg)',
    },
    'live_data': {
        'table_title_interval': 'Live'
    },
    'next_48_hours': {
        'table_title_interval': '48Hr'
    },
    'next_7_days': {
        'table_title_interval': '7 Day'
    },
    'hourly_data': {
        'x_label': 'time (hrs)',
        'diff_labels': {
            'x_label': 'time interval(hrs)',
        }
    },
    'daily_data': {
        'x_label': 'time (days)',
        'diff_labels': {
            'x_label': 'time interval(days)',
        }
    }
}
