Summary:	EDC syntax support for Vim
Summary(pl.UTF-8):	Obsługa składni EDC dla Vima
Name:		vim-addon-efl
Version:	1.11
%define	snap	20191002
%define	rel	1
Release:	0.%{snap}.%{rel}
License:	unknown
Group:		Applications/Editors/Vim
# git clone https://git.enlightenment.org/misc/vim-configs
# git archive --prefix=vim-configs/
Source0:	vim-configs-%{snap}.tar.xz
# Source0-md5:	7e9c815a4a5b7a7966bc3d666721caa7
URL:		https://git.enlightenment.org/misc/vim-configs
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	vim-rt
Obsoletes:	vim-syntax-edc < 1.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description -n vim-addon-efl
EDC syntax support for Vim.

%description -n vim-addon-efl -l pl.UTF-8
Obsługa składni EDC dla Vima.

%prep
%setup -q -n vim-configs

%install
install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles
cp -pr autoload $RPM_BUILD_ROOT%{_datadir}/vim
cp -pr {ftdetect,ftplugin,indent,snippets,syntax} $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles

%files
%defattr(644,root,root,755)
%{_datadir}/vim/autoload/edccomplete.vim
%{_datadir}/vim/vimfiles/ftdetect/edc.vim
%{_datadir}/vim/vimfiles/ftdetect/eet.vim
%{_datadir}/vim/vimfiles/ftdetect/eo.vim
%{_datadir}/vim/vimfiles/ftplugin/edc.vim
%{_datadir}/vim/vimfiles/indent/edc.vim
# owner?
%dir %{_datadir}/vim/vimfiles/snippets
%{_datadir}/vim/vimfiles/snippets/edc.snippets
%{_datadir}/vim/vimfiles/syntax/edc.vim
%{_datadir}/vim/vimfiles/syntax/eet.vim
%{_datadir}/vim/vimfiles/syntax/embryo.vim
%{_datadir}/vim/vimfiles/syntax/eo.vim
