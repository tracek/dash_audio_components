import React, {Component} from 'react';
import Sound from 'react-sound';
import PropTypes from 'prop-types';

/**
 * DashAudioComponent to play sounds.
 */
export default class DashAudioComponents extends Component {
    setStateByEvent(e) {
        if (e.position >= this.props.stopPosition) {
            this.setState({playStatus: Sound.status.PAUSED})
        }
    }
    render() {
        return (
            <Sound
                {...this.props}
                {...this.props.overrideProps}
                onPlaying={this.setStateByEvent.bind(this)}
            />
        );
    }
}

DashAudioComponents.defaultProps = {};
const propTypesDefinitions = {
    url: PropTypes.string.isRequired,
    playStatus: PropTypes.oneOf(Object.keys(Sound.status)).isRequired,
    position: PropTypes.number,
    stopPosition: PropTypes.number,
    playFromPosition: PropTypes.number,
    volume: PropTypes.number,
    playbackRate: PropTypes.number,
    autoLoad: PropTypes.bool,
    loop: PropTypes.bool,
};
DashAudioComponents.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,
    overrideProps: PropTypes.shape(propTypesDefinitions),
    url: PropTypes.string.isRequired,
    playStatus: PropTypes.oneOf(Object.keys(Sound.status)).isRequired,
    position: PropTypes.number,
    stopPosition: PropTypes.number,
    playFromPosition: PropTypes.number,
    volume: PropTypes.number,
    playbackRate: PropTypes.number,
    autoLoad: PropTypes.bool,
    loop: PropTypes.bool,
};
