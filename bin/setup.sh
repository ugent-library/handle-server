#!/bin/bash

JAVA="/usr/bin/java"
PROJ_DIR="/usr/local/handle"
SERVER="svr_1"

${JAVA} -cp ${PROJ_DIR}/bin/handle.jar net.handle.server.SimpleSetup ${PROJ_DIR}/${SERVER}
