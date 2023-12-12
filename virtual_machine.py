import asyncio
import sqlite3




class Disk:
  disk_id = 1
  disks = []
  def __init__(self, size, vm=None) -> None:
    self.id = Disk.disk_id 
    Disk.disk_id += 1
    self.size = size
    self.vm = vm
    Disk.disks.append(self)
    
  def get_disk_info(self):
    return {
      'id': self.id,
      'size': self.size,
    }
    

class VM:
  vm_id = 1
  def __init__(self, ram, cpu, disk_size) -> None:
    self.id = VM.vm_id
    VM.vm_id += 1
    self.ram = ram
    self.cpu = cpu
    self.disk = Disk(disk_size, vm=self)
    self.authorized = False


class Server:
  def __init__(self) -> None:
    self.authenticate_machines = {}
    self.virtual_machines = {}
    self.all_connect_machines_history = {}
    self.db_connection = sqlite3.connect('server.db')
    self.initialize_db()
    
  def connect_vm(self, vm):
    self.virtual_machines[vm.id] = vm
    self.all_connect_machines_history[vm.id] = vm

  def disconect(self, vm):
    machine = self.virtual_machines.pop(vm.id, False)
    if machine:
      machine.authorized = False
      
  def authenticate(self, vm, password):
    if password == 'login':
      self.authenticate_machines[vm.id] = vm
      vm.authorized = True
      self.all_connect_machines_history[vm.id] = vm
      return True
    return False

  def _get_machiine_data(self, data_dict):
    machines = []
    for machine in data_dict.values():
      machines.append({
        "id": machine.id,
        "ram": machine.ram,
        'cpu': machine.cpu,
        'disk': machine.disk.get_disk_info()
      })
    return machines
  
  def update_vm_data(self, vm_id, **kwargs):
    if vm_id in self.virtual_machines:
      vm = self.virtual_machines.get(vm_id)
      
      for key, value in kwargs.items():
        setattr(vm, key, value)
    
  def get_connect_vm(self):
    return self._get_machiine_data(self.virtual_machines)
  
  def get_authenticate_vm(self):
    return self._get_machiine_data(self.authenticate_machines)
    
  def get_history_vm(self):
    return self._get_machiine_data(self.all_connect_machines_history)
    
  def initialize_db(self):
    with self.db_connection:
      self.db_connection.execute("""
                                 CREATE TABLE IF NOT EXISTS server (
                                   id INTEGER PRIMARY KEY,
                                   ram INTEGER,
                                   cpu INTEGER,
                                   disk_id INTEGER,
                                   disk_size INTEGER)""")

  def add_client_to_db(self, vm):
    with self.db_connection:
      cursor = self.db_connection.cursor()
      cursor.execute("""
                     INSERT INTO server VALUES(
                       ?, ?, ?, ?, ?)""", (vm.id, vm.ram, vm.cpu, vm.disk.id, vm.disk.size))
      vm_id = cursor.lastrowid
      return vm_id
      
      
      
      
# if __name__ == '__main__':
#   sv = Server()
#   vm1 = VM(256, 2, 100)
#   vm2 = VM(512, 2, 40)
#   vm3 = VM(128, 1, 30)
  

#   sv.authenticate(vm1, 'login')
#   sv.connect_vm(vm1)
#   sv.connect_vm(vm2)
#   sv.connect_vm(vm3)
#   print(sv.get_connect_vm())
#   print()
#   sv.disconect(vm1)
#   print()
#   print(sv.get_authenticate_vm())
#   print()
#   print(sv.get_history_vm())
#   print(sv.add_client_to_db(vm2))
  # print(sv.authenticate_machines)
  # print(sv.virtual_machines)

















# class Server:
#   def __init__(self) -> None:
#     self.authenticate_machines = {}
#     self.virtual_machines = {}
#     self.all_connect_machines = []
    
#   def authenticate(self, vm, password):
#     if password == 'password':
#       self.authenticate_machines[vm.id] = vm
#       vm.authorized = True
#       return True
#     return False
    
  
#   def connect(self, vm):
#     self.virtual_machines[vm.id] = vm
#     self.all_connect_machines.append(vm)
    
#   def disconect(self, vm):
#     machine = self.virtual_machines.pop(machine.id, False)
#     if machine:
#       machine.authorized = False
  
#   def all_connect_machine(self):
#     vm_list = []
#     for vm, id in self.virtual_machines.items():
#       vm_list.append({
#         id: vm
#       })
#     return vm_list
  
#   def all_authenticate_machine(self):
#     vm_list = []
#     for vm, id in self.authenticate_machines.items():
#       vm_list.append({
#         id: vm
#       })
#     return vm_list
    
#   def get_all_old_machines(self):
#     return self.all_connect_machines
  
  
  
    
  # def add_to_db(self):
  #   pass

# class HardDisk:
#   def __init__(self, id, disk_size) -> None:
#     self.id = id
#     self.disk_size = disk_size
#     self.attached_vm = []
    
#   def attachvm(self, vm):
#     self.attached_vm.append(vm)


# class VirtualMachine:
#   def __init__(self, id, ram, cpu, disk_size, disk_id) -> None:
#     self.id = id
#     self.ram = ram
#     self.cpu = cpu
#     self.disk_size = disk_size
#     self.disk_id = disk_id
#     self.authorized = False
    
    
    
    








