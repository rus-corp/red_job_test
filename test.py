import unittest
from virtual_machine import Server, VM


class TestServerVM(unittest.TestCase):
  def setUp(self) -> None:
    self.server = Server()
    
  def test_connect_vm(self):
    vm = VM(254, 2 ,100)
    self.server.connect_vm(vm)
    self.assertEqual(len(self.server.virtual_machines), 1)
    
  def test_authenticate(self):
    vm = VM(254, 4, 150)
    self.server.authenticate(vm, 'login')
    self.assertEqual(len(self.server.authenticate_machines), 1)
    
  def test_update_vm_data(self):
    vm = VM(254, 4, 150)
    self.server.connect_vm(vm)
    self.server.update_vm_data(vm.id, ram=1000)
    updated_machine = self.server.virtual_machines[vm.id]
    self.assertEqual(updated_machine.ram, 1000)
    
    
    
if __name__ == '__main__':
  unittest.main()