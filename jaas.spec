%define		ver		1.0
%define 	_ver		1_0

Summary:	Java(TM) Authentication and Authorization Service
Name:		jaas
Version:	1.0
Release:	0.1
License:	Sun Binary Code License
URL:		http://java.sun.com/products/%{name}
Group:		Development/Languages/Java
Source0:	%{name}%{_ver}.zip
Source1:	%{name}%{_ver}-doc.zip
NoSource:	0
NoSource:	1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java


%description
The JavaTM Authentication and Authorization Service (JAAS) is a Java
package that enables services to authenticate and enforce access
controls upon users. It implements a Java version of the standard
Pluggable Authentication Module (PAM) framework, and supports user-based
authorization.

This optional package is provided for Java 1.3 and 1.3.1. It has been
integrated in Java 1.4

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{name}%{_ver}
%setup -q -n %{name}%{_ver} -T -D -a1

%build
exit 0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
cp lib/%{name}.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf %{name}.jar $RPM_BUILD_ROOT%{_javalibdir}/%{extension}-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* %{name}%{_ver}-doc/apidoc
%{_javalibdir}/%{name}*.jar
