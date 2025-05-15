import sys
from absl import app
from ddsp.training.data_preparation import ddsp_prepare_tfrecord as prep_script

sys.argv = [
    'ddsp_prepare_tfrecord',
    '--input_audio_filepatterns=data/audio/*.wav',
    '--output_tfrecord_path=data/train.tfrecord',
    '--example_secs=1.5',
    '--sample_rate=16000',
    '--alsologtostderr'
]

app.run(prep_script.main)


