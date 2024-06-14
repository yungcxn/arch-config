import os

def send(path):
  os.system(f'swww img -f Nearest --transition-type center --transition-pos 0.5,0.5 --transition-fps 150 --transition-duration 2 --transition-step 255 {path}')
  #os.system(f'swww img -f Nearest --transition-type center --transition-pos 0.5,0.5 --transition-fps 150 --transition-duration 2 --transition-step 255 {path} -o \'DP-1\'')
  #os.system(f'swww img -f Nearest --transition-type center --transition-pos 0.5,0.5 --transition-fps 150 --transition-duration 2 --transition-step 255 {path} -o \'DP-2\'')

def create_config():
  with open('config.txt', 'w') as f:
    f.write('0')

def rewrite_config(inp):
  with open('config.txt', 'w') as f:
    f.write(str(inp))

def get_config_num():
  with open('config.txt', 'r') as f:
    return int(f.read())
  
folder_path = os.path.dirname(os.path.abspath(__file__))

try:
  current_num = get_config_num()
except:
  create_config()
  current_num = get_config_num()

current_num += 1
built_path = os.path.join(folder_path, f'{current_num}.png')
rewrite_config(current_num)

# does file exist?
if not os.path.exists(built_path):
  rewrite_config(0)
  current_num = 0
  built_path = os.path.join(folder_path, f'{current_num}.png')

send(built_path)

