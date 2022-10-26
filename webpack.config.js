var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");

const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
  context: __dirname,
  entry: ["@babel/polyfill", "./app/shared/static/main.js"],
  output: {
    path: path.resolve("./app/shared/static/webpack_bundles/"),
    filename: "[name].js",
  },
  watchOptions: {
    ignored: /node_modules/,
    poll: 1000,
  },
  module: {
    rules: [
      {
        test: /\.m?js$/,
        exclude: /(node_modules)/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
          // plugins: [
          //    "@babel/plugin-proposal-optional-chaining",
          // ],
        },
      },
      {
        test: /\.(png|gif|jpg|mp4|jpeg|svg)$/,
        loader: "url-loader",
        options: {
          limit: 8000,
          name: "[name].[md5:hash:hex:12].[ext]",
        },
      },
      {
        test: /\.(ttf|eot|woff|woff2)$/,
        use: {
          loader: "file-loader",
        },
      },
      {
        test: /\.(ogv|mp4|m4v|webm)$/,
        use: {
          loader: "file-loader",
        },
      },
      {
        test: /\.(scss|css)$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          "postcss-loader",
          "sass-loader",
        ],
      },
    ],
  },
  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: "./webpack-stats.json",
    }),
    new MiniCssExtractPlugin({
      filename: "main.css",
    }),
    new CleanWebpackPlugin(),
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery",
      "window.jQuery": "jquery",
    }),
    new CopyPlugin({
      patterns: [{ from: "app/shared/static/images/*", to: "../images" }],
    }),
  ],
};
