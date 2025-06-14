#
# Conditional build:
%bcond_without	tests		# unit tests
#
Summary:	AWS C Common library
Summary(pl.UTF-8):	Biblioteka AWS C Common
Name:		aws-c-common
Version:	0.12.3
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/awslabs/aws-c-common
Source0:	https://github.com/awslabs/aws-c-common/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	48aa6f6b66b8fcaaaa54258e284cd2dc
URL:		https://github.com/awslabs/aws-c-common
BuildRequires:	cmake >= 3.9
BuildRequires:	gcc >= 5:3.2
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Core C99 package for AWS SDK for C. Includes cross-platform
primitives, configuration, data structures, and error handling.

%description -l pl.UTF-8
Główny pakiet C99 dla AWS SDK dla języka C. Zawiera wieloplatformowe
podstawy, konfigurację, struktury danych i obsługę błędów.

%package devel
Summary:	Header files for AWS C Common library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AWS C Common
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for AWS C Common library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AWS C Common.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NOTICE README.md THIRD-PARTY-LICENSES.txt
%attr(755,root,root) %{_libdir}/libaws-c-common.so.*.*.*
%{_libdir}/libaws-c-common.so.1

%files devel
%defattr(644,root,root,755)
%doc docs/error-handling.md
%{_libdir}/libaws-c-common.so
%dir %{_includedir}/aws
%{_includedir}/aws/common
%{_includedir}/aws/testing
%{_libdir}/cmake/aws-c-common
