# Bangla Licence Plate Restoration Using Super Resolution Generative Adversarial Networks
## Dataset

A Bangla license plates dataset (synthetic), generated with a mixture of deep learning and image processing.

[Download the dataset](https://github.com/zabir-nabil/bangla-synthetic-license-plates/)

The images are in JPG format. The labels are in darknet yolo format. [.txt, .data, .names]

![Samples](/Samples/dataset.jpg)
<div class="cell code" id="BNlclbC6yXne">

``` python
from Utilities.io import DataLoader
from Utilities.painter import Visualizer
from Models.RRDBNet import RRDBNet# we use RRDB in this demo
```

</div>

<div class="cell code" data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="xnfLpU80iP5M" data-outputId="3bd78aa7-5054-4eef-d5f5-26fdb3901006">

``` python
from google.colab import drive
drive.mount('/gdrive')
%cd /gdrive
```

<div class="output stream stdout">

    Mounted at /gdrive
    /gdrive

</div>

</div>

<div class="cell markdown" id="nYZIRiBYyXnj">

### Load in the sample images

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

<div class="output display_data">

![](f211e0a2aa6b0b2091ff89d6123d14bf1cf8dee5.png)

</div>

<div class="output display_data">

![](e3df91ee1ba52880406991cd7f64493ef499d6a3.png)

</div>

<div class="output display_data">

![](5770eb02c76b69651eccdcde83fc02aa9cb818ca.png)

</div>

<div class="output display_data">

![](30bf213a069cbb8587a49e6ea404acdfec0ab312.png)

</div>

</div>

<div class="cell code" id="VajnA9PA-CVs">

``` python
```

</div>

<div class="cell markdown" id="eSjo1W7JyXnn">

### Load in the pretrained super-resolution model

</div>

<div class="cell code" data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="XmXtQ6WEyXnn" data-outputId="40404df6-74a9-4a80-af7f-4e3aa699e997">

``` python
# pretrained rrdb network can be found in the Pretrained folder
#MODEL_PATH = 'Pretrained/rrdb'
MODEL_PATH = '/gdrive/MyDrive/Dataset/RSGAN_M/rrdb'
model = RRDBNet(blockNum=10)
model.load_weights(MODEL_PATH)
```

<div class="output execute_result" data-execution_count="5">

    <tensorflow.python.training.tracking.util.CheckpointLoadStatus at 0x7f7279ff2c50>

</div>

</div>

<div class="cell markdown" id="czW31pYMyXno">

### Run plate enhancement

</div>

<div class="cell code" data-colab="{&quot;height&quot;:597,&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="zHTBhifayXno" data-outputId="2898ee91-b6ef-47c1-ec53-2f939c137c81">

``` python
for downSample, original in data.take(4):
    yPred = model.predict(downSample)
    painter.plot(downSample, original, yPred)
```

<div class="output display_data">

![](d1743b66171afaeb9afa735090f8eb56f827e670.png)

</div>

<div class="output display_data">

![](0544983403ad2b4d685882874bc6483d407eead8.png)

</div>

<div class="output display_data">

![](286e3ea0b980921575e17713c5d9e10a62f0ee09.png)

</div>

<div class="output display_data">

![](59b39de234d445a662fe54c39dbb04666c52095b.png)

</div>

</div>

<div class="cell code" id="twd4LI1qyXnp">

``` python
```

</div>
