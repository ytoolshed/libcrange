Name:		libcrange
Version:	1.0.1
Release:	1%{?dist}
Summary:	C version of range

Group:		Base
License:	GPL
URL:		http://github.com/imeyer/libcrange
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description


%prep
%setup -q


%build
aclocal || exit 1
libtoolize --force || exit 1
autoheader || exit 1
automake -a || exit 1
autoconf || exit 1
%configure --prefix=/usr
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog

