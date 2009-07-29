%define upstream_name    Class-Gomor
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Class::Gomor - another class and object builder
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GO/GOMOR/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Obsoletes:  perl-Class-Gomor-Hash
Provides:   perl-Class-Gomor-Hash

%description
This module is yet another class builder. This one adds parameter checking in
new constructor, that is to check for attributes existence, and definedness.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
