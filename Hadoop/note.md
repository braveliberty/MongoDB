1.hdfs与MapReduce是hadoop关键的两个模块，他们是构建在网络上的分布式系统，正因为是分布式的，所以需要保证读写的统一与有效容错等等。

2.hdfs下有NameNode与DataNode，mapreduce有JobTracker与TaskTracker，还有secondeNameNode来备份，一般是DataNode与taskTracker在同一个节点上，
JobTracker与NameNode则建议在在同一个节点上，相当于都是master/slave模式.master节点内存与硬盘都是slave节点的两倍。

3.hdfs文件块：跟硬盘一样hdfs也有文件块概念，只不过比硬盘的块一般都大（可以减少寻址开销），在hdfs-site.xml文件中可以设置；
   将文件以块存储的优点：1) 可以保存比单一节点大的文件：超越了磁盘的限制，只需进行切分 
			 2）简化存储系统：见存储系统以块为单位进行管理，简化了存储管理，同时将元数据与真数据进行分开管理。
			 3）容错性高：有损坏时，集群会将副本拷贝到能正常的工作节点。
4.NameNode与SecondNameNode交互：NameNode中有命名空间镜像文件FSImage与edit.log文件，核心文件，fsimage维护了目录树，NameNode会将修改先写入edit.log当需要进行一次写入到fsimage时过程：
	1）暂时将日志写入到editlog.new
	2）赋值editlog到secondnamenode然后进行合并，合并好后传送回去，将editlog.new改为edit.log。

5.hdfs容错机制：
1）心跳机制：如果某个datanode没有心跳，则不会往这个datanode派发io操作，当探测到副本数小于设置值时，也会复制新的副本出来。
2）文件块校验和：新创建文件都会有一个校验和，以后使用时会首先检验校验和是否一致，如果不一致则认为损坏，然后从其他块复制副本。
3）负载均衡：当某个datanode空闲空间大于临界值则认为数据分布不均，hdfs会将其他数据迁移过来。
4） fsimage文件与edit log文件是核心文件，如果出错则集群会出错，需要人工干预。
5）文件删除原理：只是移除命名空间，放到/trash目录中，随时可以恢复，超过设置时间自动删除，hdfs-site.xml中 fs.trash.inteval设置秒数。



