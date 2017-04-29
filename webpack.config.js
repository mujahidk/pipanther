const path = require('path'),
    webpack = require("webpack"),
    ExtractCssPlugin = require('extract-text-webpack-plugin');

const PATHS = {
    jsx: path.join(__dirname, '/src/appx/jsx'),
    scss: path.join(__dirname, '/src/appx/scss'),
    build: path.join(__dirname, '/src/app/static')
};

module.exports = {
    entry: {
        cels: './src/appx/cels.js',
        pixels: './src/appx/pixels.js',
        common: './src/appx/common.js'
    },
    module: {
        loaders: [
            {
                test: /\.js[x]$/,
                include: PATHS.jsx,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['react', 'es2015']
                }
            },
            {
                test: /\.scss$/,
                include: PATHS.scss,
                loader: ExtractCssPlugin.extract('css!sass')
            }
        ]
    },
    output: {
        filename: '[name].bundle.js',
        path: PATHS.build
    },
    resolve: {
        extensions: ['', '.js', '.jsx', '.scss']
    },
    plugins: [
        new ExtractCssPlugin('[name].style.css'),
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false
            }
        })
    ]
}
