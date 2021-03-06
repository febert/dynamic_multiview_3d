import os
current_dir = os.path.dirname(os.path.realpath(__file__))

# tf record data location:
import dyn_mult_view
DATA_DIR = '/'.join(str.split(dyn_mult_view.__file__, '/')[:-2]) + '/trainingdata/cardataset/train'

# local output directory
OUT_DIR = current_dir + '/modeldata'

configuration = {
'experiment_name': 'rndaction_var10',
'data_dir': DATA_DIR,       # 'directory containing data.' ,
'output_dir': OUT_DIR,      #'directory for model checkpoints.' ,
'current_dir': current_dir,   #'directory for writing summary.' ,
'num_iterations': 200000,   #'number of training iterations.' ,
'batch_size':64,
'learning_rate':1e-4,
'train_val_split':0.95,
'use_depth':'',
'depth_lr_factor':1.
}