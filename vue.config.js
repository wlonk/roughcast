module.exports = {
  lintOnSave: false,
  filenameHashing: false,
  assetsDir: process.env.NODE_ENV === 'production' ? '' : 'static/',
  devServer: {
    proxy: 'http://localhost:8000',
    writeToDisk: true,
  },
  configureWebpack: {
    output: {
      filename: 'js/[name].js',
    },
  },
};
