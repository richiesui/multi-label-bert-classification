bert_vars = [
    # embeddings
    "bert/embeddings/word_embeddings",
    "bert/embeddings/token_type_embeddings",
    "bert/embeddings/position_embeddings",
    "bert/embeddings/LayerNorm/beta",
    "bert/embeddings/LayerNorm/gamma",

    # layer_0
    "bert/encoder/layer_0/attention/output/LayerNorm/beta",
    "bert/encoder/layer_0/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_0/attention/output/dense/bias",
    "bert/encoder/layer_0/attention/output/dense/kernel",
    "bert/encoder/layer_0/attention/self/query/bias",
    "bert/encoder/layer_0/attention/self/query/kernel",
    "bert/encoder/layer_0/attention/self/key/bias",
    "bert/encoder/layer_0/attention/self/key/kernel",
    "bert/encoder/layer_0/attention/self/value/bias",
    "bert/encoder/layer_0/attention/self/value/kernel",
    "bert/encoder/layer_0/intermediate/dense/bias",
    "bert/encoder/layer_0/intermediate/dense/kernel",
    "bert/encoder/layer_0/output/LayerNorm/beta",
    "bert/encoder/layer_0/output/LayerNorm/gamma",
    "bert/encoder/layer_0/output/dense/bias",
    "bert/encoder/layer_0/output/dense/kernel",

    # layer_1
    "bert/encoder/layer_1/attention/output/LayerNorm/beta",
    "bert/encoder/layer_1/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_1/attention/output/dense/bias",
    "bert/encoder/layer_1/attention/output/dense/kernel",
    "bert/encoder/layer_1/attention/self/key/bias",
    "bert/encoder/layer_1/attention/self/key/kernel",
    "bert/encoder/layer_1/attention/self/query/bias",
    "bert/encoder/layer_1/attention/self/query/kernel",
    "bert/encoder/layer_1/attention/self/value/bias",
    "bert/encoder/layer_1/attention/self/value/kernel",
    "bert/encoder/layer_1/intermediate/dense/bias",
    "bert/encoder/layer_1/intermediate/dense/kernel",
    "bert/encoder/layer_1/output/LayerNorm/beta",
    "bert/encoder/layer_1/output/LayerNorm/gamma",
    "bert/encoder/layer_1/output/dense/bias",
    "bert/encoder/layer_1/output/dense/kernel",

    # layer2
    "bert/encoder/layer_2/attention/output/LayerNorm/beta",
    "bert/encoder/layer_2/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_2/attention/output/dense/bias",
    "bert/encoder/layer_2/attention/output/dense/kernel",
    "bert/encoder/layer_2/attention/self/key/bias",
    "bert/encoder/layer_2/attention/self/key/kernel",
    "bert/encoder/layer_2/attention/self/query/bias",
    "bert/encoder/layer_2/attention/self/query/kernel",
    "bert/encoder/layer_2/attention/self/value/bias",
    "bert/encoder/layer_2/attention/self/value/kernel",
    "bert/encoder/layer_2/intermediate/dense/bias",
    "bert/encoder/layer_2/intermediate/dense/kernel",
    "bert/encoder/layer_2/output/LayerNorm/beta",
    "bert/encoder/layer_2/output/LayerNorm/gamma",
    "bert/encoder/layer_2/output/dense/bias",
    "bert/encoder/layer_2/output/dense/kernel",

    # layer3
    "bert/encoder/layer_3/attention/output/LayerNorm/beta",
    "bert/encoder/layer_3/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_3/attention/output/dense/bias",
    "bert/encoder/layer_3/attention/output/dense/kernel",
    "bert/encoder/layer_3/attention/self/key/bias",
    "bert/encoder/layer_3/attention/self/key/kernel",
    "bert/encoder/layer_3/attention/self/query/bias",
    "bert/encoder/layer_3/attention/self/query/kernel",
    "bert/encoder/layer_3/attention/self/value/bias",
    "bert/encoder/layer_3/attention/self/value/kernel",
    "bert/encoder/layer_3/intermediate/dense/bias",
    "bert/encoder/layer_3/intermediate/dense/kernel",
    "bert/encoder/layer_3/output/LayerNorm/beta",
    "bert/encoder/layer_3/output/LayerNorm/gamma",
    "bert/encoder/layer_3/output/dense/bias",
    "bert/encoder/layer_3/output/dense/kernel",

    # layer4
    "bert/encoder/layer_4/attention/output/LayerNorm/beta",
    "bert/encoder/layer_4/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_4/attention/output/dense/bias",
    "bert/encoder/layer_4/attention/output/dense/kernel",
    "bert/encoder/layer_4/attention/self/key/bias",
    "bert/encoder/layer_4/attention/self/key/kernel",
    "bert/encoder/layer_4/attention/self/query/bias",
    "bert/encoder/layer_4/attention/self/query/kernel",
    "bert/encoder/layer_4/attention/self/value/bias",
    "bert/encoder/layer_4/attention/self/value/kernel",
    "bert/encoder/layer_4/intermediate/dense/bias",
    "bert/encoder/layer_4/intermediate/dense/kernel",
    "bert/encoder/layer_4/output/LayerNorm/beta",
    "bert/encoder/layer_4/output/LayerNorm/gamma",
    "bert/encoder/layer_4/output/dense/bias",
    "bert/encoder/layer_4/output/dense/kernel",

    # layer_5
    "bert/encoder/layer_5/attention/output/LayerNorm/beta",
    "bert/encoder/layer_5/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_5/attention/output/dense/bias",
    "bert/encoder/layer_5/attention/output/dense/kernel",
    "bert/encoder/layer_5/attention/self/key/bias",
    "bert/encoder/layer_5/attention/self/key/kernel",
    "bert/encoder/layer_5/attention/self/query/bias",
    "bert/encoder/layer_5/attention/self/query/kernel",
    "bert/encoder/layer_5/attention/self/value/bias",
    "bert/encoder/layer_5/attention/self/value/kernel",
    "bert/encoder/layer_5/intermediate/dense/bias",
    "bert/encoder/layer_5/intermediate/dense/kernel",
    "bert/encoder/layer_5/output/LayerNorm/beta",
    "bert/encoder/layer_5/output/LayerNorm/gamma",
    "bert/encoder/layer_5/output/dense/bias",
    "bert/encoder/layer_5/output/dense/kernel",

    # layer_6
    "bert/encoder/layer_6/attention/output/LayerNorm/beta",
    "bert/encoder/layer_6/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_6/attention/output/dense/bias",
    "bert/encoder/layer_6/attention/output/dense/kernel",
    "bert/encoder/layer_6/attention/self/key/bias",
    "bert/encoder/layer_6/attention/self/key/kernel",
    "bert/encoder/layer_6/attention/self/query/bias",
    "bert/encoder/layer_6/attention/self/query/kernel",
    "bert/encoder/layer_6/attention/self/value/bias",
    "bert/encoder/layer_6/attention/self/value/kernel",
    "bert/encoder/layer_6/intermediate/dense/bias",
    "bert/encoder/layer_6/intermediate/dense/kernel",
    "bert/encoder/layer_6/output/LayerNorm/beta",
    "bert/encoder/layer_6/output/LayerNorm/gamma",
    "bert/encoder/layer_6/output/dense/bias",
    "bert/encoder/layer_6/output/dense/kernel",

    # layer_7
    "bert/encoder/layer_7/attention/output/LayerNorm/beta",
    "bert/encoder/layer_7/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_7/attention/output/dense/bias",
    "bert/encoder/layer_7/attention/output/dense/kernel",
    "bert/encoder/layer_7/attention/self/key/bias",
    "bert/encoder/layer_7/attention/self/key/kernel",
    "bert/encoder/layer_7/attention/self/query/bias",
    "bert/encoder/layer_7/attention/self/query/kernel",
    "bert/encoder/layer_7/attention/self/value/bias",
    "bert/encoder/layer_7/attention/self/value/kernel",
    "bert/encoder/layer_7/intermediate/dense/bias",
    "bert/encoder/layer_7/intermediate/dense/kernel",
    "bert/encoder/layer_7/output/LayerNorm/beta",
    "bert/encoder/layer_7/output/LayerNorm/gamma",
    "bert/encoder/layer_7/output/dense/bias",
    "bert/encoder/layer_7/output/dense/kernel",

    # layer_8
    "bert/encoder/layer_8/attention/output/LayerNorm/beta",
    "bert/encoder/layer_8/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_8/attention/output/dense/bias",
    "bert/encoder/layer_8/attention/output/dense/kernel",
    "bert/encoder/layer_8/attention/self/key/bias",
    "bert/encoder/layer_8/attention/self/key/kernel",
    "bert/encoder/layer_8/attention/self/query/bias",
    "bert/encoder/layer_8/attention/self/query/kernel",
    "bert/encoder/layer_8/attention/self/value/bias",
    "bert/encoder/layer_8/attention/self/value/kernel",
    "bert/encoder/layer_8/intermediate/dense/bias",
    "bert/encoder/layer_8/intermediate/dense/kernel",
    "bert/encoder/layer_8/output/LayerNorm/beta",
    "bert/encoder/layer_8/output/LayerNorm/gamma",
    "bert/encoder/layer_8/output/dense/bias",
    "bert/encoder/layer_8/output/dense/kernel",

    # layer_9
    "bert/encoder/layer_9/attention/output/LayerNorm/beta",
    "bert/encoder/layer_9/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_9/attention/output/dense/bias",
    "bert/encoder/layer_9/attention/output/dense/kernel",
    "bert/encoder/layer_9/attention/self/key/bias",
    "bert/encoder/layer_9/attention/self/key/kernel",
    "bert/encoder/layer_9/attention/self/query/bias",
    "bert/encoder/layer_9/attention/self/query/kernel",
    "bert/encoder/layer_9/attention/self/value/bias",
    "bert/encoder/layer_9/attention/self/value/kernel",
    "bert/encoder/layer_9/intermediate/dense/bias",
    "bert/encoder/layer_9/intermediate/dense/kernel",
    "bert/encoder/layer_9/output/LayerNorm/beta",
    "bert/encoder/layer_9/output/LayerNorm/gamma",
    "bert/encoder/layer_9/output/dense/bias",
    "bert/encoder/layer_9/output/dense/kernel",

    # layer_10
    "bert/encoder/layer_10/attention/output/LayerNorm/beta",
    "bert/encoder/layer_10/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_10/attention/output/dense/bias",
    "bert/encoder/layer_10/attention/output/dense/kernel",
    "bert/encoder/layer_10/attention/self/key/bias",
    "bert/encoder/layer_10/attention/self/key/kernel",
    "bert/encoder/layer_10/attention/self/query/bias",
    "bert/encoder/layer_10/attention/self/query/kernel",
    "bert/encoder/layer_10/attention/self/value/bias",
    "bert/encoder/layer_10/attention/self/value/kernel",
    "bert/encoder/layer_10/intermediate/dense/bias",
    "bert/encoder/layer_10/intermediate/dense/kernel",
    "bert/encoder/layer_10/output/LayerNorm/beta",
    "bert/encoder/layer_10/output/LayerNorm/gamma",
    "bert/encoder/layer_10/output/dense/bias",
    "bert/encoder/layer_10/output/dense/kernel",

    # layer_11
    "bert/encoder/layer_11/attention/output/LayerNorm/beta",
    "bert/encoder/layer_11/attention/output/LayerNorm/gamma",
    "bert/encoder/layer_11/attention/output/dense/bias",
    "bert/encoder/layer_11/attention/output/dense/kernel",
    "bert/encoder/layer_11/attention/self/key/bias",
    "bert/encoder/layer_11/attention/self/key/kernel",
    "bert/encoder/layer_11/attention/self/query/bias",
    "bert/encoder/layer_11/attention/self/query/kernel",
    "bert/encoder/layer_11/attention/self/value/bias",
    "bert/encoder/layer_11/attention/self/value/kernel",
    "bert/encoder/layer_11/intermediate/dense/bias",
    "bert/encoder/layer_11/intermediate/dense/kernel",
    "bert/encoder/layer_11/output/LayerNorm/beta",
    "bert/encoder/layer_11/output/LayerNorm/gamma",
    "bert/encoder/layer_11/output/dense/bias",
    "bert/encoder/layer_11/output/dense/kernel",

    # dense
    "bert/pooler/dense/bias",
    "bert/pooler/dense/kernel"
]
