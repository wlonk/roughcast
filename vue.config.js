module.exports = {
  lintOnSave: false,
  filenameHashing: false,
  assetsDir: 'static/',
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
