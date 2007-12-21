%define module Class-Gomor

Summary:	Class::Gomor - another class and object builder
Name:		perl-%{module}
Version:	1.01
Release:	%mkrel 1
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GO/GOMOR/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module is yet another class builder. This one adds parameter checking in
new constructor, that is to check for attributes existence, and definedness.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE LICENSE.Artistic README
%dir %{perl_vendorlib}/Class/Gomor
%{perl_vendorlib}/Class/Gomor/*.pm
%{perl_vendorlib}/Class/Gomor.pm
%{_mandir}/*/*

