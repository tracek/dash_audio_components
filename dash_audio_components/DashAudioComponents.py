# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashAudioComponents(Component):
    """A DashAudioComponents component.
DashAudioComponent to play sounds.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- overrideProps (optional): Override existing properties, can be used
to change all properties in one callback.. overrideProps has the following type: dict containing keys 'src', 'autoPlay', 'style', 'from_position', 'to_position', 'controls'.
Those keys have the following types: 
  - src (string; required)
  - autoPlay (boolean; required)
  - style (dict with strings as keys and values of type string; optional)
  - from_position (number; optional)
  - to_position (number; optional)
  - controls (boolean; optional)
- src (string; required): Source of audio file.
- autoPlay (boolean; required): Play automatically on src change.
- style (dict with strings as keys and values of type string; optional): Styles for audio component.
- from_position (number; optional): 'From' position in seconds. Will be appended to src.
- to_position (number; optional): 'To' position in seconds. Will be appended to src.
- controls (boolean; optional): Show controls UI.

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, overrideProps=Component.UNDEFINED, src=Component.REQUIRED, autoPlay=Component.REQUIRED, style=Component.UNDEFINED, from_position=Component.UNDEFINED, to_position=Component.UNDEFINED, controls=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'overrideProps', 'src', 'autoPlay', 'style', 'from_position', 'to_position', 'controls']
        self._type = 'DashAudioComponents'
        self._namespace = 'dash_audio_components'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'overrideProps', 'src', 'autoPlay', 'style', 'from_position', 'to_position', 'controls']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['src', 'autoPlay']:
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
