import asyncio


from virtual_machine import Server, VM



HOST = '127.0.0.1'
PORT = 9999



async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
  auth_data = await reader.read(1024)
  auth_msg = auth_data.decode()
  
  addr, port = writer.get_extra_info('peername')
  print(f'Получен запрос на подключение от {addr}: {port} - {auth_data}')
  client_info = auth_msg.strip().split(',')
  client_data = {
      'ram': client_info[0],
      'cpu': client_info[1],
      'disk_size': client_info[2],
  }
  vm = VM(*client_data)
  try:
    while True:
      writer.write(auth_data)
      await writer.drain()
      data = await reader.read(1024)
      msg = data.decode()
      if msg.strip() == 'disconnect':
        print(f'Получен запрос на отключение от {addr}: {port}')
        break
      if msg.strip() == 'login':
        status = sv.authenticate(vm, msg.strip())
        if status:
          writer.write('OK'.encode())
          await writer.drain()
          print(f'Client {vm.id} login')
        else:
          writer.write('Authentication failed'.encode())
          await writer.drain()
      elif msg.strip() == 'connect':
        sv.connect_vm(vm)
        writer.write('You are connected'.encode())
        print(f'Client {vm.id} connected')
        await writer.drain()
      elif msg.strip() == 'add_to_db':
        data_id = sv.add_client_to_db(vm)
        writer.write('You are added to db'.encode())
        print(f'Client {vm.id} added to db for number {data_id}')
        await writer.drain()
      elif msg.strip() == 'update_vm_data':
        sv.update_vm_data(vm.id, cpu=4)
        writer.write('You are updated'.encode())
        print(f'Client {vm.id} updated')
        await writer.drain()
      elif msg.strip() == 'get_connect_vm':
        machines = sv.get_connect_vm()
        writer.write('OK'.encode())
        print(f'connect machines {machines}')
        await writer.drain()
      elif msg.strip() == 'history':
        machines_history = sv.get_history_vm()
        writer.write('Ok'.encode())
        print(f'machines_history {machines_history}')
        await writer.drain()
  except asyncio.CancelledError:
    pass
  finally:     
    writer.close()
    await writer.wait_closed()
    
  
async def run_server():
  server = await asyncio.start_server(handle_client, HOST, PORT)
  async with server:
    await server.serve_forever()
    
if __name__ == '__main__':
  sv = Server()
  loop = asyncio.new_event_loop()
  loop.run_until_complete(run_server())
  
  