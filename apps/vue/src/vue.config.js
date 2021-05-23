const BundleTracker = require("webpack-bundle-tracker");

const pages = {
  'app1': {
    entry: './app1.js',
    chunks: ['chunk-vendors']
  },
  'app2': {
    entry: './app2.js',
    chunks: ['chunk-vendors']
  },
}

module.exports = {
  pages: pages,
  filenameHashing: false,
  productionSourceMap: false,
  publicPath: process.env.NODE_ENV === 'production'
    ? ''
    : 'http://localhost:8080/',
  outputDir: '../static/vue/',

  chainWebpack: config => {

    config.optimization
      .splitChunks({
        cacheGroups: {
          vendor: {
            test: /[\\/]node_modules[\\/]/,
            name: "chunk-vendors",
            chunks: "all",
            priority: 1
          },
        },
      });

    Object.keys(pages).forEach(page => {
      config.plugins.delete(`html-${page}`);
      config.plugins.delete(`preload-${page}`);
      config.plugins.delete(`prefetch-${page}`);
    })

    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{filename: './webpack-stats.json'}]);

    config.resolve.alias
      .set('__STATIC__', 'static')

    config.devServer
      .public('http://0.0.0.0:8080')
      .host('0.0.0.0')
      .port(8080)
      .hotOnly(true)
      .watchOptions({poll: 1000})
      .https(false)
      .disableHostCheck(true)
      .headers({"Access-Control-Allow-Origin": ["*"]})

  }
};
