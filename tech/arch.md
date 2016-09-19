# 网站架构

## 目录

### 第一篇

#### 大型网站架构演化

#### 大型网站架构模式
- 分层
- 分割
- 分布式
- 集群
- 缓存
- 异步
- 冗余
- 自动化
- 安全

#### 大型网站核心架构要素
- 性能
- 可用性
- 伸缩性
- 扩展性
- 安全性

### 第二篇

#### 瞬时响应：网站的高性能架构
- 网站性能测试
- web前端优化
- 应用服务器性能优化
- 存储性能优化

#### 万无一失：网站的高可用架构
- 网站可用性度量
- 高可用的网站架构
- 高可用的应用
- 高可用的服务
- 高可用的数据
- 高可用的软件质量保证
- 网站运行监控

#### 永无止境：网站的伸缩性能
- 网站架构的伸缩性设计
- 应用服务器集群的伸缩性设计
- 分布式缓存集群的伸缩性设计
- 数据存储服务器集群的伸缩性设计

#### 随需应变：网站的可扩展架构
- 构建可扩展的网站架构
- 利用分布式消息队列降低系统耦合性
- 利用分布式服务打造可复用的业务平台
- 可扩展的数据结构

#### 固若金汤：网站的安全架构
- 网站攻击于防御
- 信息加密及密钥安全管理
- 信息过滤与反垃圾
- 电子商务风险控制

### 第三篇

#### 架构师的领导艺术
- 关注人而不是产品
- 发掘人的优秀
- 共享美好蓝图
- 共同参与架构
- 学会妥协
- 成就他人

#### 网站架构师职场攻略
- 发现问题，寻求突破
- 提出问题，寻求支持
- 解决问题，达成绩效

#### 漫画网站架构师
- 安作用划分架构师
- 安效果划分架构师
- 安职责角色划分架构师
- 安关注层次划分架构师
- 安口碑划分架构师
- 非主流方式划分架构师

# <hr/>

# 概述

## 大型网站系统特点
- 高并发，大流量
- 高可用(7*24)
- 海量数据
- 安全环境恶劣
- 需求快速变更，发布频繁
- 渐进式发展

## 大型网站演化发展历程
- 应用程序，数据库，文件等所有资源都在一台服务器上
- 应用程序，数据库，文件服务器都独立存在一台服务器上。
- 使用缓存改善网站性能 80%的业务访问集中在20%的数据上。
>将这些小部分数据保存在内存中,这样可以大大加快数据的访问,减小数据库压力.
缓存可以使用本地缓存,和专门的缓存服务器上,远程缓存服务器可以使用集群方式.

- 使用应用服务器集群,改善网站的并发能力.
>通过负载均衡服务器,将用户请求分发到应用服务器集群中的任何一台,来加快响应,提高并发.

- 数据库读写分离
>网站使用缓存后绝大部分数据访问操作都不需要通过数据库就能完成,
但是仍会有一份访问操作很全部的写操作需要访问数据库,当用户达到一定规模后
网站的数据库服务就会成为性能瓶颈<br>
目前大部分主流数据库都支持主从热备份,通过配置两台服务器的主从关系,实现读写分离.
此时架构相当于:<br>
负载军很服务器,应用服务器,数据库服务器,缓存服务器,文件服务器都独立开来

- 使用CDN和反向代理
- 使用分布式文件系统和分布式数据库系统
>分布式数据库是网站数据库拆分的最后手段,只有在单张表数据规模非常庞大的时候才使用
不到不得已时,网站更常用的数据库拆分手段是业务分库,将不同的业务数据部署到不同的物理服务器上

>此时的网站架构为:CDN服务器,反向代理服务器,负载均衡服务器,应用服务器集群,数据库服务器集群(分布式+读写分离),分布式文件服务器,分布式缓存服务器

- 使用NoSQL和搜索引擎
>随着网站业务越来越复杂,对数据库存储和检索的需求也越来越复杂,网站需要采用一些非关系型数据库技术如NoSQL和非数据库查询技术如搜索引擎<br>
搜索引擎通过应用服务器中的统一数据访问模块进行操作.<br>
`应用服务器通过一个统一的数据访问模块访问各种数据,减轻应用程序管理诸多数据源的麻烦`
此时的架构中多了一个搜索引擎集群以及NoSQL服务器集群

- 业务拆分
>大型网站的业务越来越复杂,此时需要通过分而治之的手段,将网站的业务分成不同的产品线
如大型购物网站将首页,商铺,订单,卖家,产品等拆分给不同的业务团队管理.<br>
`具体到技术上,也会根据产品线划分,将一个网站拆分成许多不同的应用,每个应用独立维护,
应用之间可以通过超链接建立关系,也可以通过消息队列进行数据分发,最多的是通过访问
同一个数据存储系统来构成一个关联的完整系统`
此时`应用服务器集群又需要按照业务来再次拆分`

- 分布式服务
>随着业务拆分越来越小,存储系统越来月大,应用系统的部署维护越来越困难<br>
既然每个系统都需要执行相同的业务操作,比如用户管理,商品管理等,那么可以将这些共用的业务提取出来,
独立部署.由这些可复用的业务链接数据库,提供共用业务服务,而应用系统只需要管理用户界面,通过分布式服务调用共用业务服务
完成具体业务操作

<hr>


