%global pkg_name maven-plugin-testing
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.1
Release:        11.12%{?dist}
Summary:        Maven Plugin Testing
License:        ASL 2.0
URL:            http://maven.apache.org/plugin-testing/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugin-testing/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}easymock2
BuildRequires: %{?scl_prefix_java_common}junit
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}maven-resources-plugin
BuildRequires: %{?scl_prefix}maven-source-plugin
BuildRequires: %{?scl_prefix}plexus-containers-component-metadata
BuildRequires: %{?scl_prefix}maven-javadoc-plugin
BuildRequires: %{?scl_prefix}maven-doxia-sitetools
BuildRequires: %{?scl_prefix}maven-reporting-impl
#BuildRequires: %{?scl_prefix}maven-test-tools

%description
The Maven Plugin Testing contains the necessary modules
to be able to test Maven Plugins.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%package harness
Summary: Maven Plugin Testing Mechanism

%description harness
The Maven Plugin Testing Harness provides mechanisms to manage tests on Mojo.

%package tools
Summary: Maven Plugin Testing Tools

%description tools
A set of useful tools to help the Maven Plugin testing.

%package -n %{?scl_prefix}maven-test-tools
Summary: Maven Testing Tool

%description -n %{?scl_prefix}maven-test-tools
Framework to test Maven Plugins with Easymock objects.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_alias : org.apache.maven.shared:
# Tests are skipped due to some test failures most probably caused by issues 
# with our plexus container
%mvn_build -f -s
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles-%{pkg_name}
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE NOTICE
%files harness -f .mfiles-%{pkg_name}-harness
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files tools -f .mfiles-%{pkg_name}-tools
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files -n %{?scl_prefix}maven-test-tools -f .mfiles-maven-test-tools
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jan 15 2015 Michael Simacek <msimacek@redhat.com> - 2.1-11.12
- Add common dirs to subpackages

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-11.11
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.1-11.10
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.1-11.9
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-11.8
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-11.7
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-11.6
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-11.5
- Rebuild to fix incorrect auto-requires

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 2.1-11.4
- SCL-ize subpackage's name

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-11.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-11.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-11.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.1-11
- Mass rebuild 2013-12-27

* Tue Oct 08 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-10
- Remove not needed workaround for 1002873 
- Resolves: rhbz#1002873

* Mon Sep 16 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-9
- Workaround installation problem with easymock2 compat package
- Related: rhbz#1002873

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-8
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 22 2013 Michal Srb <msrb@redhat.com> - 2.1-7
- Another rebuild (Fix artifactId=None issue)

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-6
- Rebuild

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-5
- Install missing license files
- Build with xmvn
- Resolves: rhbz#920258

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-2
- Fix easymock requires

* Mon Jan 07 2013 Tomas Radej <tradej@redhat.com> - 2.1-1
- Updated to latest upstream version
- Cleanup - removed patches, old files etc.
- Added requires to subpackages

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Jaromir Capik <jcapik@redhat.com> 2.0-2.alpha1
- Structuring mess cleanup (depmap fragments split, removing jar duplicities)

* Wed Nov 09 2011 Jaromir Capik <jcapik@redhat.com> 2.0-1.alpha1
- Update to 2.0-alpha1
- Spec file changes according to the latest guidelines

* Thu Feb 10 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2-9
- Fix building.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 20 2010 Yong Yang <yyang@redhat.com> 1.1-7
- Build with plexus-containers 1.5.4

* Mon May 31 2010 Alexander Kurtakov <akurtako@redhat.com> 1.2-6
- Proper obsolete for maven-shared-test-tools.

* Mon May 31 2010 Alexander Kurtakov <akurtako@redhat.com> 1.2-5
- One more item to the depmap.

* Mon May 31 2010 Alexander Kurtakov <akurtako@redhat.com> 1.2-4
- Add depmap to fix build.

* Sat May 29 2010 Alexander Kurtakov <akurtako@redhat.com> 1.2-3
- Obsolete maven-shared-test-tools.

* Thu May 27 2010 Yong Yang <yyang@redhat.com> 1:1.2-2.8
- Fix parent pom install

* Thu May 27 2010 Yong Yang <yyang@redhat.com> 1:1.2-2.7
- Fix installed pom.xml source path

* Thu May 27 2010 Yong Yang <yyang@redhat.com> 1:1.2-2.6
- Add more maven depmap for maven-test-tools and maven-plugin-testing-tools for backward compatibility 

* Thu May 27 2010 Yong Yang <yyang@redhat.com> 1:1.2-2.5
- Fix maven-plugin-testing-tools pom name

* Thu May 27 2010 Yong Yang <yyang@redhat.com> 1:1.2-2.4
- Change JPP.%{name}.%{name}-harness.pom to JPP.%{name}-%{name}-harness.pom

* Thu May 27 2010 Yong Yang <yyang@redhat.com> 1:1.2-2.3
- Remove epoch in Requires of maven-test-tools

* Wed May 12 2010 Alexander Kurtakov <akurtako@redhat.com> 1:1.2-2
- Fix line lengths and use macroses consistently.
- Add comment for the tests skip.
- Add missing requires and set permissions.

* Wed May 12 2010 Alexander Kurtakov <akurtako@redhat.com> 1:1.2-1
- Initial package.
