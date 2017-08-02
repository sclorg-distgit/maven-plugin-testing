%{?scl:%scl_package maven-plugin-testing}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-plugin-testing
Version:        3.3.0
Release:        9.1%{?dist}
Summary:        Maven Plugin Testing
License:        ASL 2.0
URL:            http://maven.apache.org/plugin-testing/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugin-testing/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

Patch0:         0001-Port-to-plexus-utils-3.0.21.patch
Patch1:         0002-Port-to-current-maven-artifact.patch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(commons-io:commons-io)
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-compat)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-model)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-invoker)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.wagon:wagon-file)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  %{?scl_prefix}mvn(org.easymock:easymock)

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
%setup -n %{pkg_name}-%{version} -q

%patch0 -p1
%patch1 -p1

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin

sed -i -e "s/MockControl/IMocksControl/g" maven-test-tools/src/main/java/org/apache/maven/shared/tools/easymock/MockManager.java

# needs network for some reason
rm maven-plugin-testing-tools/src/test/java/org/apache/maven/shared/test/plugin/ProjectToolTest.java

%mvn_alias : org.apache.maven.shared:

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{pkg_name}
%doc LICENSE NOTICE

%files harness -f .mfiles-%{pkg_name}-harness

%files tools -f .mfiles-%{pkg_name}-tools

%files -n %{?scl_prefix}maven-test-tools -f .mfiles-maven-test-tools

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 3.3.0-9.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Michael Simacek <msimacek@redhat.com> - 3.3.0-8
- Remove site-plugin from build

* Thu Jun 02 2016 Michael Simacek <msimacek@redhat.com> - 3.3.0-7
- Remove network using test

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Michael Simacek <msimacek@redhat.com> - 3.3.0-5
- Port to current maven-artifact

* Fri Oct 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.0-4
- Enable tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 27 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.0-2
- Port to plexus-utils 3.0.21
- Remove legacy maven-shared provides
- Regenerate build-requires

* Thu Feb  5 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.0-1
- Update to upstream version 3.3.0

* Thu Feb  5 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.0-2
- Add missing BR on maven-site-plugin
- Port to Maven 3.2.5

* Mon Jul 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.0-1
- Update to upstream version 3.2.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.0-3
- Remove BuildRequires on maven-surefire-provider-junit4

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.1.0-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Feb 24 2014 Michal Srb <msrb@redhat.com> - 3.1.0-1
- Update to upstream version 3.1.0

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-2
- Fix unowned directory

* Tue Jan 07 2014 Michal Srb <msrb@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Tue Aug 06 2013 Michal Srb <msrb@redhat.com> - 2.1-9
- Port to Maven 3.1.0 (Resolves: #988253, #991860)

* Thu Jul 25 2013 Alexander Kurtakov <akurtako@redhat.com> 2.1-8
- Build against easymock3.

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
- Change JPP.%{pkg_name}.%{pkg_name}-harness.pom to JPP.%{pkg_name}-%{pkg_name}-harness.pom

* Thu May 27 2010 Yong Yang <yyang@redhat.com> 1:1.2-2.3
- Remove epoch in Requires of maven-test-tools

* Wed May 12 2010 Alexander Kurtakov <akurtako@redhat.com> 1:1.2-2
- Fix line lengths and use macroses consistently.
- Add comment for the tests skip.
- Add missing requires and set permissions.

* Wed May 12 2010 Alexander Kurtakov <akurtako@redhat.com> 1:1.2-1
- Initial package.
