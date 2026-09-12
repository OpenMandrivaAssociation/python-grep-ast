Name:		python-grep-ast
Version:	0.9.0
Release:	1
Summary:	Grep a source file via its syntax tree
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/paul-gauthier/grep-ast
Source0:	https://files.pythonhosted.org/packages/source/g/grep-ast/grep_ast-%{version}.tar.gz
Patch0:		0001-use-individual-tree-sitter-langs.patch
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(pathspec)
Requires:	python%{pyver}dist(tree-sitter)
Requires:	python%{pyver}dist(tree-sitter-python)
Requires:	python%{pyver}dist(tree-sitter-javascript)
Requires:	python%{pyver}dist(tree-sitter-typescript)
Requires:	python%{pyver}dist(tree-sitter-rust)
Requires:	python%{pyver}dist(tree-sitter-go)
Requires:	python%{pyver}dist(tree-sitter-bash)
Requires:	python%{pyver}dist(tree-sitter-json)
Requires:	python%{pyver}dist(tree-sitter-html)
Requires:	python%{pyver}dist(tree-sitter-c)
Requires:	python%{pyver}dist(tree-sitter-cpp)
Requires:	python%{pyver}dist(tree-sitter-java)
Requires:	python%{pyver}dist(tree-sitter-css)
Requires:	python%{pyver}dist(tree-sitter-yaml)
Requires:	python%{pyver}dist(tree-sitter-markdown)

%description
grep-ast walks a file's Tree-sitter AST. Aider uses it for the
repository map. This build uses individual compiled grammars
instead of the prebuilt tree-sitter-language-pack wheels.

%prep
%autosetup -p1 -n grep_ast-%{version}

%build

%install
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.
for cmd in grep-ast gast; do
	if [ -f %{buildroot}%{_bindir}/$cmd ]; then
		sed -i '1s|^#!/usr/bin/env python3|#!/usr/bin/python|' \
			%{buildroot}%{_bindir}/$cmd
		sed -i '1s|^#!/usr/bin/python3|#!/usr/bin/python|' \
			%{buildroot}%{_bindir}/$cmd
	fi
done

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/grep-ast
%{_bindir}/gast
%{py_sitedir}/grep_ast
%{py_sitedir}/grep_ast-*.*-info
