%global py_setup_args WX_CONFIG=/usr/bin/wx-config-3.0 WXPORT=gtk3
Name:           wxPython
Version:        3.0.2.0
Release:        25
Summary:        GUI toolkit for the Python programming language
License:        LGPLv2+ and wxWidgets
URL:            http://www.wxpython.org/
Source0:        http://downloads.sourceforge.net/wxpython/%{name}-src-%{version}.tar.bz2
# Remove Editra - it doesn't work an is technically a bundle.
Patch0001:         fix-editra-removal.patch
# fix print format
Patch0002:         wxPython-3.0.0.0-format.patch
# crash when GetHandle() called on wx.Frame if unrealized
# http://trac.wxeidgets.org/ticket/16765
Patch0003:         wxPython-3.0.2.0-getxwindowcrash.patch
# wx.plot.lib broken in classic
# http://trac.wxeidgets.org/ticket/16767
Patch0004:         wxPython-3.0.2.0-plot.patch
# SetSize with default height on wxTextCtrl while hidden after parameter
# change results in zero height with wxGTK3
# http://trac.wxeidgets.org/ticket/17160
Patch0005:         wxPython-3.0.2.0-listctrl-mixin-edit.patch
# python-wxgtk3.0 can't use wx.html2
# http://bugs.debian.org/821934
Patch0006:         wxPython-3.0.2.0-webview-optional.patch
# fix version mismatching
Patch0007:         wxPython-3.0.2.0-suppress-version-mismatch-warning.patch
# add wxcairo support for pycairo
# https://github.com/wxWidgets/wxPython/pull/23
Patch0008:         wxPython-3.0.2.0-fix-wxcairo.patch
BuildRequires:  gcc-c++ wxGTK3-devel >= 3.0.0 python2-devel

%description
wxPython is a GUI toolkit for the Python programming language. It allows\
Python programmers to create programs with a robust, highly functional\
graphical user interface, simply and easily. It is implemented as a Python\
extension module (native code) that wraps the popular wxWindows cross\
platform GUI library, which is written in C++.

%package -n python2-wxpython
Summary:        GUI toolkit for the Python programming language
%python_provide python2-wxpython
Provides:       wxPython = %{version}-%{release}
Obsoletes:      wxPython < %{version}-%{release}

%description -n python2-wxpython
wxPython is a GUI toolkit for the Python programming language. It allows\
Python programmers to create programs with a robust, highly functional\
graphical user interface, simply and easily. It is implemented as a Python\
extension module (native code) that wraps the popular wxWindows cross\
platform GUI library, which is written in C++.

%package        devel
Summary:        Development files for wxPython add-on modules
Requires:       python2-wxpython = %{version}-%{release}
Requires:       wxGTK3-devel
BuildArch:      noarch

%description devel
This package includes C++ header files and SWIG files needed for developing
add-on modules for wxPython. It is NOT needed for development of most
programs which use the wxPython toolkit.

%package        help
Summary:        Documentation and samples for wxPython
Requires:       python2-wxpython = %{version}-%{release}
Provides:       wxPython-docs = %{version}-%{release}
Obsoletes:      wxPython-docs < %{version}-%{release}
BuildArch:      noarch

%description help
Documentation, samples and demo application for wxPython.

%package -n python2-wxpython-webview
Summary:        WebView add-on for wxPython
Requires:       python2-wxpython%{?_isa} = %{version}-%{release}
%python_provide python2-wxpython-webview
Provides:       wxPython-webview = %{version}-%{release}
Obsoletes:      wxPython-webview < %{version}-%{release}

%description -n python2-wxpython-webview
This package contains the optional WebView (html2) module for wxPython.

%prep
%autosetup -n wxPython-src-%{version} -p1
sed -i -e 's|/usr/lib|%{_libdir}|' -e 's|-O3|-O2|' wxPython/config.py

%build
cd wxPython
%py2_build

%install
cd wxPython
%py2_install
mv $RPM_BUILD_ROOT%{python2_sitelib}/wx.pth  $RPM_BUILD_ROOT%{python2_sitearch}
mv $RPM_BUILD_ROOT%{python2_sitelib}/wxversion.py* $RPM_BUILD_ROOT%{python2_sitearch}

%files -n python2-wxpython
%license wxPython/licence/*
%{_bindir}/*
%{python2_sitelib}/*
%exclude %{python2_sitearch}/wx-3.0-gtk3/wx/*html2.*
%{python2_sitearch}/*

%files devel
%dir %{_includedir}/wx-3.0/wx/wxPython
%{_includedir}/wx-3.0/wx/wxPython/*.h
%dir %{_includedir}/wx-3.0/wx/wxPython/i_files
%{_includedir}/wx-3.0/wx/wxPython/i_files/{*.i,*.py*,*.swg}

%files help
%doc wxPython/docs wxPython/demo wxPython/samples

%files -n python2-wxpython-webview
%{python2_sitearch}/wx-3.0-gtk3/wx/*html2.*

%changelog
* Thu Mar 12 2020 gulining<gulining1@huawei.com> - 3.0.2.0-25
- Package init
