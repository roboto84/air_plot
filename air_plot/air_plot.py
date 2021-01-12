# Air properties time interval plotter

import sys
import ntpath
import os.path
from typing import NoReturn
from bin.air_settings import file_settings
from bin.plot import Plot
from bin.plot_settings import plotter_settings


class AirPlot:
    HOME_PATH: str = ntpath.dirname(__file__)

    def __init__(self):
        self.delta_graph: bool = False
        self.data_file: str = file_settings['live_data']['data_file']
        self.data_col1: str = plotter_settings['data_col1']
        self.data_col2: str = plotter_settings['data_col2']
        self.x_label: str = plotter_settings['hourly_data']['x_label']
        self.y_label: str = plotter_settings['y_label']
        self.table_title_interval: str = plotter_settings['live_data']['table_title_interval']

        if len(sys.argv) == 2 or len(sys.argv) == 3:
            if self.diff() or self.diff2():
                self.delta_graph: bool = True
                self.data_col1: str = '{} Interval'.format(self.data_col1)
                self.data_col2: str = '{} Delta'.format(self.data_col2)
                self.y_label: str = plotter_settings['diff_labels']['y_label']
                self.x_label: str = plotter_settings['hourly_data']['diff_labels']['x_label']

            if sys.argv[1] == 'live':
                if self.diff():
                    self.data_file: str = file_settings['live_data']['diff_file']
                    self.table_title_interval: str = '{} Delta'.format(self.table_title_interval)
                elif self.diff2():
                    self.data_file: str = file_settings['live_data']['diff2_file']
                    self.table_title_interval: str = '{} 2nd Delta'.format(self.table_title_interval)

            elif sys.argv[1] == '48hr':
                self.data_file: str = file_settings['next_48_hours']['data_file']
                self.table_title_interval: str = plotter_settings['next_48_hours']['table_title_interval']
                if self.diff():
                    self.data_file: str = file_settings['next_48_hours']['diff_file']
                    self.table_title_interval: str = '{} Delta'.format(self.table_title_interval)

            elif sys.argv[1] == '7day':
                self.data_file: str = file_settings['next_7_days']['data_file']
                self.table_title_interval: str = plotter_settings['next_7_days']['table_title_interval']
                self.x_label: str = plotter_settings['daily_data']['x_label']
                if self.diff():
                    self.data_file: str = file_settings['next_7_days']['diff_file']
                    self.table_title_interval: str = '{} Delta'.format(self.table_title_interval)
                    self.x_label: str = plotter_settings['daily_data']['diff_labels']['x_label']

    @staticmethod
    def diff() -> bool:
        return len(sys.argv) == 3 and sys.argv[2] == 'diff'

    @staticmethod
    def diff2() -> bool:
        return len(sys.argv) == 3 and sys.argv[2] == 'diff2'

    def run_plot(self) -> NoReturn:
        full_path_data_file: str = os.path.join(self.HOME_PATH, self.data_file)
        plot_time_interval: int = 10000
        if self.delta_graph:
            graph_type: str = 'scatter'
        else:
            graph_type: str = 'plot'

        table_settings = {
            'data_col1': self.data_col1,
            'data_col2': self.data_col2,
            'x_label': self.x_label,
            'y_label': self.y_label,
            'table_title_interval': 'AirPlot Barometric Pressure | {}'.format(self.table_title_interval)
        }

        new_plot: Plot = Plot(full_path_data_file, table_settings, plot_time_interval, graph_type)
        new_plot.show_plot()


if __name__ == '__main__':
    air_plot: AirPlot = AirPlot()
    air_plot.run_plot()
