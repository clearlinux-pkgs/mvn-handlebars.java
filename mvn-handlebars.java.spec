#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-handlebars.java
Version  : 4.0.7
Release  : 1
URL      : https://github.com/jknack/handlebars.java/archive/v4.0.7.tar.gz
Source0  : https://github.com/jknack/handlebars.java/archive/v4.0.7.tar.gz
Source1  : https://repo1.maven.org/maven2/com/github/jknack/handlebars-helpers/4.0.7/handlebars-helpers-4.0.7.jar
Source2  : https://repo1.maven.org/maven2/com/github/jknack/handlebars-helpers/4.0.7/handlebars-helpers-4.0.7.pom
Source3  : https://repo1.maven.org/maven2/com/github/jknack/handlebars.java/4.0.7/handlebars.java-4.0.7.pom
Source4  : https://repo1.maven.org/maven2/com/github/jknack/handlebars/4.0.7/handlebars-4.0.7.jar
Source5  : https://repo1.maven.org/maven2/com/github/jknack/handlebars/4.0.7/handlebars-4.0.7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-handlebars.java-data = %{version}-%{release}
Requires: mvn-handlebars.java-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
[![Build Status](https://secure.travis-ci.org/jknack/handlebars.java.png?branch=master)](https://travis-ci.org/jknack/handlebars.java)
[![Coverage Status](https://coveralls.io/repos/jknack/handlebars.java/badge.png)](https://coveralls.io/r/jknack/handlebars.java)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.github.jknack/handlebars/badge.svg)](https://maven-badges.herokuapp.com/maven-central/com.github.jknack/handlebars)
[![javadoc](https://javadoc.io/badge/com.github.jknack/handlebars.svg)](https://javadoc.io/doc/com.github.jknack/handlebars)

%package data
Summary: data components for the mvn-handlebars.java package.
Group: Data

%description data
data components for the mvn-handlebars.java package.


%package license
Summary: license components for the mvn-handlebars.java package.
Group: Default

%description license
license components for the mvn-handlebars.java package.


%prep
%setup -q -n handlebars.java-4.0.7

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-handlebars.java
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-handlebars.java/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/jknack/handlebars-helpers/4.0.7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/github/jknack/handlebars-helpers/4.0.7/handlebars-helpers-4.0.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/jknack/handlebars-helpers/4.0.7
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/github/jknack/handlebars-helpers/4.0.7/handlebars-helpers-4.0.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/jknack/handlebars.java/4.0.7
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/github/jknack/handlebars.java/4.0.7/handlebars.java-4.0.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/jknack/handlebars/4.0.7
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/github/jknack/handlebars/4.0.7/handlebars-4.0.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/jknack/handlebars/4.0.7
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/github/jknack/handlebars/4.0.7/handlebars-4.0.7.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/github/jknack/handlebars-helpers/4.0.7/handlebars-helpers-4.0.7.jar
/usr/share/java/.m2/repository/com/github/jknack/handlebars-helpers/4.0.7/handlebars-helpers-4.0.7.pom
/usr/share/java/.m2/repository/com/github/jknack/handlebars.java/4.0.7/handlebars.java-4.0.7.pom
/usr/share/java/.m2/repository/com/github/jknack/handlebars/4.0.7/handlebars-4.0.7.jar
/usr/share/java/.m2/repository/com/github/jknack/handlebars/4.0.7/handlebars-4.0.7.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-handlebars.java/LICENSE
