# Minecraft_QQBot

> [!WARNING]
> 本仓库已停止更新，现重构后于 [UniBot](https://github.com/MineJPGcraft/UniBot) 维护。

### [**文档**](https://mcbot.ylmty.cc)

**一款基于 Nonebot2 用多种方式与 Minecraft 交互的 Python QQ 机器人**。功能丰富，使用简单，性能高强且可以自行配置，仅需简单配置即可使用。目前已实现的功能有：

- 多服互联，群服互通。
    - 在不同服务器之间转发消息。
    - 可在游戏内看到 QQ 群的消息。
    - 可使用指令在游戏内向 QQ 群发送消息。
    - 可播报服务器开启、关闭，玩家进入离开服务器以及死亡消息。
- 使用 WebUi 简单配置。
- 戳一戳机器人发送一言卡片。
- 可自行配置指令的开启或关闭。
- 可自行配置接入 AI 功能。
- 对 QQ 群指令相应。目前已实现的指令有：
    - `luck` 查看今日幸运指数。
    - `mcdr` 在指定的服务器上执行 MCDR 指令。
    - `list` 查询每个服务器的玩家在线情况。
    - `help` 查看帮助信息。
    - `server` 查看当前在线的服务器并显示对应编号，也可用于查看服务器占用。
    - `bound` 有关绑定白名单的指令。
    - `command` 发送指令到服务器。

更多功能还在探索中……

> [!WARNING]
> 本项目采用 GPL3 许可证，请勿商用！如若修改请务必开源并且注明出处。

## Docker 部署

本项目支持使用 Docker 进行部署，方便快捷。

### 使用 Docker Compose (推荐)

1. 确保已安装 Docker 和 Docker Compose
2. 在项目根目录下创建或修改 `.env` 配置文件
3. 运行以下命令启动服务：

```bash
git clone https://github.com/Minecraft-QQBot/BotServer
cd BotServer
docker-compose up -d
```

### 自行构建镜像

```bash
docker build -t minecraft-qqbot .
docker run -d \
  --name minecraft-qqbot \
  -p 8000:8000 \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/Plugins:/app/Plugins \
  -v $(pwd)/Resources:/app/Resources \
  -v $(pwd)/Scripts:/app/Scripts \
  -v $(pwd)/Logs:/app/Logs \
  -v $(pwd)/data:/app/data \
  --restart unless-stopped \
  minecraft-qqbot
```

## 安装插件

本机器人可通过各种方式与 Minecraft 服务器进行交互，包括：

- [Fabric](https://www.github.com/Minecraft-QQBot/Mode.Fabric) 模组（开发中）
- [Spigot](https://www.github.com/Minecraft-QQBot/Plugin.Spigot) 插件
- [McdReforged](https://www.github.com/Minecraft-QQBot/Plugin.McdReforged) 插件
- [FakePlayer](https://www.github.com/Minecraft-QQBot/Platform.FakePlayer) 工具

请前往你需要插件的仓库按照说明进行安装。请注意，不同的插件所提供的功能可能是不一样的，您可根据需求选择安装。

如你有能力开发其他的对接插件，欢迎联系并加入我们！

## 安装教程

请参考 [快速开始](https://mcbot.ytb.icu/%E6%96%87%E6%A1%A3/%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.html) 进行安装。  

## 鸣谢

感谢 [Lagrange](https://lagrangedev.github.io/Lagrange.Doc/) 提供了稳定的 QQ 协议端。

感谢以下人员为此机器人开发提供帮助，在此特别鸣谢：

- [Msg_Lbo](https://github.com/Msg-Lbo) 提供网站服务器以及域名，贡献 WebUi 代码。
- [meng877](https://github.com/meng877) 提出意见，贡献部分代码。
- [Decent_Kook](https://github.com/AISophon) 提供测试环境，提出意见，帮忙宣传。
- [creepebucket](https://github.com/creepebucket) 提供测试环境。

> [!TIP]
> 若遇到问题，或有更好的想法，可以加入 QQ 群 [`962802248`](https://qm.qq.com/q/B3kmvJl2xO) 或者提交 Issues
> 向作者反馈。若你有能力，欢迎为本项目提供代码贡献！

## 友链

- TQM 服务器
- [LemonFate 服务器](https://www.lemonfate.cn/)
- [RedstoneDaily 红石日报](https://www.redstonedaily.com/)
