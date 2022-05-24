%global py_setup_args WX_CONFIG=/usr/bin/wx-config-3.0 WXPORT=gtk3
Name:           wxPython
Version:        4.1.1
Release:        1
Summary:        GUI toolkit for the Python programming language
License:        LGPLv2+ and wxWidgets
URL:            http://www.wxpython.org/
Source0:        https://files.pythonhosted.org/packages/b0/4d/80d65c37ee60a479d338d27a2895fb15bbba27a3e6bb5b6d72bb28246e99/wxPython-4.1.1.tar.gz
BuildRequires:  gcc-c++ wxGTK3-devel >= 3.0.0 python-devel

%description
wxPython is a GUI toolkit for the Python programming language. It allows\
Python programmers to create programs with a robust, highly functional\
graphical user interface, simply and easily. It is implemented as a Python\
extension module (native code) that wraps the popular wxWindows cross\
platform GUI library, which is written in C++.

%package -n python-wxpython
Summary:        GUI toolkit for the Python programming language
%python_provide python-wxpython
Provides:       wxPython = %{version}-%{release}
Obsoletes:      wxPython < %{version}-%{release}

%description -n python-wxpython
wxPython is a GUI toolkit for the Python programming language. It allows\
Python programmers to create programs with a robust, highly functional\
graphical user interface, simply and easily. It is implemented as a Python\
extension module (native code) that wraps the popular wxWindows cross\
platform GUI library, which is written in C++.

%prep
%autosetup -n wxPython-%{version} -p1
sed -i -e '/^#!\//, 1d' wx/py/*.py
sed -i -e '/^#!\//, 1d' wx/tools/*.py
sed -i -e '/^#!\//, 1d' wx/py/tests/*.py
echo "# empty module" >> wx/lib/pubsub/core/itopicdefnprovider.py

%build
python3 build.py build

%install
python3 build.py install --destdir=%{buildroot} --extra_setup="-O1 --force"

%files -n python-wxpython
%license LICENSE.txt license/*.txt
%doc CHANGES.rst README.rst TODO.rst
%{_bindir}/helpviewer
%{_bindir}/img2png
%{_bindir}/img2py
%{_bindir}/img2xpm
%{_bindir}/pycrust
%{_bindir}/pyshell
%{_bindir}/pyslices
%{_bindir}/pyslicesshell
%{_bindir}/pywxrc
%{_bindir}/wxdemo
%{_bindir}/wxdocs
%{_bindir}/wxget
%{python3_sitearch}/wxPython-%{version}-py*.egg-info
%{python3_sitearch}/wx/

%changelog
* Tue Mar 24 2022 YukariChiba<i@0x7f.cc> - 4.1.1-1
- Upgrade version to python3

* Thu Mar 12 2020 gulining<gulining1@huawei.com> - 3.0.2.0-25
- Package init
