import asyncio

HOST = '127.0.0.1'
PORT = 9999


async def run_client():
  try:
    reader, writer = await asyncio.open_connection(HOST, PORT)
    writer.write(b'250,50,40')
    await writer.drain()
    question = ['connect', 'login', 'update_vm_data', 'add_to_db','get_connect_vm',
                'history', 'disconnect']
    messages = len(question)
    
    for quest in question:
      await asyncio.sleep(2)
      writer.write(quest.encode())
      await writer.drain()
      data = await reader.read(1024)
      print(f'recived data: {data.decode()!r}')
  finally:
    writer.write(b'disconncet')
    await writer.drain()
    
    data = await reader.read(1024)
    print(f'finall {data.decode()!r}')
    writer.close
    await writer.wait_closed()
    
    
async def main():
  clients = [run_client(i) for i in range(1, 6)]
  await asyncio.gather(clients)
    
  
if __name__ == '__main__':
  asyncio.run(run_client())