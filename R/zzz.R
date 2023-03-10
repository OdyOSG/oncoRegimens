#Source python functions on load
.onLoad <- function(libname, pkgname) {
  print("Sourcing python files...")
  reticulate::source_python(system.file("./python/init.py",package="oncoRegimens"),envir=globalenv())
  reticulate::source_python(system.file("./python/score.py",package="oncoRegimens"),envir=globalenv())
  reticulate::source_python(system.file("./python/align.py",package="oncoRegimens"),envir=globalenv())
  reticulate::source_python(system.file("./python/main.py",package="oncoRegimens"),envir=globalenv())
}
