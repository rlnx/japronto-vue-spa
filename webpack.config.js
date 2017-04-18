var path    = require('path')
var webpack = require('webpack')
var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './client/main.coffee',
  output: {
    path: path.resolve(__dirname, './static/build'),
    filename: 'app.js'
  },
  plugins: [
    new HtmlWebpackPlugin({
      inject: false,
      template: './client/container.pug',
      filename: 'app.html'
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      _: 'underscore'
    })
  ],
  resolve: {
    alias: {
      vue$: 'vue/dist/vue.esm.js',
      assets: path.resolve(__dirname, './static/assets')
    }
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          // vue-loader options go here
        }
      },
      {
        test: /\.coffee$/,
        loader: 'coffee-loader',
        exclude: /node_modules/
      },
      {
        test: /\.styl$/,
        loader: ['style-loader', 'css-loader', 'stylus-loader']
      },
      {
        test: /\.pug$/,
        loader: 'pug-loader'
      }
    ]
  },
  devtool: '#eval-source-map',
  performance: false
}

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}
