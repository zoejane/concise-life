# 简练日志小站

## Logs

### 20170824

### 目标

- 建立专门的 concise-life github repo
- 生成独立网址 （github pages）
- 采用 wiki 方式记录 （simiki / wiki 方式比 blog 方式更系统，方便在历史基础上迭代）
- 初始文稿统一放在 Ulysses 的 DebugUself 文件夹

### 步骤

- 新建 repo
- git clone 到本地
- simiki 安装 （需配置 xcode / zsh 配置好快速使用 proxy ）
- simiki deploy (根据官方文档，将相应内容推送到 gh-pages ，用 GitHub Pages 的方式展示)
- 添加对应的文件夹 Init / Journal，添加初始文档

### 体验

- GitHub 这个真实的环境，就足够有意思，值得好好玩了
- 即使我不能换到别的工作又如何，我依然能在 GitHub 上尽情做各种我喜欢做的事情，认识我喜欢的人，这种感觉也挺好。我不需要一定要一份工作才能开始自己的项目，我可以现在就开始
- Talk is cheap, show me the code
- 在环境配置中会踩到很多坑，这个是教学环境中刻意避免的，教学环境更像温室的花朵，而且是在它搭好的脚手架上往前走的，脱离了脚手架就有点无所适从。所以还是要拥抱真实世界的真实项目。

### 20170825

### 目标

- 将 wiki 迁移到另外的 mobile 阅读更友好的系统上 ( 暂定 GitBook，虽然 Blog 阅读体验友好，但是写作时不够系统，更倾向于流水记录，而不是体系搭建)

### 步骤

- 阅读 GitBook Help 中和 GitHub 有关的部分
- 链接 GitBook 与 已有仓库
- 测试网页版同步正常
- 在 GitHub 上搜索GitBook 的 CLI 工具，初步阅读文档
- 下载 GitBook 的 CLI 工具 （给 npm 配置 cnpm 用于下载）
- 测试 CLI 的基本使用
- 尝试使用 simiki 提供的方式，将 build 的 static website deploy 到 GitHub Pages 
	- 似乎 master 和 gh-pages 想要都用的话，会让 gh-pages 的commit history 无法保留，一次性发布可以，保留历史的发布有问题，这个可能是 simiki 用什么方式绕过了这个问题，别的服务用这种方式的话，似乎只保留 gh-pages 的方式比较好，待继续探索
- CLI 自带修订 markdown 自动更新本地 static website 的效果( 比网页版快很多倍，Cool )
- 添加对应文章 和 Summary （添加 zsh alias subl）
- deploy 最后是用的 gitbook 提供的 domain 的设置，成功建立小站 http://concise-life.zoejane.net

### 体验

- 官方文档真的很好用，其实根本不用使用 Google 大法搜索，很多问题直接看文档。既是最新的，又很全面，同时也很权威。
	- 不会拐到莫名奇妙的坑里，比如解决方案过时了，比如寻找不到合适的解决方案。
	- 速度快。文档内容其实非常短，比搜索快多了，节约许多时间。
- 命令行工具真好用啊，GitBook 的网页版， Desktop 版用起来都非常慢。真正用到命令行，被它的简洁和速度感动了！原来命令行这么好用！本地修订就能实时预览，再也不用为了看最终效果而苦苦等待。
- 命令行的一大坑就是环境部署，比如这里就遇到了 npm 下载比较慢的问题，对无尽的等待实在是心有余悸。不过知道这个有国内镜像站，所以 Google 搜到了合适的解决方案。proxy + cnpm，速度慢的问题一解决，就能看到命令行的畅快世界啦。
- ZoomQuiet 说的真的都是对的，看官方文档，用命令行，真的就是打开全新世界的体验。感觉节约了好多生命！