#!/bin/bash

# Abre um terminal e roda o receptor
gnome-terminal -- bash -c "python3 receptor.py; exec bash"

# Aguarda 1 segundo para dar tempo de abrir o terminal anterior
sleep 1

# Abre outro terminal e roda o transmissor
gnome-terminal -- bash -c "python3 transmissor.py; exec bash"
