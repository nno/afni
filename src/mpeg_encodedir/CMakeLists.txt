add_afni_executable(
  mpeg_encode
  bframe.c
  bitio.c
  block.c
  bsearch.c
  combine.c
  frame.c
  frametype.c
  fsize.c
  huff.c
  iframe.c
  jrevdct.c
  libpnmrw.c
  main.c
  mfwddct.c
  mheaders.c
  mpeg.c
  nojpeg.c
  opts.c
  parallel.c
  param.c
  pframe.c
  postdct.c
  psearch.c
  rate.c
  readframe.c
  rgbtoycc.c
  specifics.c
  subsample.c
)
target_include_directories(
  mpeg_encode PRIVATE $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/headers>
)
target_link_libraries(mpeg_encode m)