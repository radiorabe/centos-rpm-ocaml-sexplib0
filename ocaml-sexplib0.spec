Name:           ocaml-sexplib0
Version:        0.11.0
Release:        0.0%{?dist}
Summary:        definition of S-expressions and some base converters

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# NOTE: The license changes to MIT after the first 0.11.0 tag
License:        Apache-2.0
URL:            https://github.com/janestreet/sexplib0/
Source0:        https://github.com/janestreet/sexplib0/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  jbuilder

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

# Generate debuginfo, or try to.
sed 's/ocamlc/ocamlc -g/g' -i Makefile
sed 's/ocamlopt/ocamlopt -g/g' -i Makefile

%build
%make_build

%install
# Currently sexplib0 installs itself with ocamlfind.
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%license LICENSE.txt
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.ml
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license LICENSE.txt
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.11.0-0.0
- Initial build for pcre-ocaml package bump
