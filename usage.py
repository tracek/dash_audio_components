from enum import Enum

import dash
import dash_audio_components
from dash.dependencies import Input, Output, Event
import dash_html_components as html


class PlayStatuses(Enum):
    PLAYING = 'PLAYING'
    STOPPED = 'STOPPED'
    PAUSED = 'PAUSED'


app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    html.Button([
        html.Div([
            html.Label('Play audio')
        ], className='box')],
        id='playAudio',
        className='button'
    ),
    html.Div(id='output'),
    dash_audio_components.DashAudioComponents(
        id='audio-player',
        url='https://storage.googleapis.com/audio-files-samples/SampleAudio_0.4mb.mp3',
        playStatus=PlayStatuses.STOPPED.value
    )
])

@app.callback(
    Output('audio-player', 'playStatus'),
    [
        Input('playAudio', 'n_clicks')
    ]
)
def btn_click_play_callback(n_clicks):
    if n_clicks is not None:
        return (PlayStatuses.PLAYING.value
                if n_clicks % 2 != 0
                else PlayStatuses.STOPPED.value)

@app.callback(
    Output('output', 'children'),
    [
        Input('playAudio', 'n_clicks')
    ]
)
def btn_click_output_callback(n_clicks):
    status = 'Not clicked'
    if n_clicks is not None:
        status = (PlayStatuses.PLAYING.value
                  if n_clicks % 2 != 0
                  else PlayStatuses.STOPPED.value)
    return status


if __name__ == '__main__':
    app.run_server(debug=True)
