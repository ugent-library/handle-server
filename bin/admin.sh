#!/bin/bash

JAVA="/usr/bin/java"
PROJ_DIR="/usr/local/handle"

${JAVA} -cp ${PROJ_DIR}/bin/handle.jar net.handle.apps.gui.hadmin.HandleTool
