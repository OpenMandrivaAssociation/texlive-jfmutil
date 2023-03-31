Name:		texlive-jfmutil
Version:	60987
Release:	2
Summary:	Utility to process pTeX-extended TFM and VF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jfmutil
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jfmutil.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jfmutil.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This program provides functionality to process data files (JFM
and VF) that form logical fonts used in (u)pTeX. The functions
currently available include: The mutual conversion between
Japanese virtual fonts (pairs of VF and JFM) and files in the
"ZVP format", which is an original text format representing
data in virtual fonts. This function can be seen as a
counterpart to the vftovp/vptovf programs. The mutual
conversion between VF files alone and files in the "ZVP0
format", which is a subset of the ZVP format.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/jfmutil
%doc %{_texmfdistdir}/texmf-dist/doc/fonts/jfmutil

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
