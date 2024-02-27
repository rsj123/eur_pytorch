%global _empty_manifest_terminate_build 0
Name:		pytorch
Version:	2.0.1
Release:	2
Summary:	Tensors and Dynamic neural networks in Python with strong GPU acceleration
License:	BSD-3
URL:		https://pytorch.org/
Source0:	https://github.com/pytorch/pytorch/releases/download/v2.0.1/pytorch-v2.0.1.tar.gz

BuildRequires:  g++
Requires:	python3-future
Requires:	python3-numpy

%description
PyTorch is a Python package that provides two high-level features:
- Tensor computation (like NumPy) with strong GPU acceleration
- Deep neural networks built on a tape-based autograd system
You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend PyTorch when needed.

%package -n python3-pytorch
Summary:	Tensors and Dynamic neural networks in Python with strong GPU acceleration
Provides:	python-torch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
BuildRequires:	python3-pbr
BuildRequires:	python3-pip
BuildRequires:	python3-wheel
BuildRequires:	python3-hatchling

BuildRequires:	python3-astunparse
BuildRequires:	python3-numpy
BuildRequires:	python3-pyyaml
BuildRequires:	cmake
BuildRequires:	python3-typing-extensions
BuildRequires:	python3-requests

%description -n python3-pytorch
PyTorch is a Python package that provides two high-level features:
- Tensor computation (like NumPy) with strong GPU acceleration
- Deep neural networks built on a tape-based autograd system
You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend PyTorch when needed.

%package help
Summary:	Development documents and examples for torch
Provides:	python3-pytorch-doc
%description help
PyTorch is a Python package that provides two high-level features:
- Tensor computation (like NumPy) with strong GPU acceleration
- Deep neural networks built on a tape-based autograd system
You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend PyTorch when needed.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
export CFLAGS+=" -Wno-error=maybe-uninitialized -Wno-error=uninitialized -Wno-error=restrict -fPIC"
export CXXFLAGS+=" -Wno-error=maybe-uninitialized -Wno-error=uninitialized -Wno-error=restrict -fPIC"
%pyproject_build

%install
%pyproject_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/doclist.lst .

%files -n python3-pytorch
%doc *.md
%license LICENSE
%{_bindir}/convert-caffe2-to-onnx
%{_bindir}/convert-onnx-to-caffe2
%{_bindir}/torchrun
%{python3_sitearch}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Aug 17 2023 Dongxing Wang <dxwangk@isoftstone.com> - 2.0.1-2
- Fix the EulerMaker failure for verion 2.0.1

* Mon Jul 24 2023 Dongxing Wang <dxwangk@isoftstone.com> - 2.0.1-1
- upgrade to 2.0.1

* Thu Feb 16 2023 Dongxing Wang <dxwangk@isoftstone.com> - 1.11.0-2
- fixes: error: the CXX 11 compiler error (linux.cc flexible array member not at end of struct)

* Mon Jun 13 2022 Zhipeng Xie <xiezhipeng1@huawei.com> - 1.11.0-1
- upgrade to 1.11.0

* Mon Jun 28 2021 wulei <wulei80@huawei.com> - 1.6.0-3
- fixes: error: the CXX compiler identification is unknown

* Thu Feb 4 2021 Zhipeng Xie<xiezhipeng1@huawei.com> - 1.6.0-2
- disable SVE to fix compile error in gcc 9

* Sun Sep 27 2020 Zhipeng Xie<xiezhipeng1@huawei.com> - 1.6.0-1
- Package init
