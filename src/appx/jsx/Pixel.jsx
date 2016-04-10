var React = require('react');

var Pixel = React.createClass({
    handleClick: function(e) {
        e.preventDefault();
        var row = this.props.pixel.row,
            column = this.props.pixel.column;

        $.ajax({
            url: '/api/pixels/'+row+'/'+column,
            dataType: 'json',
            type: 'POST',
            success: function(data) {
                this.setState({pixel: data});
            }.bind(this),
                error: function(xhr, status, err) {
                console.error(status, err.toString());
            }.bind(this)
        });
    },
    getInitialState: function() {
        return { pixel: this.props.pixel };
    },
    componentDidMount: function() {
        this.setState({pixel: this.state.pixel});
    },
    componentWillReceiveProps: function(){
        this.setState({pixel: this.props.pixel});
    },
    render: function() {
        var pixel = this.state.pixel,
            buttonStyle;
        buttonStyle = "rgb(" + pixel.color + ")";
        if (buttonStyle === 'rgb(0,0,0)') {
            buttonStyle = 'inherit';
        }
        return (
            <td>
                <button onClick={this.handleClick}
                    className="btn btn-default"
                    style={{backgroundColor: buttonStyle}}>
                    {pixel.row}:{pixel.column}
                </button>
            </td>
        );
    }
});

module.exports = Pixel;
