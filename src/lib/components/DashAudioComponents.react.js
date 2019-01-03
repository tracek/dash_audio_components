import React, {Component} from 'react';
import Sound from 'react-sound';
import PropTypes from 'prop-types';

/**
 * DashAudioComponent to play sounds.
 */
export default class DashAudioComponents extends Component {
    render() {
        return (
            <Sound
                {...this.props}
            />
        );
    }
}

DashAudioComponents.defaultProps = {};

DashAudioComponents.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,
    url: PropTypes.string.isRequired,
    playStatus: PropTypes.oneOf(Object.keys(Sound.status)).isRequired,
    position: PropTypes.number,
    playFromPosition: PropTypes.number,
    volume: PropTypes.number,
    playbackRate: PropTypes.number,
    onError: PropTypes.func,
    onLoading: PropTypes.func,
    onLoad: PropTypes.func,
    onPlaying: PropTypes.func,
    onPause: PropTypes.func,
    onResume: PropTypes.func,
    onStop: PropTypes.func,
    onFinishedPlaying: PropTypes.func,
    onBufferChange: PropTypes.func,
    autoLoad: PropTypes.bool,
    loop: PropTypes.bool,
    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func
};
