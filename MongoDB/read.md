# 学习笔记
**schema**
#### 1.Schema是一个类，构造一个schema实例就是在创建一个表，之后也可以制定方法，schema.methods.findSimilat = function(){},schema.statics.findSimila = function(){},静态方法，但是在es6箭头函数中禁用了this，所以会报错。
#### 2.monoose即使不建立连接也可以调用models，因为mongose内部调缓存调用了model 函数，会等待连接直到连接上MongoDB。
#### 3.SchemaTypes有10种基本数据类型，
Number，
String，
Date，
Array,
Mixed：可以传入任何数据类型，Mongo没有能力自动探索该数据值，当修改后，需要人工保存下

```
person.anything = { x: [3, 4, { y: "changed" }] };
person.markModified('anything');
person.save(); // Mongoose will save changes to `anything`.

```

Buffer，
Boolean，
ObjectId，
Buffer，
Map：{"key":"value", "key2":"value"}
在设置每个数据类型的时候，可以设置option，每个类型有自己的opiton，称为属性的校验器（validator），对传入的值进行提前校验。
图片相对路径：getter用法
```
const root = 'http://www.baidu.com';
const  schema = new Schema({
    name: String,
    pic:{
        type: String,
        get: v => `$(root)$(v)`
    }
});

```
schema.path('name')//查看属性的详细信息


































