#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v24
# autospec commit: a88ffdc
#
Name     : R-rlang
Version  : 1.1.6
Release  : 97
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/rlang_1.1.6.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/rlang_1.1.6.tar.gz
Summary  : Functions for Base Types and Core R and 'Tidyverse' Features
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: R-rlang-lib = %{version}-%{release}
Requires: R-rlang-license = %{version}-%{release}
Requires: R-winch
BuildRequires : buildreq-R

%description
like the condition system, and core 'Tidyverse' features like tidy
  evaluation.

%package lib
Summary: lib components for the R-rlang package.
Group: Libraries
Requires: R-rlang-license = %{version}-%{release}

%description lib
lib components for the R-rlang package.


%package license
Summary: license components for the R-rlang package.
Group: Default

%description license
license components for the R-rlang package.


%prep
%setup -q -n rlang
pushd ..
cp -a rlang buildavx2
popd
pushd ..
cp -a rlang buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744404062

%install
export SOURCE_DATE_EPOCH=1744404062
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-rlang
cp %{_builddir}/rlang/LICENSE.note %{buildroot}/usr/share/package-licenses/R-rlang/4a2ee4ad4dd9dc2459b06f6b0c777a2063819b63 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/rlang/help/figures/logo.png
/usr/lib64/R/library/rlang/help/paths.rds
/usr/lib64/R/library/rlang/help/rlang.rdb
/usr/lib64/R/library/rlang/help/rlang.rdx
/usr/lib64/R/library/rlang/html/00Index.html
/usr/lib64/R/library/rlang/html/R.css
/usr/lib64/R/library/rlang/tests/sink.R
/usr/lib64/R/library/rlang/tests/testthat.R
/usr/lib64/R/library/rlang/tests/testthat/_snaps/4.5_and_older/trace.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/arg.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/attr.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/bytes.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/c-api.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/call.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/cnd-abort.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/cnd-entrace.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/cnd-handlers.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/cnd-message.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/cnd-signal.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/cnd.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/current/cnd-abort.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/dots-ellipsis.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/dots.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/env-binding.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/env.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/eval-tidy.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/fn.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/friendly-type.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/lifecycle.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/nse-defuse.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/nse-inject.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/operators.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/parse.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/pre-3.6.0/cnd-abort.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/s3.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/session.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/standalone-cli.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/standalone-downstream-deps.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/standalone-obj-type.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/standalone-rlang.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/standalone-s3-register.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/standalone-types-check.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/standalone-vctrs.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/state.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/sym.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/trace.md
/usr/lib64/R/library/rlang/tests/testthat/_snaps/types.md
/usr/lib64/R/library/rlang/tests/testthat/fixtures/Makefile
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-backtrace-conditionMessage.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-backtrace-empty.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-backtrace-parent.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-backtrace-rethrown.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-backtrace.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-entrace.R
/usr/lib64/R/library/rlang/tests/testthat/fixtures/error-show-messages.R
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
/usr/lib64/R/library/rlang/tests/testthat/helper-package.R
/usr/lib64/R/library/rlang/tests/testthat/helper-performance.R
/usr/lib64/R/library/rlang/tests/testthat/helper-print.R
/usr/lib64/R/library/rlang/tests/testthat/helper-rlang.R
/usr/lib64/R/library/rlang/tests/testthat/helper-trace.R
/usr/lib64/R/library/rlang/tests/testthat/setup-tests.R
/usr/lib64/R/library/rlang/tests/testthat/teardown-tests.R
/usr/lib64/R/library/rlang/tests/testthat/test-arg.R
/usr/lib64/R/library/rlang/tests/testthat/test-attr.R
/usr/lib64/R/library/rlang/tests/testthat/test-bytes.R
/usr/lib64/R/library/rlang/tests/testthat/test-c-api.R
/usr/lib64/R/library/rlang/tests/testthat/test-call.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd-abort.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd-entrace.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd-handlers.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd-message.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd-signal.R
/usr/lib64/R/library/rlang/tests/testthat/test-cnd.R
/usr/lib64/R/library/rlang/tests/testthat/test-deparse.R
/usr/lib64/R/library/rlang/tests/testthat/test-deprecated-vec-squash.R
/usr/lib64/R/library/rlang/tests/testthat/test-deprecated.R
/usr/lib64/R/library/rlang/tests/testthat/test-dots-ellipsis.R
/usr/lib64/R/library/rlang/tests/testthat/test-dots.R
/usr/lib64/R/library/rlang/tests/testthat/test-encoding.R
/usr/lib64/R/library/rlang/tests/testthat/test-entrace.Rmd
/usr/lib64/R/library/rlang/tests/testthat/test-env-binding.R
/usr/lib64/R/library/rlang/tests/testthat/test-env-special.R
/usr/lib64/R/library/rlang/tests/testthat/test-env.R
/usr/lib64/R/library/rlang/tests/testthat/test-eval-tidy.R
/usr/lib64/R/library/rlang/tests/testthat/test-eval.R
/usr/lib64/R/library/rlang/tests/testthat/test-expr.R
/usr/lib64/R/library/rlang/tests/testthat/test-fn.R
/usr/lib64/R/library/rlang/tests/testthat/test-formula.R
/usr/lib64/R/library/rlang/tests/testthat/test-friendly-type.R
/usr/lib64/R/library/rlang/tests/testthat/test-hash.R
/usr/lib64/R/library/rlang/tests/testthat/test-lifecycle.R
/usr/lib64/R/library/rlang/tests/testthat/test-names.R
/usr/lib64/R/library/rlang/tests/testthat/test-node.R
/usr/lib64/R/library/rlang/tests/testthat/test-nse-defuse.R
/usr/lib64/R/library/rlang/tests/testthat/test-nse-inject.R
/usr/lib64/R/library/rlang/tests/testthat/test-obj.R
/usr/lib64/R/library/rlang/tests/testthat/test-operators.R
/usr/lib64/R/library/rlang/tests/testthat/test-parent-errors.Rmd
/usr/lib64/R/library/rlang/tests/testthat/test-parse.R
/usr/lib64/R/library/rlang/tests/testthat/test-quo.R
/usr/lib64/R/library/rlang/tests/testthat/test-raw.R
/usr/lib64/R/library/rlang/tests/testthat/test-s3.R
/usr/lib64/R/library/rlang/tests/testthat/test-session.R
/usr/lib64/R/library/rlang/tests/testthat/test-stack.R
/usr/lib64/R/library/rlang/tests/testthat/test-standalone-cli.R
/usr/lib64/R/library/rlang/tests/testthat/test-standalone-downstream-deps.R
/usr/lib64/R/library/rlang/tests/testthat/test-standalone-obj-type.R
/usr/lib64/R/library/rlang/tests/testthat/test-standalone-purrr.R
/usr/lib64/R/library/rlang/tests/testthat/test-standalone-rlang.R
/usr/lib64/R/library/rlang/tests/testthat/test-standalone-s3-register.R
/usr/lib64/R/library/rlang/tests/testthat/test-standalone-types-check.R
/usr/lib64/R/library/rlang/tests/testthat/test-standalone-vctrs.R
/usr/lib64/R/library/rlang/tests/testthat/test-standalone-zeallot.R
/usr/lib64/R/library/rlang/tests/testthat/test-standalone.R
/usr/lib64/R/library/rlang/tests/testthat/test-state.R
/usr/lib64/R/library/rlang/tests/testthat/test-sym.R
/usr/lib64/R/library/rlang/tests/testthat/test-trace-full.Rmd
/usr/lib64/R/library/rlang/tests/testthat/test-trace.R
/usr/lib64/R/library/rlang/tests/testthat/test-trace.Rmd
/usr/lib64/R/library/rlang/tests/testthat/test-types.R
/usr/lib64/R/library/rlang/tests/testthat/test-utils.R
/usr/lib64/R/library/rlang/tests/testthat/test-vec-new.R
/usr/lib64/R/library/rlang/tests/testthat/test-vec-utils.R
/usr/lib64/R/library/rlang/tests/testthat/test-vec.R
/usr/lib64/R/library/rlang/tests/testthat/test-weakref.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/rlang/libs/rlang.so
/V4/usr/lib64/R/library/rlang/libs/rlang.so
/usr/lib64/R/library/rlang/libs/rlang.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-rlang/4a2ee4ad4dd9dc2459b06f6b0c777a2063819b63
