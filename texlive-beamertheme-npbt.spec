%global tl_name beamertheme-npbt
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.1
Release:	%{tl_revision}.1
Summary:	A collection of LaTeX beamer themes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-npbt
License:	gpl3 pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-npbt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-npbt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
"NPBT" stands for "Norman's Pandoc Beamer Themes". Currently the
following themes are supported: Sefiroth Consulting: A private
(demonstration) theme. FOM: The layout of Hochschule FOM. FOM ifes: The
layout of Hochschule FOM, Institut fur Empirie & Statistik. eufom: The
layout of eufom.

