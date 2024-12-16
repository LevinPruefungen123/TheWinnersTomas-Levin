from asyncua import Client, ua
import asyncio

async def main(x1, y1):
    async with Client(url='opc.tcp://192.168.100.13:2035/') as client:

        node = client.get_node('i=20001')
        method_id = client.get_node('i=20002')  
        x = ua.Variant(x1, ua.VariantType.Int64)
        y = ua.Variant(y1, ua.VariantType.Int64)
        result = await node.call_method(method_id, x, y)
        print(result)

if __name__ == '__main__':
    # Main Methode ausführen
    asyncio.run(main())