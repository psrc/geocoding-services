library(reticulate)
library(tidyverse)

repo.dir <- "C:/Users/CLam/Desktop/geocoding-services/prep"

dir <- "J:/Projects/Geocoding/19GEOCODING/Setup/1Raw/King"
setwd(dir)

files <- list.files(dir, pattern = ".zip")
unzip.files <- partial(unzip, junkpaths = TRUE)

walk(files, unzip.files)

source(file.path(repo.dir, "king_reporject.py"))