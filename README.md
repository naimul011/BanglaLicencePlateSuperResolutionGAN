# Bangla Licence Plate Restoration Using Super Resolution Generative Adversarial Networks
## Dataset

A Bangla license plates dataset (synthetic), generated with a mixture of deep learning and image processing.

[Download the dataset](https://github.com/zabir-nabil/bangla-synthetic-license-plates/)

The images are in JPG format. The labels are in darknet yolo format. [.txt, .data, .names]

![Samples](/Samples/dataset.jpg)

<div class="cell markdown" id="nYZIRiBYyXnj">

## Load in the sample images

</div>

<div class="cell code" data-colab="{&quot;height&quot;:813,&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="gcApcEuJyXnl" data-outputId="53c33cd2-5c7d-48ce-8a92-54141e22ddc5">

``` python
import glob
#DATA_PATH = 'Samples'
DATA_PATH = '/gdrive/MyDrive/Dataset/VAL'
loader = DataLoader()
data = loader.load(glob.glob(DATA_PATH + '/*.jpg'), batchSize=1)
painter = Visualizer()
for downSample, original in data.take(4):
    painter.plot(downSample, original)
```
    
![Samples](/Samples/Capture.PNG)

## Result
### Run plate enhancement

</div>

<div class="cell code" data-colab="{&quot;height&quot;:597,&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="zHTBhifayXno" data-outputId="2898ee91-b6ef-47c1-ec53-2f939c137c81">

``` python
for downSample, original in data.take(4):
    yPred = model.predict(downSample)
    painter.plot(downSample, original, yPred)
```
![Samples](/Samples/Capture2.PNG)

