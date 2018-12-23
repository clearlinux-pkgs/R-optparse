#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-optparse
Version  : 1.6.0
Release  : 12
URL      : https://cran.r-project.org/src/contrib/optparse_1.6.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/optparse_1.6.0.tar.gz
Summary  : Command Line Option Parser
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-getopt
Requires: R-stringi
BuildRequires : R-getopt
BuildRequires : R-stringi
BuildRequires : clr-R-helpers

%description
be used with Rscript to write "#!" shebang scripts that accept short and
    long flag/options.

%prep
%setup -q -c -n optparse

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529290006

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1529290006
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optparse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optparse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optparse
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library optparse|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/optparse/COPYRIGHTS
/usr/lib64/R/library/optparse/DESCRIPTION
/usr/lib64/R/library/optparse/INDEX
/usr/lib64/R/library/optparse/Meta/Rd.rds
/usr/lib64/R/library/optparse/Meta/features.rds
/usr/lib64/R/library/optparse/Meta/hsearch.rds
/usr/lib64/R/library/optparse/Meta/links.rds
/usr/lib64/R/library/optparse/Meta/nsInfo.rds
/usr/lib64/R/library/optparse/Meta/package.rds
/usr/lib64/R/library/optparse/Meta/vignette.rds
/usr/lib64/R/library/optparse/NAMESPACE
/usr/lib64/R/library/optparse/NEWS.md
/usr/lib64/R/library/optparse/R/optparse
/usr/lib64/R/library/optparse/R/optparse.rdb
/usr/lib64/R/library/optparse/R/optparse.rdx
/usr/lib64/R/library/optparse/doc/index.html
/usr/lib64/R/library/optparse/doc/optparse.R
/usr/lib64/R/library/optparse/doc/optparse.Rrst
/usr/lib64/R/library/optparse/doc/optparse.html
/usr/lib64/R/library/optparse/exec/display_file.R
/usr/lib64/R/library/optparse/exec/example.R
/usr/lib64/R/library/optparse/help/AnIndex
/usr/lib64/R/library/optparse/help/aliases.rds
/usr/lib64/R/library/optparse/help/optparse.rdb
/usr/lib64/R/library/optparse/help/optparse.rdx
/usr/lib64/R/library/optparse/help/paths.rds
/usr/lib64/R/library/optparse/html/00Index.html
/usr/lib64/R/library/optparse/html/R.css
