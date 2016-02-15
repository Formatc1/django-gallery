var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var browserSync = require('browser-sync');
var reload = browserSync.reload;
var url = require('url');
var proxy = require('proxy-middleware');
var exec = require('child_process').exec;
var notify = require('gulp-notify');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');

var AUTOPREFIXER_BROWSERS = [
  'ie >= 10',
  'ie_mob >= 10',
  'ff >= 30',
  'chrome >= 34',
  'safari >= 7',
  'opera >= 23',
  'ios >= 7',
  'android >= 4.4',
  'bb >= 10'
];

gulp.task('runserver', function () {
  var proc = exec('python manage.py runserver');
});

gulp.task('collectstatic', function () {
  var proc = exec('python manage.py collectstatic --noinput ');
});

gulp.task('sass', function() {
    return gulp.src('static_dev/scss/**/*.scss')
    .pipe(sass())
    .on('error', notify.onError(function (error) {
      return 'Sass error: ' + error.formatted;
    }))
    .pipe(autoprefixer({browsers: AUTOPREFIXER_BROWSERS}))
    .pipe(gulp.dest('static/css'))
    .pipe(reload({
        stream: true
    }));
});

gulp.task('scripts', function() {
  return gulp.src('static_dev/js/**/*.js')
  .pipe(concat('scripts.js'))
  .pipe(uglify())
  .on('error', notify.onError(function (error) {
    return 'JS error: ' + error.message;
  }))
  .pipe(gulp.dest('static/js'));
});

gulp.task('images', function() {
  return gulp.src('static_dev/img/**/*')
  .pipe(gulp.dest('static/img'));
});

gulp.task('default', ['collectstatic', 'images', 'scripts', 'sass', 'runserver'], function () {
  browserSync({
    notify: false,
    proxy: 'http://localhost:8000/',
    serveStatic: ['.', './static']
  });

  gulp.watch(['*/templates/**/*.html', '*/mustache/**/*.mustache'], reload);
  gulp.watch(['**/*.py'], reload);
  gulp.watch(['static_dev/scss/**/*.scss'], ['sass']);
  gulp.watch(['static_dev/img/**/*'], ['images']);
  gulp.watch(['static_dev/js/**/*.js'], ['scripts']);
  // gulp.watch(['static/css/**/*.css'], reload);
  gulp.watch(['static/js/**/*.js'], reload);
  gulp.watch(['static/img/**/*'], reload);
});
