import os
import pathlib as Path
import random 
import shutil
import numpy as np

def modify(dir, type):
    type_value = {
        'train': '0_',
        'valid': '1_',
        'test': '2_'
    }
    print(type_value[type])

    end_val = []
    rgb_dir = os.path.join(dir, 'rgb')
    pose_dir = os.path.join(dir, 'pose')

    for stt, i in enumerate(sorted(os.listdir(rgb_dir))):
        a = i.split('.')
        a[0] = int(a[0]) - 1
        rd= random.randrange(0, 1000)
        if rd not in end_val:
            end_val.append(rd)
        else:
            while True:
                rd = random.randrange(0, 1000)
                if(rd not in end_val):
                    end_val.append(rd)
                    break
        b = type_value[type] + str(a[0]).zfill(5) + '_' + str(rd).zfill(8) + '.' + a[1]
        os.rename(os.path.join(rgb_dir, i),  os.path.join(rgb_dir, b))
    print("Changed RGB_" + type)
        
    for stt, i in enumerate(sorted(os.listdir(pose_dir))):
        with open(os.path.join(pose_dir, i), "r") as f_r:
            list_value = str(f_r.read()).split(' ')
            space = ' '
            line_0 = list_value[0] + space + list_value[1] + space + list_value[2] + space +list_value[3] +"\n"
            line_1 = list_value[4] + space + list_value[5] + space + list_value[6] + space +list_value[7] +"\n"
            line_2 = list_value[8] + space + list_value[9] + space + list_value[10] + space +list_value[11] +"\n"
            line_3 = list_value[12] + space + list_value[13] + space + list_value[14] + space +list_value[15]
            line = line_0 + line_1 + line_2 + line_3
        with open(os.path.join(pose_dir, i),"w") as f_w:
            f_w.write(line)
            f_w.close

        a = i.split('.')
        a[0] = int(a[0]) - 1
        name_pose = type_value[type] + str(a[0]).zfill(5) + '_' +str(end_val[stt]).zfill(8) + '.' + a[1]
        # print(name_pose)
        os.rename(os.path.join(pose_dir, i), os.path.join(pose_dir, name_pose))
    print("Changed pose_" + type)
    

if __name__ == '__main__':
    root_dir = 'C:\\Users\\STB\\Downloads\\nerfpp\\tat_intermediate_Playground' 
    
    train_dir = os.path.join(root_dir, 'train')
    valid_dir = os.path.join(root_dir, 'validation')
    test_dir = os.path.join(root_dir, 'test')


    modify(train_dir, 'train')
    modify(valid_dir, 'valid')
    modify(test_dir, 'test')
    print('------------------')
    print('Changed completely')



