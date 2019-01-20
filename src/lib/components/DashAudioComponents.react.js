import React, {Component} from 'react';
import ReactAudioPlayer from 'react-audio-player';
import PropTypes from 'prop-types';

/**
 * DashAudioComponent to play sounds.
 */
export default class DashAudioComponents extends Component {
    render() {
        const props = {...this.props, ...this.props.overrideProps};
        let src = props.src;
        if (props.from_position && props.to_position) {
            src = `${src}#t=${props.from_position},${props.to_position}`;
        }
        return (
            <ReactAudioPlayer
                style={props.style}
                src={src}
                autoPlay={props.autoPlay}
                controls={props.controls}
            />
        );
    }
}

DashAudioComponents.defaultProps = {};
const propTypesDefinitions = {
    src: PropTypes.string.isRequired,
    autoPlay: PropTypes.bool.isRequired,
    style: PropTypes.objectOf(PropTypes.string),
    from_position: PropTypes.number,
    to_position: PropTypes.number,
    controls: PropTypes.bool,
};
DashAudioComponents.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    /**
     * Override existing properties, can be used
     * to change all properties in one callback.
     */
    overrideProps: PropTypes.shape(propTypesDefinitions),
    /**
     * Source of audio file.
     */
    src: PropTypes.string.isRequired,
    /**
     * Play automatically on src change.
     */
    autoPlay: PropTypes.bool.isRequired,
    /**
     * Styles for audio component.
     */
    style: PropTypes.objectOf(PropTypes.string),
    /**
     * 'From' position in seconds. Will be appended to src.
     */
    from_position: PropTypes.number,
    /**
     * 'To' position in seconds. Will be appended to src.
     */
    to_position: PropTypes.number,
    /**
     * Show controls UI.
     */
    controls: PropTypes.bool,
};