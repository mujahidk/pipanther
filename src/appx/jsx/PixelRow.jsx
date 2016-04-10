var React = require('react');

var PixelRow = React.createClass({
    render: function(){
        return (<tr>{this.props.row}</tr>);
    }
});

module.exports = PixelRow;
