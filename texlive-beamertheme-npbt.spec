Name:		texlive-beamertheme-npbt
Version:	54512
Release:	2
Summary:	A collection of LaTeX beamer themes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-npbt
License:	gpl3 pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-npbt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-npbt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
"NPBT" stands for "Norman's Pandoc Beamer Themes". Currently
the following themes are supported: Sefiroth Consulting: A
private (demonstration) theme. FOM: The layout of Hochschule
FOM. FOM ifes: The layout of Hochschule FOM, Institut fur
Empirie & Statistik. eufom: The layout of eufom.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamertheme-npbt
%doc %{_texmfdistdir}/doc/latex/beamertheme-npbt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
