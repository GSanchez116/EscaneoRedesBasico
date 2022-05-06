print("\n|----------------------------------------------------------------------|")
print("|                       ESCANEO DE PUERTOS                             |")
print("|----------------------------------------------------------------------|")

# -*- encoding: utf-8 -*-
# !/usr/bin/python3


import socket


def scanHost(ip, startPort, endPort):
    """ Starts a TCP scan on a given IP address """

    print('[*] Starting TCP port scan on host %s' % ip)

    tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on host %s complete' % ip)


def scanRange(network, startPort, endPort):
    """ Starts a TCP scan on a given IP address range """

    print('[*] Starting TCP port scan on network %s.0' % network)

    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on network %s.0 complete' % network)


def tcp_scan(ip, startPort, endPort):
    """ Creates a TCP socket and attempts to connect via supplied ports """

    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            if not tcp.connect_ex((ip, port)):
                print('[+] %s:%d/TCP Open' % (ip, port))
                tcp.close()

        except Exception:
            pass


if __name__ == '__main__':

    def menu():
        print("[1] Escaneo de un host")
        print("[2] Escaneo de un rango de red")
        print("[3] Salir")


    menu()
    Escaneo = input("Introduzca la opcion que desea utilizar: ")

    while Escaneo != '3':

        if Escaneo == '1':
            network = input("Introduzca la direccion ip: ")
            startPort = int(input("Introduzca el puerto inicial: "))
            endPort = int(input("Introduzca el puerto final: "))
            scanHost(network, startPort, endPort)

        elif Escaneo == '2':
            network = input("Introduzca la direccion ip: ")
            startPort = int(input("Introduzca el puerto inicial: "))
            endPort = int(input("Introduzca el puerto final: "))
            scanRange(network, startPort, endPort)

        elif Escaneo == '3':
            print('Hasta luego')

        else:
            print("la opción no es válida")

        print()
        menu()
        Escaneo = input("Introduzca la opción que desea utilizar: ")