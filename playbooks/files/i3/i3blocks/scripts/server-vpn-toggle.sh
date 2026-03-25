#!/bin/bash

SERVER_SSH="vyatka"
SERVICE="openvpn-client@er-vyatka"
SSH_CMD="/usr/bin/ssh -i ~/.ssh/id_ed25519_vyatka -o BatchMode=yes"

if [ "$BLOCK_BUTTON" = "1" ]; then
    STATUS=$($SSH_CMD $SERVER_SSH "sudo -n systemctl is-active $SERVICE")

    if [ "$STATUS" = "active" ]; then
        $SSH_CMD $SERVER_SSH "sudo -n systemctl stop $SERVICE"
    else
        $SSH_CMD $SERVER_SSH "sudo -n systemctl start $SERVICE"
    fi
fi

STATUS=$(ssh $SERVER_SSH "sudo -n systemctl is-active $SERVICE")

if [ "$STATUS" = "active" ]; then
    echo "VPN: ON"
else
    echo "VPN: OFF"
fi
