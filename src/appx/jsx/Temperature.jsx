var React = require('react'),
    ReactDOM = require('react-dom');

var Temperature = React.createClass({

    round: function(data){
        return Number((data).toFixed(2));
    },
    loadFromPi: function() {
    $.ajax({
      url: this.props.source,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({
            celsius: this.round(data.celsius),
            fahrenheit: this.round(data.fahrenheit)
        });
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.source, status, err.toString());
      }.bind(this)
    });
  },

    getInitialState: function() {
        return {
            celsius: '--',
            fahrenheit: '--'
        };
    },

    componentDidMount: function() {
        this.loadFromPi();
        setInterval(this.loadFromPi, this.props.interval);
    },

    render: function() {
        return (
            <div>
                <span className="pi-label">Pi Temperature</span><br />
                <span className="pi-unit large">{this.state.celsius} <sup>o</sup>C</span><br />
                <small>{this.state.fahrenheit} <sup>o</sup>F</small>
            </div>
        );
    }
});

module.exports = Temperature;
