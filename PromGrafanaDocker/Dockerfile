FROM openjdk:8-jdk-alpine
WORKDIR /app
ARG APP_JAR_FILE
ARG JMX_PORT
ARG JMX_CONFIG_FILE
ARG JMX_JAR_FILE
ENV JMX_METRIC_PORT=${JMX_PORT}
COPY ${APP_JAR_FILE} app.jar
COPY ${JMX_CONFIG_FILE} config.yml
COPY ${JMX_JAR_FILE} jmx_jar.jar
ENTRYPOINT java -javaagent:./jmx_jar.jar=$JMX_METRIC_PORT:config.yml -jar app.jar