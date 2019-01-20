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
    dash_audio_components.DashAudioComponents(
        id='audio-player',
        src='https://storage.googleapis.com/audio-files-samples/SampleAudio_0.4mb.mp3',
        autoPlay=True,
        from_position=1.1,
        to_position=3.5,
        style={'display': 'none',
               'width': 0, 'height': 0},
        controls=False
    ),
])

@app.callback(
    Output('audio-player', 'overrideProps'),
    [
        Input('playAudio', 'n_clicks')
    ]
)
def btn_click_play_callback(n_clicks):
    if n_clicks is not None:
        return {'src': (''
                        if n_clicks % 2 != 0
                        else 'https://storage.googleapis.com/audio-files-samples/'
                             'SampleAudio_0.4mb.mp3')}

if __name__ == '__main__':
    app.run_server(debug=True)
