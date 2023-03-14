
from tqdm import tqdm
import os
import pathlib as Path
import random 
import shutil
import argparse

def modify(dir, type, out_rgb_dir, out_pose_dir):
	type_value = {
		'train': '0_',
		'validation': '1_',
		'test': '2_'
	}
	print(type_value[type])

	end_val = []
	rgb_dir = os.path.join(dir, 'rgb')
	pose_dir = os.path.join(dir, 'pose')

	for stt, i in enumerate(tqdm(sorted(os.listdir(rgb_dir)))):
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
		os.rename(os.path.join(rgb_dir, i),  os.path.join(out_rgb_dir, b))
	print("Changed RGB_" + type)
	
	shutil.copytree(rgb_dir, out_rgb_dir, dirs_exist_ok=True)	
	
	for stt, i in enumerate(tqdm(sorted(os.listdir(pose_dir)))):
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
		os.rename(os.path.join(pose_dir, i), os.path.join(pose_dir, name_pose))

	shutil.copytree(pose_dir, out_pose_dir, dirs_exist_ok=True)
	print("Changed pose_" + type)
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('data_dir', type = str, help = 'dir to data folder that contain test/, train/, valid/')
	#parser.add_argument('--output_dir', type = str, help = 'dir contain pose/, rgb/, intrinsics.txt')
	output_dir = "../"
	opt = parser.parse_args()

	if os.path.exists(os.path.join(opt.data_dir, 'train')):
		train_dir = (os.path.join(opt.data_dir, 'train'))
		print(os.path.abspath(train_dir))
	if os.path.exists(os.path.join(opt.data_dir, 'validation')):
		validation_dir = os.path.join(opt.data_dir, 'validation')
		print(os.path.abspath(validation_dir))
	if os.path.exists(os.path.join(opt.data_dir, 'test')):
		test_dir = os.path.join(opt.data_dir, 'test')
		print(os.path.abspath(test_dir))
	output_dir = os.path.join(os.path.abspath(output_dir), 'npp2tat')  #name folder
	if not os.path.exists(output_dir):
		os.mkdir(output_dir)
		print(output_dir)
		print("Created output dir")
	output_temp_dir = os.path.join(output_dir, "temp")
	shutil.copytree(opt.data_dir, output_temp_dir, dirs_exist_ok= True)

	rgb_dir = os.path.join(output_dir, 'rgb')
	pose_dir = os.path.join(output_dir, 'pose')
	intrinsics_dir = os.path.join(output_dir, 'intrinsics.txt')
	if not os.path.exists(rgb_dir):
		os.mkdir(rgb_dir)
		print("Created rgb dir")
	if not os.path.exists(pose_dir):
		os.mkdir(pose_dir)
		print("Created pose dir")
	

	train_dir = os.path.abspath(os.path.join(opt.data_dir, 'train'))
	valid_dir = os.path.abspath(os.path.join(opt.data_dir, 'validation'))
	test_dir = os.path.abspath(os.path.join(opt.data_dir, 'test'))
	
	list_intrin = (os.listdir(os.path.join(train_dir, 'intrinsics')))
	intrin_dir = None
	for i in list_intrin:
		intrin_dir = os.path.join(os.path.join(os.path.abspath(train_dir), 'intrinsics'), i)
		break
	line = ""
	with open(os.path.join(os.path.abspath(intrin_dir))) as f_r:
		list_value = str(f_r.read()).split(' ')
		space = ' '
		# print(list_value)
		line_0 = list_value[0] + space + list_value[1] + space + list_value[2] + space +list_value[3] +"\n"
		line_1 = list_value[4] + space + list_value[5] + space + list_value[6] + space +list_value[7] +"\n"
		line_2 = list_value[8] + space + list_value[9] + space + list_value[10] + space +list_value[11] +"\n"
		line_3 = list_value[12] + space + list_value[13] + space + list_value[14] + space +list_value[15]
		line = line_0 + line_1 + line_2 + line_3
		print(line)
	with open(intrinsics_dir,"w") as f_w:
		f_w.write(line)
		f_w.close

	modify(os.path.join(output_temp_dir, 'train'), 'train', rgb_dir, pose_dir)
	modify(os.path.join(output_temp_dir, 'validation'), 'validation', rgb_dir, pose_dir)
	modify(os.path.join(output_temp_dir, 'test'), 'test', rgb_dir, pose_dir)
	shutil.rmtree(output_temp_dir)
	print('------------------')
	print('Changed completely')


