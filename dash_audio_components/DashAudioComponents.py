# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashAudioComponents(Component):
    """A DashAudioComponents component.
DashAudioComponent to play sounds.

Keyword arguments:
- url (string; required)
- autoLoad (boolean; optional)
- playStatus (required)
- playbackRate (number; optional)
- volume (number; optional)
- position (number; optional)
- playFromPosition (number; optional)
- id (string; optional): The ID used to identify this component in Dash callbacks
- loop (boolean; optional)

Available events: """
    @_explicitize_args
    def __init__(self, onLoading=Component.UNDEFINED, onLoad=Component.UNDEFINED, onResume=Component.UNDEFINED, onBufferChange=Component.UNDEFINED, url=Component.REQUIRED, playbackRate=Component.UNDEFINED, playStatus=Component.REQUIRED, autoLoad=Component.UNDEFINED, volume=Component.UNDEFINED, onError=Component.UNDEFINED, onPause=Component.UNDEFINED, onStop=Component.UNDEFINED, onFinishedPlaying=Component.UNDEFINED, position=Component.UNDEFINED, onPlaying=Component.UNDEFINED, playFromPosition=Component.UNDEFINED, id=Component.UNDEFINED, loop=Component.UNDEFINED, **kwargs):
        self._prop_names = ['url', 'id', 'playbackRate', 'playStatus', 'autoLoad', 'volume', 'position', 'playFromPosition', 'loop']
        self._type = 'DashAudioComponents'
        self._namespace = 'dash_audio_components'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['url', 'id', 'playbackRate', 'playStatus', 'autoLoad', 'volume', 'position', 'playFromPosition', 'loop']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in [u'url', u'playStatus']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashAudioComponents, self).__init__(**args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('DashAudioComponents(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'DashAudioComponents(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
