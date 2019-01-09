# 学习笔记
**schema**
#### 1.Schema是一个类，构造一个schema实例就是在创建一个表，之后也可以制定方法，schema.methods.findSimilat = function(){},schema.statics.findSimila = function(){},静态方法，但是在es6箭头函数中禁用了this，所以会报错。
sljdfl
#### 1.monoose即使不建立连接也可以调用models，因为mongose内部调缓存调用了model 函数，会等待连接直到连接上MongoDB。
