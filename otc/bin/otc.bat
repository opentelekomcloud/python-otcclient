@ECHO OFF
rem set JAVA_HOME=../jre
java -cp CLASSPATH -cp "../lib/otc-0.0.1-SNAPSHOT.jar;../lib/*" com.tsystems.otc.OtcMain %*
