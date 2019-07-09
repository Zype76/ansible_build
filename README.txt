# ansible_build
Ansible playbooks for building a linux vm.
Wanted to make a polished playbook to showcase my Ansible competencies.

EXAMPLE SYNTAX TO CALL THE PLAYBOOK: 
ansible-playbook --ask-vault-pass -i hosts build.yml -k

This setup requires an external vars file, and I recommend that you encrypt it with ansible vault.

Steps for a vault file: 
To create the file: ansible-vault create external_vars.yml
File content example: 
# Secure variables
SSHDPORT:        #Insert ssh port number here
SERVICE_ACCOUNT: #Insert account name here
SERVER_HOSTNAME: #Insert desired hostname for server
HOST_IP:         #Insert desired ip for host here
HOST_SUBNET:     #Insert subnet mask for host here
HOST_GATEWAY:    #Insert gateway for host here
