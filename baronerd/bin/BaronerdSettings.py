#  Configuration for different plotting perspectives

File_Settings = {
    'live_data': {
        'data_file': 'data/liveData.csv',
        'diff_file': 'data/differentials/liveDataDiff.csv',
        'diff2_file': 'data/differentials/liveData2ndOrderDiffFile.csv'
    },
    'next_48_hours': {
        'data_file': 'data/next48Data.csv',
        'diff_file': 'data/differentials/next48HrsDataDiffFile.csv'
    },
    'next_7_days': {
        'data_file': 'data/next7DaysData.csv',
        'diff_file': 'data/differentials/next7DaysDataDiffFile.csv'
    }
}

Plotter_Settings = {
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
