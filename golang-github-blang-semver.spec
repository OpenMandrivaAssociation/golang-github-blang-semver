# http://github.com/blang/semver
%global goipath         github.com/blang/semver
Version:                3.5.1

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Semantic Versioning library written in golang
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .


%install
%goinstall glide.lock glide.yaml


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Oct 31 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.5.1-1
- Release 3.5.1

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 3.3.0-0.9.git60ec348
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-0.8.git60ec348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 3.3.0-0.7.git60ec348
- Upload glide.lock and glide.yaml

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 3.3.0-0.6.20160701git60ec348
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-0.5.git60ec348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-0.4.git60ec348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-0.3.git60ec348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-0.2.git60ec348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git60ec348
- First package for Fedora
  resolves: #1412152
