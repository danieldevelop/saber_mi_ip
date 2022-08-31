import socket;

hostname = socket.gethostname();
ip = socket.gethostbyname(hostname);

print(f"\nEl nombre de tu ordenador es: {hostname}");
print(f"Tu dirección IP es: {ip}");

input("\n!!Presione enter para terminar el programa...");