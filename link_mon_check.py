# from pandevice import panorama
from pawn import keys
from pawn import Panorama

pan_vm = Panorama('10.46.164.193')

panorama_connected_fws = pan_vm.all_connected_fws()

print(panorama_connected_fws)
