cmake ../ -DCMAKE_INSTALL_PREFIX=. -DBLAS=mkl -DBLAS_ROOT=/usr/share/intel-mkl -DWITH_MPI=ON -DCMAKE_CXX_COMPILER=/usr/bin/g++-9 -DCMAKE_C_COMPILER=/usr/bin/gcc-9 -DCMAKE_Fortran_COMPILER=/usr/bin/gfortran-9 -DWITH_SYSTEM_BLAS=OFF