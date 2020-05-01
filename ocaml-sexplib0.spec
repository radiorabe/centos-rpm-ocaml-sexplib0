%define debug_package %{nil}


Name:           ocaml-sexplib0
Version:        0.13.0
Release:        0.1%{?dist}
Summary:        definition of S-expressions and some base converters

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:        MIT
URL:            https://github.com/janestreet/sexplib0/
Source0:        https://github.com/janestreet/sexplib0/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib

%description
A Part of Jane Street's Core library The Core suite of libraries is
an industrial strength alternative to OCaml's standard library that
was developed by Jane Street.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{libname}-%{version}

%build
%make_build

%install
# Currently sexplib0 installs itself with ocamlfind.
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{_libdir}/ocaml/
mkdir -p $OCAMLFIND_DESTDIR
# using dune install so I can set libdir (rather than make install)
dune install --prefix=$OCAMLFIND_DESTDIR --libdir=$OCAMLFIND_DESTDIR

%files
%doc %{_libdir}/ocaml/doc/%{libname}/
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.ml
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Fri May  1 2020 Lucas Bickel <hairmare@rabe.ch> - 1.13.0-0.1
* Bump version to 0.13.0

* Sat Aug  3 2019 Lucas Bickel <hairmare@rabe.ch> - 1.12.0-0.1
- Fix install location

* Wed Jul 17 2019 Lucas Bickel <hairmare@rabe.ch> - 0.12.0-0.0
- Bump version to 0.12.0
- Build with ocaml-dune instead of jbuilder

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.11.0-0.0
- Initial build for pcre-ocaml package bump
