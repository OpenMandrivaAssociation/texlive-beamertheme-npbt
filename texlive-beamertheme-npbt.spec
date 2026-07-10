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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
"NPBT" stands for "Norman's Pandoc Beamer Themes". Currently the
following themes are supported: Sefiroth Consulting: A private
(demonstration) theme. FOM: The layout of Hochschule FOM. FOM ifes: The
layout of Hochschule FOM, Institut fur Empirie & Statistik. eufom: The
layout of eufom.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-npbt
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-npbt
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-npbt/example
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-npbt/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-npbt/README
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-npbt/example/NPBT_exsamle.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-npbt/example/NPBT_exsamle.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-npbt/header.tex
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/beamercolorthemeNPBT_EUFOM.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/beamercolorthemeNPBT_FOM.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/beamercolorthemeNPBT_FOM_ifes.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/beamercolorthemeNPBT_SC.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/beamerouterthemeNPBT_FOM.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/beamerouterthemeNPBT_FOM_ifes.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/beamerthemeNPBT.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/LICENSE.md
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_FOM_background.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_FOM_frametitlebackground.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_FOM_ifes_backgound.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_FOM_ifes_frametitlebackgound.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_FOM_ifes_linie.pdf
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_FOM_ifes_logo.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_FOM_linie.pdf
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_FOM_logo.pdf
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_SC_background.jpg
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_SC_logo.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_eufom_backgound.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_eufom_frametitlebackgound.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_eufom_linie.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/NPBT_eufom_logo.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-npbt/images/lNPBT_SC_linie.png
