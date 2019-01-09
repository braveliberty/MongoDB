# MongoDB
## 1. schema：通过Mongoose.schema拿到Schema对象，本质上是一个Class，通过new Schema的方式创建表
```
const schema = new Schema(
	{
		name:String,
		age: Number
		})
```
