var React = require('react'),
    ResetButton = require('./ResetButton'),
    PixelRow = require('./PixelRow'),
    Pixel = require('./Pixel');

var PixelGrid = React.createClass({

    handleResetClick: function(e) {
        e.preventDefault();
        $.ajax({
            url: this.props.source,
            dataType: 'json',
            type: 'DELETE',
            success: function(result) {
                this.setState({
                    pixels: result.pixels
                });
            }.bind(this),
                error: function(xhr, status, err) {
                console.error(this.props.source, status, err.toString());
            }.bind(this)
        });
    },

    getInitialState: function() {
    return {
            pixels: []
        };
    },

    componentDidMount: function() {
        this.serverRequest = $.get(this.props.source, function (result) {
            this.setState({
                pixels: result.pixels
            });
        }.bind(this));
    },

    componentWillUnmount: function() {
        this.serverRequest.abort();
    },

    render: function() {
        var rows = [[],[],[],[],[],[],[],[]],
            pixel,
            pixels = this.state.pixels;
        // Add Pixel to respective row
        pixels.forEach(function(pixel) {
            (rows[pixel.row]).push(<Pixel key={pixel.row+'-'+pixel.column} pixel={pixel} />);
        });
        // Render PixelRow
        for (var i = rows.length - 1; i >= 0; i--) {
            rows[i] = (<PixelRow key={i} row={rows[i]} />)
        }
        return (
            <div>
                <table>
                    <tbody>{rows}</tbody>
                </table>
                <div className="reset-button">
                    <ResetButton onclick={this.handleResetClick} />
                </div>
            </div>
        );
    }
});

module.exports = PixelGrid;
