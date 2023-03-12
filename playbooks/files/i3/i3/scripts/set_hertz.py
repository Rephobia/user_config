#!/usr/bin/env python3

import argparse
import subprocess

def get_args() -> argparse:
    """
    returns user inputs object, it has two fields mode and rate
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', required=True, type=str, help='xrandr mode wrapper, resolution')
    parser.add_argument('--rate', required=True, type=str, help='xrandr rate wrapper, hertz')
    args = parser.parse_args()
    return args

def get_connected_ports() -> map:
    """
    gets map of connected ports
    """
    ports = subprocess.check_output('xrandr').decode().split('\n')

    connected_ports = []
    for port in ports:
        for port_entity in port.split():
            if port_entity == 'connected':
                connected_ports.append(port)
    # xrandr output string has format PORT STATUS TYPE RESOLUTION (POSITION) SIZE, e.q.
    # DP-0 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 527mm x 296mm
    # first entity is name
    return map(lambda x: x.split()[0], connected_ports)

def set_mode_and_rate(ports: map, mode: str, rate: str) -> None:
    """
    sets mode and rate to passed ports
    """
    for port in ports:
        subprocess.run(['xrandr', '--output', port, '--mode', mode, '--rate', rate])

if __name__ == '__main__':
    args = get_args()
    ports = get_connected_ports()
    set_mode_and_rate(ports, args.mode, args.rate)
