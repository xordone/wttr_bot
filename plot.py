import configs.db as db
from datetime import datetime
from configs.config import time_format
import plotly.graph_objs as go

title = datetime.now().strftime(time_format)


def get_plot(style='line'):
    a = db.fetchall()
    date = []
    temp = []
    temp_min = []
    temp_max = []
    for i in a:
        temp.append(i[1])
        date.append(i[2])
        temp_min.append(i[3])
        temp_max.append(i[4])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=date, y=temp, name='temperature'))
    if style == 'full':
        fig.add_trace(go.Scatter(x=date, y=temp_min, name='min', fill='tonexty'))
        fig.add_trace(go.Scatter(x=date, y=temp_max, name='max', fill='tonexty'))

    fig.update_layout(title=title, title_x=0.5)
    fig.write_image('plot.png')

    return True
