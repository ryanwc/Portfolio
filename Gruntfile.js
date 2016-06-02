module.exports = function(grunt) {

  grunt.initConfig({
    responsive_images: {
      dev: {
        options: {
          engine: 'im',
          sizes: [{
            name: 'small',
            width: '400',
            suffix: '_small',
            quality: 30
          },{
            name: 'large',
            width: '1200',
            suffix: '_large',
            quality: 30
          }]
        },
        files: [{
          expand: true,
          src: ['*.{gif,jpg,jpeg,png}'],
          cwd: 'images_s_src/',
          dest: 'images/'
        }]
      }
    },
  });

  grunt.loadNpmTasks('grunt-responsive-images');
  grunt.registerTask('default', ['responsive_images']);

};
