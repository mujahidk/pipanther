const ReactDOM = require('react-dom'),
    React = require('react'),
    Temperature = require('./jsx/Temperature'),
    Humidity = require('./jsx/Humidity');

require("./scss/cels");

ReactDOM.render(
    React.createElement(Temperature, { source: '/api/temperature', interval: 5000 }),
    document.querySelector('#temperature'));

ReactDOM.render(
    React.createElement(Humidity, { source: '/api/humidity', interval: 10000 }),
    document.querySelector('#humidity'));
