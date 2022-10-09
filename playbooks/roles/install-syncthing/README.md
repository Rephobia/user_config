Syncthing
--------------

Install syncthing package

Role Variables
--------------

| Variable                       | Default                  | Comments                                                                                         |
| `syncthing_user`               | -                        | user on whose behalf syncthing will run, user also must be able to write/read shared directories |
| `syncthing_host`               | ansible_host             | host for syncthing web-gui                                                                       |
| `syncthing_port`               | 8384                     | port for syncthing web-gui                                                                       |

Dependencies
------------

No specific dependencies

Example Playbook
----------------

```
- hosts: servers
  roles:
 - role: install-syncthing
      syncthing_user: "{{ nas_user }}"
```
