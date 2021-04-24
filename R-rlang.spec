#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rlang
Version  : 0.4.10
Release  : 61
URL      : https://cran.r-project.org/src/contrib/rlang_0.4.10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rlang_0.4.10.tar.gz
Summary  : Functions for Base Types and Core R and 'Tidyverse' Features
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: R-rlang-lib = %{version}-%{release}
Requires: R-winch
BuildRequires : R-winch
BuildRequires : buildreq-R

%description
like the condition system, and core 'Tidyverse' features like tidy
  evaluation.

%package lib
Summary: lib components for the R-rlang package.
Group: Libraries

%description lib
lib components for the R-rlang package.


%prep
%setup -q -c -n rlang
cd %{_builddir}/rlang

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609806000

%install
export SOURCE_DATE_EPOCH=1609806000
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rlang
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rlang
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rlang
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rlang || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rlang/DESCRIPTION
/usr/lib64/R/library/rlang/INDEX
/usr/lib64/R/library/rlang/LICENSE
/usr/lib64/R/library/rlang/Meta/Rd.rds
/usr/lib64/R/library/rlang/Meta/features.rds
/usr/lib64/R/library/rlang/Meta/hsearch.rds
/usr/lib64/R/library/rlang/Meta/links.rds
/usr/lib64/R/library/rlang/Meta/nsInfo.rds
/usr/lib64/R/library/rlang/Meta/package.rds
/usr/lib64/R/library/rlang/NAMESPACE
/usr/lib64/R/library/rlang/NEWS.md
/usr/lib64/R/library/rlang/R/rlang
/usr/lib64/R/library/rlang/R/rlang.rdb
/usr/lib64/R/library/rlang/R/rlang.rdx
/usr/lib64/R/library/rlang/backtrace-ver
/usr/lib64/R/library/rlang/help/AnIndex
/usr/lib64/R/library/rlang/help/aliases.rds
/usr/lib64/R/library/rlang/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/rlang/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/rlang/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/rlang/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/rlang/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/rlang/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/rlang/help/figures/lifecycle-retired.svg
/usr/lib64/R/library/rlang/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/rlang/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/rlang/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/rlang/help/figures/rlang.png
/usr/lib64/R/library/rlang/help/paths.rds
/usr/lib64/R/library/rlang/help/rlang.rdb
/usr/lib64/R/library/rlang/help/rlang.rdx
/usr/lib64/R/library/rlang/html/00Index.html
/usr/lib64/R/library/rlang/html/R.css
/usr/lib64/R/library/rlang/tests/sink.R
/usr/lib64/R/library/rlang/tests/testthat.R
/usr/lib64/R/library/rlang/tests/testthat/_snaps/arg.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/cnd-abort.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/cnd-entrace.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/cnd-error.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/cnd-signal.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/env-special.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/operators.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/trace.md
/usr/lib64/R/library/rlang/tests/testthat/fixtures/Makefile
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-backtrace-conditionMessage.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-backtrace-empty.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-backtrace-parent.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-backtrace-rethrown.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-backtrace.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-entrace.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/lib.zip
/usr/lib64/R/library/rlang/tests/testthat/fixtures/rlanglibtest/DESCRIPTION
/usr/lib64/R/library/rlang/tests/testthat/fixtures/rlanglibtest/NAMESPACE
/usr/lib64/R/library/rlang/tests/testthat/fixtures/rlanglibtest/R/rlanglibtest.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/rlanglibtest/src/Makevars
/usr/lib64/R/library/rlang/tests/testthat/fixtures/rlanglibtest/src/init.c
/usr/lib64/R/library/rlang/tests/testthat/fixtures/rlanglibtest/src/test-quo-accessors.c
/usr/lib64/R/library/rlang/tests/testthat/fixtures/rlanglibtest/tests/testthat.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/rlanglibtest/tests/testthat/test-quo-accessors.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/trace-srcref.R
/usr/lib64/R/library/rlang/tests/testthat/helper-c-api.R
/usr/lib64/R/library/rlang/tests/testthat/helper-capture.R
/usr/lib64/R/library/rlang/tests/testthat/helper-cli.R
/usr/lib64/R/library/rlang/tests/testthat/helper-cnd.R
/usr/lib64/R/library/rlang/tests/testthat/helper-locale.R
/usr/lib64/R/library/rlang/tests/testthat/helper-print.R
/usr/lib64/R/library/rlang/tests/testthat/helper-rlang.R
/usr/lib64/R/library/rlang/tests/testthat/helper-stack.R
/usr/lib64/R/library/rlang/tests/testthat/helper-trace.R
/usr/lib64/R/library/rlang/tests/testthat/setup-tests.R
/usr/lib64/R/library/rlang/tests/testthat/teardown-tests.R
/usr/lib64/R/library/rlang/tests/testthat/test-arg.R
/usr/lib64/R/library/rlang/tests/testthat/test-attr.R
/usr/lib64/R/library/rlang/tests/testthat/test-c-api.R
/usr/lib64/R/library/rlang/tests/testthat/test-call.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd-abort.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd-entrace.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd-error.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd-handlers.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd-message.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd-signal.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd.R
/usr/lib64/R/library/rlang/tests/testthat/test-compat-zeallot.R
/usr/lib64/R/library/rlang/tests/testthat/test-compat.R
/usr/lib64/R/library/rlang/tests/testthat/test-deparse.R
/usr/lib64/R/library/rlang/tests/testthat/test-dots.R
/usr/lib64/R/library/rlang/tests/testthat/test-encoding.R
/usr/lib64/R/library/rlang/tests/testthat/test-env-binding.R
/usr/lib64/R/library/rlang/tests/testthat/test-env-special.R
/usr/lib64/R/library/rlang/tests/testthat/test-env.R
/usr/lib64/R/library/rlang/tests/testthat/test-eval-tidy.R
/usr/lib64/R/library/rlang/tests/testthat/test-eval.R
/usr/lib64/R/library/rlang/tests/testthat/test-expr.R
/usr/lib64/R/library/rlang/tests/testthat/test-fn.R
/usr/lib64/R/library/rlang/tests/testthat/test-formula.R
/usr/lib64/R/library/rlang/tests/testthat/test-hash.R
/usr/lib64/R/library/rlang/tests/testthat/test-lifecycle.R
/usr/lib64/R/library/rlang/tests/testthat/test-node.R
/usr/lib64/R/library/rlang/tests/testthat/test-nse-defuse.R
/usr/lib64/R/library/rlang/tests/testthat/test-nse-force.R
/usr/lib64/R/library/rlang/tests/testthat/test-operators.R
/usr/lib64/R/library/rlang/tests/testthat/test-parse.R
/usr/lib64/R/library/rlang/tests/testthat/test-quo.R
/usr/lib64/R/library/rlang/tests/testthat/test-raw.R
/usr/lib64/R/library/rlang/tests/testthat/test-retired.R
/usr/lib64/R/library/rlang/tests/testthat/test-s3.R
/usr/lib64/R/library/rlang/tests/testthat/test-sexp.R
/usr/lib64/R/library/rlang/tests/testthat/test-stack.R
/usr/lib64/R/library/rlang/tests/testthat/test-state.R
/usr/lib64/R/library/rlang/tests/testthat/test-sym.R
/usr/lib64/R/library/rlang/tests/testthat/test-trace.R
/usr/lib64/R/library/rlang/tests/testthat/test-trace.Rmd
/usr/lib64/R/library/rlang/tests/testthat/test-types.R
/usr/lib64/R/library/rlang/tests/testthat/test-utils.R
/usr/lib64/R/library/rlang/tests/testthat/test-vec-new.R
/usr/lib64/R/library/rlang/tests/testthat/test-vec-squash.R
/usr/lib64/R/library/rlang/tests/testthat/test-vec-utils.R
/usr/lib64/R/library/rlang/tests/testthat/test-vec.R
/usr/lib64/R/library/rlang/tests/testthat/test-weakref.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rlang/libs/rlang.so
/usr/lib64/R/library/rlang/libs/rlang.so.avx2
/usr/lib64/R/library/rlang/libs/rlang.so.avx512
