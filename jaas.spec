%define		ver		1.0_01
%define 	_ver		%(echo %{ver} | tr . _)

Summary:	Java(TM) Authentication and Authorization Service
Summary(pl.UTF-8):   JAAS - usługa uwierzytelniania i autoryzacji dla Javy
Name:		jaas
Version:	%{ver}
Release:	0.1
License:	Sun Binary Code License
Group:		Development/Languages/Java
Source0:	%{name}-%{_ver}.zip
Source1:	%{name}-%{_ver}-doc.zip
URL:		http://java.sun.com/products/jaas/
NoSource:	0
NoSource:	1
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
The Java(TM) Authentication and Authorization Service (JAAS) is a Java
package that enables services to authenticate and enforce access
controls upon users. It implements a Java version of the standard
Pluggable Authentication Module (PAM) framework, and supports
user-based authorization.

This optional package is provided for Java 1.3 and 1.3.1. It has been
integrated in Java 1.4.

%description -l pl.UTF-8
JAAS (Java(TM) Authentication and Authorization Service) to pakiet
Javy umożliwiający usługom na uwierzytelnianie oraz narzucanie
kontroli dostępu w zależności od użytkownika. Pakiet jest
implementacją javowej wersji standardowego szkieletu PAM (Pluggable
Authentication Module) i obsługuje autoryzacją w oparciu o
użytkowników.

Ten opcjonalny pakiet jest przeznaczony dla Javy 1.3 i 1.3.1; został
zintegrowany z Javą 1.4.

%prep
%setup -q -n %{name}%{_ver} -a1

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
