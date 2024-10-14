#!/usr/bin/python3

from libs.hbproxmox import HandelProxmox

def main():
  node = "console-fpt-pceph-nvme.vndata.vn"
  user = "<Username>@pve"
  passwd = "<Password>"

  proxmox = HandelProxmox(node, user, passwd)
  proxmox.start_vm("<vm_name>")

if __name__ == '__main__':
  main()
