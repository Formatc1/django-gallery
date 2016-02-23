var gulp = require('gulp');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('gulp-autoprefixer');
var browserSync = require('browser-sync');
var reload = browserSync.reload;
var url = require('url');
var proxy = require('proxy-middleware');
var exec = require('child_process').exec;
var notify = require('gulp-notify');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');

var scripts = [
  'static_dev/js/jquery-2.1.4.min.js',
  'static_dev/js/bin/materialize.min.js',
  'static_dev/js/scripts.js'
];

var AUTOPREFIXER_BROWSERS = [
  'Android 2.3',
  'Android >= 4',
  'Chrome >= 20',
  'Firefox >= 24',
  'Explorer >= 8',
  'iOS >= 6',
  'Opera >= 12',
  'Safari >= 6'
];

gulp.task('runserver', function () {
  var proc = exec('python manage.py runserver');
});

gulp.task('collectstatic', function () {
  var proc = exec('python manage.py collectstatic --noinput ');
});

gulp.task('sass', function() {
    return gulp.src('static_dev/sass/style.scss')
    .pipe(sourcemaps.init())
    .pipe(sass())
    .on('error', notify.onError(function (error) {
      return 'Sass error: ' + error.formatted;
    }))
    .pipe(sourcemaps.write())
    .pipe(autoprefixer({browsers: AUTOPREFIXER_BROWSERS}))
    .pipe(gulp.dest('static/css'))
    .pipe(reload({
        stream: true
    }));
});

gulp.task('scripts', function() {
  return gulp.src(scripts)
  .pipe(concat('scripts.js'))
  .pipe(uglify())
  .on('error', notify.onError(function (error) {
    return 'JS error: ' + error.message;
  }))
  .pipe(gulp.dest('static/js'));
});

gulp.task('images', function() {
  return gulp.src('static_dev/images/**/*')
  .pipe(gulp.dest('static/img'));
});

gulp.task('default', ['collectstatic', 'images', 'scripts', 'sass', 'runserver'], function () {
  browserSync({
    notify: false,
    proxy: 'http://localhost:8000/',
    serveStatic: ['.', './static']
  });

  gulp.watch(['*/templates/**/*.html'], reload);
  gulp.watch(['**/*.py'], reload);
  gulp.watch(['static_dev/sass/**/*.scss'], ['sass']);
  gulp.watch(['static_dev/images/**/*'], ['images']);
  gulp.watch(['static_dev/js/**/*.js'], ['scripts']);
  // gulp.watch(['static/css/**/*.css'], reload);
  gulp.watch(['static/js/**/*.js'], reload);
  gulp.watch(['static/img/**/*'], reload);
});
