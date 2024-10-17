Name:		texlive-epigraph-keys
Version:	61719
Release:	2
Summary:	Epigraphs using key values
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/epigraph-keys
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigraph-keys.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigraph-keys.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package lays out epigraphs: quotations across a page,
usually to open or close a chapter. It is intended as a simple
replacement for the more sophisticated epigraph package. The
package depends on pgfkeys, conditionals (which is distributed
as part of the songbook package), enumitem, and microtype.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/epigraph-keys
%doc %{_texmfdistdir}/doc/latex/epigraph-keys

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
