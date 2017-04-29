var React = require('react'),
    ReactDOM = require('react-dom');

var Humidity = React.createClass({

    loadFromPi: function() {
        $.ajax({
          url: this.props.source,
          dataType: 'json',
          cache: false,
          success: function(data) {
            this.setState({humidity: Number((data.humidity).toFixed(2))});
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(this.props.source, status, err.toString());
          }.bind(this)
        });
    },

    getInitialState: function() {
        return {
            humidity: '--'
        };
    },

    componentDidMount: function() {
        this.loadFromPi();
        setInterval(this.loadFromPi, this.props.interval);
    },

    render: function() {
        return (
            <div>
                <span className="pi-label">Humidity</span><br />
                <span className="pi-unit large">{this.state.humidity}</span>
            </div>
        );
    }
});

module.exports = Humidity;
