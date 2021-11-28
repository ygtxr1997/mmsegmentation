from mmcv.utils import Registry
CONVERTERS = Registry('converter')

# 使用注册器管理模块
@CONVERTERS.register_module()
class Converter1(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b


converter_cfg = dict(type='Converter1', a=1, b=2, c=3)
converter = CONVERTERS.build(converter_cfg)
print(converter)

