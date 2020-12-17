# A general GUI data graph plot

import os.path
import ntpath
import logging.config
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from bin.plot_settings import default_plot_theme


class Plot:
    HOME_PATH = ntpath.dirname(__file__)
    logging.config.fileConfig(fname=os.path.join(HOME_PATH, 'logging.conf'), disable_existing_loggers=False)

    def __init__(self, data_file, table_settings, interval, graph_type='plot'):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(logging.INFO)

        self.data_file = data_file
        self.graph_type = graph_type
        self.table_settings = table_settings
        self.interval = interval

        self.background_color = default_plot_theme['background_color']
        self.graph_values_color = default_plot_theme['graph_values_color']
        self.axis_value_color = default_plot_theme['axis_value_color']
        self.grid_line_color = default_plot_theme['grid_line_color']
        self.axis_title_color = default_plot_theme['axis_title_color']
        self.fig_title_color = default_plot_theme['fig_title_color']

    def show_plot(self):
        if os.path.isfile(self.data_file):
            self.logger.info('Data file exists... attempting to plot')
            plt.style.use('fivethirtyeight')
            fig = plt.figure()
            fig.set_facecolor(self.background_color)
            fig.set_tight_layout(True)

            try:
                ani = FuncAnimation(fig, self.animate, interval=self.interval)
                plt.show()
            except KeyboardInterrupt:
                self.logger.warning('Received a KeyboardInterrupt... exiting process')
                exit()
        else:
            self.logger.error('Data file does not exist. Please assure data file exists before attempting a plot')
            exit()

    @staticmethod
    def read_in_data_file(logger, data_file):
        try:
            data = pd.read_csv(data_file)
            return data
        except ValueError:
            logger.error('It appears the data file is not structure correctly, possibly missing columns, check '
                         'csv format... now exiting')
            exit()

    def animate(self, i):
        data = self.read_in_data_file(self.logger, self.data_file)
        x_values = data[self.table_settings['data_col1']]
        y_values = data[self.table_settings['data_col2']]

        plt.cla()
        plt.xlabel(self.table_settings['x_label'], color=self.axis_title_color)
        plt.ylabel(self.table_settings['y_label'], color=self.axis_title_color)
        plt.title(self.table_settings['table_title_interval'], color=self.fig_title_color)
        plt.gcf().autofmt_xdate()

        if self.graph_type == 'scatter':
            plt.scatter(x_values, y_values, s=80, color=self.graph_values_color)
            plt.minorticks_on()
            plt.grid(b=True, which='minor', color='#000EEE', linestyle='-', alpha=0.2)
            plt.grid(b=True, which='major', color=self.grid_line_color, linestyle='dotted')
        else:
            plt.plot(x_values, y_values, self.graph_values_color)
            plt.grid(b=True, which='major', linestyle='dotted')
        axes = plt.gca()

        # Set colors
        axes.set_facecolor(self.background_color)
        axes.tick_params(labelcolor=self.axis_value_color)
        ticks = axes.get_xgridlines()

        for tick in ticks:
            tick.set_color(self.grid_line_color)

        for spine in axes.spines.values():
            spine.set_edgecolor(self.background_color)

        # Set axis range
        if self.table_settings.get('y_ticks'):
            axes.set_ylim(self.table_settings.get('y_ticks'))
        else:
            try:
                y_range = abs(max(y_values)) - abs(min(y_values))
                y_buffer_interval = y_range / 15
                axes.set_ylim([min(y_values) - y_buffer_interval, max(y_values) + y_buffer_interval])
            except ValueError:
                self.logger.error('It appears the data file may not be populated.  Can not plot empty data set... '
                                  'now exiting')
                exit()
