const ReactDOM = require('react-dom'),
    React = require('react'),
    PixelGrid = require('./jsx/PixelGrid');

require("./scss/pixels");

ReactDOM.render(
    React.createElement(PixelGrid, { source: '/api/pixels' }),
    document.querySelector('#pixelgrid'));
