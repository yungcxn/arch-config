#!/bin/bash
# Dispatch command to kill the active window
hyprctl dispatch killactive
sleep 0.01

# Capture the current workspace
current_workspace=$(hyprctl activeworkspace)

# Extract the workspace ID
output="${current_workspace#*ID }"
n="${output:0:1}"

# Loop while there are no windows and the workspace ID is not "1"
while [ ! -z "$(hyprctl activeworkspace | grep 'windows: 0')" ] && [ "${n}" != "1" ]; do
    hyprctl dispatch workspace m-1
    sleep 0.01
    current_workspace=$(hyprctl activeworkspace)
    # Extract the workspace ID
    output="${current_workspace#*ID }"
    n="${output:0:1}"
done
