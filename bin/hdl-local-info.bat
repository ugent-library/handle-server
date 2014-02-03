#!/bin/sh

PRG=$0
#progname=`basename $0`

# Resolve symlinks. See 4152645.
while [ -L "$PRG" ]; do
    ls=`/bin/ls -ld "$PRG"`
    link=`/usr/bin/expr "$ls" : '.*-> \(.*\)$'`
    if /usr/bin/expr "$link" : '/' > /dev/null; then
	PRG="$link"
    else
	PRG="`/usr/bin/dirname $PRG`/$link"
    fi
done

unset JAVA_HOME
unset CLASSPATH

# Get the full name of the directory where the Handle system is installed
HDLHOME=`dirname "$PRG"`
HDLHOME="${HDLHOME}/../"
#echo "HDLHOME is $HDLHOME"

# Load all of the .jar files in the lib directory into the classpath
CP=""
for jarfile in ${HDLHOME}lib/*.jar ; do
  CP=${CP}:${jarfile}
done
for jarfile in ${HDLHOME}lib/*/*.jar ; do
  CP=${CP}:${jarfile}
done
for jarfile in ${HDLHOME}lib/amazons3/*.jar ; do
  CP=${CP}:${jarfile}
done

# the last line of this script is added by the build process
# To developers:  make sure there is at least one blank line after
# this line

java -cp "%CP%" net.handle.apps.privatelhs.LocalInfoJPanel %* 