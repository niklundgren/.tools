This will throw an error if run without
editing out these three lines, and changing
CMAKE_INSTALL PREFIX (line 15).

set(PKG_SNAP ON CACHE BOOL "" FORCE)
set(PKG_KSPACE ON CACHE BOOL "" FORCE)
set(PKG_MANYBODY ON CACHE BOOL "" FORCE)
set(PKG_MOLECULE ON CACHE BOOL "" FORCE)
set(PKG_USER-PHONON ON CACHE BOOL "" FORCE)
set(BUILD_SHARED_LIBS ON CACHE BOOL "" FORCE)
set(LAMMPS_EXCEPTIONS "yes" CACHE STRING "" FORCE)
set(CMAKE_INSTALL_PREFIX "/home/nwlundgren/develop/lammps/cmake/" CACHE STRING "" FORCE)
set(PKG_USER-QUIP ON CACHE BOOL "" FORCE)
set(QUIP_LIBRARY "/home/nwlundgren/develop/QUIP/build/linux_x86_64_gfortran_openmp/libquip.a" CACHE STRING "" FORCE)
set(FFT "KISS" CACHE STRING "" FORCE)
