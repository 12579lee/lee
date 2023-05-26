import torch
import numpy as np
import onnxruntime as ort
import cv2
# # 模型
# model = torch.hub.load(repo_or_dir=r'D:\yolo-workimport torch\yolov5-master',model=r'best.pt',source='local')  # or yolov5n - yolov5x6, custom
#
# # 图像
# img = r'D:\yolo-workimport torch\yolov5-master\data\VOCdevkit2007\voc2007\image\000006.jpg'  # or file, Path, PIL, OpenCV, numpy, list
#
# # 推理
# results = model(img)
#
# # 结果
# results.show() # or .show(), .save(), .crop(), .pandas(), etc

file = r'D:\yolo-workimport torch\yolov5-master\best1.onnx'
provider = ort.get_available_providers()[
    1 if ort.get_device() == 'GPU' else 0
]
print('设备：',provider)
model = ort.InferenceSession(file,providers=[provider])

for node_list in model.get_inputs(),model.get_outputs():
    for node in node_list:
        attr = {'name':node.name,
                'shape':node.shape,
                'type':node.type}
        print(attr)
    print('-'*60)

input_node_name = model.get_inputs()[0].name
output_node_name = [node.name for node in model.get_outputs()]

image = cv2.imread(r'D:\yolo-workimport torch\yolov5-master\data\VOCdevkit2007\voc2007\image\000006.jpg')
img = np.asanyarray(image,dtype=np.float)

print(model.run(output_names=output_node_name,
                input_feed={input_node_name:img}))




