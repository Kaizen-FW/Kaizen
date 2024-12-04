const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');

module.exports = {
  entry: './src/index.js',  // Entry point for your application
  output: {
    path: path.resolve(__dirname, 'build'),  // Build directory
    filename: 'bundle.js',  // Output file for the JavaScript bundle
    publicPath: '/',  // Path to the public folder
  },
  resolve: {
    extensions: ['.js', '.jsx', '.json'],  // Resolve these extensions without needing to specify them
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,  // Transpile JSX and JS files
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react'],  // For ES6+ and React
            plugins: [process.env.NODE_ENV !== 'production' && require.resolve('react-refresh/babel')].filter(Boolean),  // React Refresh for hot reloading
          },
        },
      },
      {
        test: /\.css$/,  // Process CSS files
        use: [
          process.env.NODE_ENV === 'production' ? MiniCssExtractPlugin.loader : 'style-loader',
          'css-loader',
        ],
      },
      {
        test: /\.(png|jpe?g|gif|svg)$/i,  // Handle image files
        use: ['file-loader'],
      },
      {
        test: /\.json$/,  // Handle JSON files
        use: 'json-loader',
      },
    ],
  },
  devtool: 'eval-source-map',  // For better debugging during development
  devServer: {
    contentBase: path.join(__dirname, 'public'),
    port: 3000,
    hot: true,  // Enable hot module replacement for React Refresh
    historyApiFallback: true,  // For client-side routing with React Router
    proxy: {
      '/api': 'http://localhost:5000',  // Proxy API requests to backend (example)
    },
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html',  // HTML template for the final output
      inject: 'body',  // Injects the bundle script at the end of the body tag
    }),
    new MiniCssExtractPlugin({
      filename: 'styles.css',  // Output CSS file
    }),
    process.env.NODE_ENV !== 'production' && new ReactRefreshWebpackPlugin(),  // Enable React refresh in development
  ].filter(Boolean),
  optimization: {
    splitChunks: {
      chunks: 'all',  // Optimize vendor code by splitting it into separate chunks
    },
  },
};
# Placeholder content for frontend/webpack.config.js
