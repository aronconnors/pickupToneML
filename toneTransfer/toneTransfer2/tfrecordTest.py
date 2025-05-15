import tensorflow as tf

dataset = tf.data.TFRecordDataset('data/train.tfrecord-00000-of-00001')
example = tf.train.Example()
example.ParseFromString(next(iter(dataset)).numpy())
print(example)
