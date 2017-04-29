var React = require('react');

var ResetButton = React.createClass({
    render: function(){
        return (<button onClick={this.props.onclick}
                    type="button"
                    className="btn btn-danger">Reset</button>);
    }
});

module.exports = ResetButton;
