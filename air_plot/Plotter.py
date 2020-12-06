# Air properties time interval plotter

import sys
import ntpath
import os.path
from bin.AirSettings import File_Settings
from bin.Plot import Plot
from bin.PlotSettings import Plotter_Settings


class Plotter:
    HOME_PATH = ntpath.dirname(__file__)

    def __init__(self):
        self.delta_graph = False
        self.data_file = File_Settings['live_data']['data_file']
        self.data_col1 = Plotter_Settings['data_col1']
        self.data_col2 = Plotter_Settings['data_col2']
        self.x_label = Plotter_Settings['hourly_data']['x_label']
        self.y_label = Plotter_Settings['y_label']
        self.table_title_interval = Plotter_Settings['live_data']['table_title_interval']

        if len(sys.argv) == 2 or len(sys.argv) == 3:
            if self.diff() or self.diff2():
                self.delta_graph = True
                self.data_col1 = '{} Interval'.format(self.data_col1)
                self.data_col2 = '{} Delta'.format(self.data_col2)
                self.y_label = Plotter_Settings['diff_labels']['y_label']
                self.x_label = Plotter_Settings['hourly_data']['diff_labels']['x_label']

            if sys.argv[1] == 'live':
                if self.diff():
                    self.data_file = File_Settings['live_data']['diff_file']
                    self.table_title_interval = '{} Delta'.format(self.table_title_interval)
                elif self.diff2():
                    self.data_file = File_Settings['live_data']['diff2_file']
                    self.table_title_interval = '{} 2nd Delta'.format(self.table_title_interval)

            elif sys.argv[1] == '48hr':
                self.data_file = File_Settings['next_48_hours']['data_file']
                self.table_title_interval = Plotter_Settings['next_48_hours']['table_title_interval']
                if self.diff():
                    self.data_file = File_Settings['next_48_hours']['diff_file']
                    self.table_title_interval = '{} Delta'.format(self.table_title_interval)

            elif sys.argv[1] == '7day':
                self.data_file = File_Settings['next_7_days']['data_file']
                self.table_title_interval = Plotter_Settings['next_7_days']['table_title_interval']
                self.x_label = Plotter_Settings['daily_data']['x_label']
                if self.diff():
                    self.data_file = File_Settings['next_7_days']['diff_file']
                    self.table_title_interval = '{} Delta'.format(self.table_title_interval)
                    self.x_label = Plotter_Settings['daily_data']['diff_labels']['x_label']

    @staticmethod
    def diff():
        return len(sys.argv) == 3 and sys.argv[2] == 'diff'

    @staticmethod
    def diff2():
        return len(sys.argv) == 3 and sys.argv[2] == 'diff2'

    def run_plot(self):
        full_path_data_file = os.path.join(self.HOME_PATH, self.data_file)
        plot_time_interval = 10000
        if self.delta_graph:
            graph_type = 'scatter'
        else:
            graph_type = 'plot'

        table_settings = {
            'data_col1': self.data_col1,
            'data_col2': self.data_col2,
            'x_label': self.x_label,
            'y_label': self.y_label,
            'table_title_interval': 'AirPlot Barometric Pressure | {}'.format(self.table_title_interval)
        }

        new_plot = Plot(full_path_data_file, table_settings, plot_time_interval, graph_type)
        new_plot.show_plot()


if __name__ == '__main__':
    air_plot = Plotter()
    air_plot.run_plot()
