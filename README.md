夸张吹牛简述
🔥 究极文件加密分片神器 🔥
这不是普通的Python脚本，这是你数据安全的终极守护者！zip_crypto_tool.py能把你的ZIP文件加密得比银行金库还严实，再切成小块，像忍者一样神不知鬼不觉地分散存储！想恢复？一键合并解密，丝滑到飞起！它用AES加密，强度堪比核弹防护盾，分片功能精准到字节，简直是黑客的噩梦、程序员的福音！无论你是想保护商业机密还是藏私房钱（开玩笑啦），这工具都能让你高枕无忧！😎
使用教程
这个工具支持两种模式：交互式菜单模式和命令行模式，灵活到让你怀疑人生。以下是详细使用指南：
1. 准备工作
安装依赖：确保你有Python 3.x，然后安装pyzipper库：
bash
pip install pyzipper
文件准备：准备好一个.zip文件（比如data.zip）作为输入。
2. 交互式菜单模式
适合喜欢点菜式操作的小白用户！直接运行脚本：
bash
python zip_crypto_tool.py
菜单选项：
加密并分片：
输入源ZIP文件名（例如data.zip）。
设置一个超安全的密码（别忘了！）。
指定分片大小（单位MB，比如10）。
程序会生成加密后的xxx_encrypted.zip并切成xxx_encrypted.zip.part1、xxx_encrypted.zip.part2等分片文件。
合并并解密：
输入分片文件前缀（例如xxx_encrypted.zip.part）。
输入解密密码（输错就GG）。
指定输出目录（例如output_folder）。
程序会合并分片，解密内容，并提取到指定目录。
退出：优雅说再见。
3. 命令行模式
适合硬核程序员，效率拉满！直接带参数运行：
加密并分片：
bash
python zip_crypto_tool.py enc data.zip mypassword 10
enc：加密模式。
data.zip：源ZIP文件。
mypassword：加密密码。
10：分片大小（MB）。
输出：加密ZIP和分片文件（如data_encrypted.zip.part1等）。
合并并解密：
bash
python zip_crypto_tool.py dec data_encrypted.zip.part mypassword output_folder
dec：解密模式。
data_encrypted.zip.part：分片文件前缀。
mypassword：解密密码。
output_folder：解密输出目录。
输出：解密后的文件在output_folder中。
4. 注意事项
密码安全：密码输错，文件就跟你说拜拜！记好密码！
分片完整性：合并时确保所有分片文件都在当前目录，否则会报错。
文件大小：分片大小（MB）要合理，别切个1GB文件成1KB一块，累死你。
依赖环境：没装pyzipper？别问为啥跑不动，赶紧pip！
彩蛋
这脚本简直是数据安全的“瑞士军刀”！想把机密文件藏在U盘里？加密分片后随便丢几块到云端，敌人拿了也解不开！快去试试，感受一下黑科技的魅力吧！🚀
