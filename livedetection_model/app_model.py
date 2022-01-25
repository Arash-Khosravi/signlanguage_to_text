# Paths

WORKSPACE_PATH = "Tensorflow/workspace"
SCRIPTS_PATH = "Tensorflow/scripts"
APIMODEL_PATH = "Tensorflow/models"
ANNOTATION_PATH = WORKSPACE_PATH + "/annotations"
IMAGE_PATH = WORKSPACE_PATH + "/images"
MODEL_PATH = WORKSPACE_PATH + "/models"
PRETRAINED_MODEL_PATH = WORKSPACE_PATH + "/pre-trained-models"
CONFIG_PATH = MODEL_PATH + "/app_model/pipeline.config"
CHECKPOINT_PATH = MODEL_PATH + "/app_model/"

# Create Label Map
# labels --> given by user

input_labels = None
ids = 0
labels = []
for data in input_labels:
    labels.append({"name": data.name, "id": ids + 1})

with open(ANNOTATION_PATH + "\label_map.pbtxt", "w") as f:
    for label in labels:
        f.write("item { \n")
        f.write("\tname:'{}'\n".format(label["name"]))
        f.write("\tid:{}\n".format(label["id"]))
        f.write("}\n")

# Creating Tensorflow records for train
# !python {SCRIPTS_PATH + '/generate_tfrecord.py'} -x {IMAGE_PATH + '/train'} -l {ANNOTATION_PATH + '/label_map.pbtxt'} -o {ANNOTATION_PATH + '/train.record'}
# !python {SCRIPTS_PATH + '/generate_tfrecord.py'} -x{IMAGE_PATH + '/test'} -l {ANNOTATION_PATH + '/label_map.pbtxt'} -o {ANNOTATION_PATH + '/test.record'}

# Using Pretrained Tensorflow Model Zoo
# !cd Tensorflow && git clone https://github.com/tensorflow/models

# Model Config to Training Folder
CUSTOM_MODEL_NAME = "app_model"
# !mkdir {'Tensorflow\workspace\models\\'+CUSTOM_MODEL_NAME}
# !cp {PRETRAINED_MODEL_PATH+'/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/pipeline.config'} {MODEL_PATH+'/'+CUSTOM_MODEL_NAME}
