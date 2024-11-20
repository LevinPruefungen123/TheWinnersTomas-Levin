from opcua import Client
from opcua import ua

# Verbindung zum OPC UA Server herstellen
client = Client("opc.tcp://192.168.100.13:2035/")
client.connect()

# Zugriff auf die Methoden-Objekte
jump_to_method = client.get_node("ns=0;i=20002")  # JumpTo Methode
get_charge_percent_method = client.get_node("ns=0;i=20005")  # GetChargePercent Methode

# Überprüfen, ob der Knoten eine Methode ist
if jump_to_method.get_node_class() == ua.NodeClass.Method:
    print(f"JumpTo ist eine Methode: {jump_to_method}")
else:
    print("JumpTo ist keine Methode!")

if get_charge_percent_method.get_node_class() == ua.NodeClass.Method:
    print(f"GetChargePercent ist eine Methode: {get_charge_percent_method}")
else:
    print("GetChargePercent ist keine Methode!")

# Argumente für JumpTo korrekt definieren
input_args = [
    ua.Variant(10, ua.VariantType.Int32),  # Beispielwert für x
    ua.Variant(20, ua.VariantType.Int32)   # Beispielwert für y
]

# Versuchen Sie, die Methoden mit den richtigen Eingabewerten aufzurufen
try:
    result_jump_to = jump_to_method.call_method('0:JumpTo', *input_args)  # Aufruf der Methode mit den Eingabewerten
    print(f"Ergebnis des JumpTo: {result_jump_to}")
except Exception as e:
    print(f"Fehler bei JumpTo-Methode: {e}")

# Abrufen des Ladelevels für GetChargePercent
try:
    result_charge_percent = get_charge_percent_method.call_method('0:GetChargePercent')  # Aufruf der Methode ohne Argumente
    print(f"Ladelevel: {result_charge_percent}")
except Exception as e:
    print(f"Fehler bei GetChargePercent-Methode: {e}")

# Verbindung zum Server trennen
client.disconnect()
