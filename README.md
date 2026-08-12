# 掌心窗公开版 v0.3.5.1-cleartext-http

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/linzhi-524/linjian-peek-public)

> 这个按钮已指向公开仓库 `linzhi-524/linjian-peek-public`。仓库根目录已补 `render.yaml`，按钮会按 Blueprint 创建 `server` 和 `mcp` 两个服务，并共用同一个 `LINJIAN_TOKEN`。

掌心窗是一套“手机端 App + 同步后端 + MCP 服务”的小工具。它可以在你本人授权后，让你设置的陪伴对象看见手机生活状态、请求截图、打开 App、返回/主页/最近任务、点击/滑动、发送通知、设置闹钟、读取轻量生活状态，并在你需要时做应用门禁和主动提醒。

这一版把自用版 v0.3.4 的功能和 UI 同步到公开版：总览、看见、守护、设置四页结构一致；天气地区、应用门禁、主动提醒、周期提醒都收进抽屉；同时去掉私人名字、私人设备 ID、私人城市和私用默认配置。默认保留“老公 / 宝宝”的关系语感，但称呼可以在手机端设置里改成你们自己的称呼。设置后的名称会同步到提醒、看一眼、回家模式和门禁页。

> 重要提醒：截图、读屏、控制手机、通知、闹钟、应用门禁、自动打开目标 App 都是敏感能力。只在本人设备、本人服务器、本人明确授权的场景使用。不要把 Token 发给别人，也不要接入不可信 MCP 客户端。



## v0.3.5.1 HTTP 明文连接修复版

这一版是在 v0.3.5.0 归电公开版基础上的 hotfix，主要解决部分用户使用本地/局域网纯 HTTP 服务时，Android 端后台轮询被系统拦截的问题。

- AndroidManifest 已将 `android:usesCleartextTraffic` 改为 `true`。
- 支持连接 `http://192.168.x.x:8513`、`http://局域网IP:端口` 这类本地 HTTP 服务。
- 修复日志里反复出现 `Cleartext HTTP traffic to 192.168.x.x not permitted` 的问题。
- 保留 v0.3.5.0 的归电、感官页、守护页、设置页和 MCP 功能。
- 公网/正式部署仍推荐 HTTPS；本修复主要面向本人设备、局域网测试和自建 HTTP 服务。

## v0.3.5.0 归电感官版

这一版把私用版里的「归电」搬到公开版，但不合并聆音、鲸鸣、声息等私用功能。

- 「感官」页新增归电状态卡：显示上次回来、下次最早归电、今日次数、最近拒绝理由和自动检查结果。
- 「设置」页新增归电设置：可改归电开关、远程调整许可、全屏来电、提醒间隔、冷却时间、每日上限、安静时段、目标 App、主题、来电文案池和拒绝理由。
- 归电对象会读取设置里的“对方称呼 / AI 名字”；文案池支持 `{AI}` 和 `{USER}` 占位符。
- 目标 App 可填 `ChatGPT`、`Claude`、`Gemini`、已保存的应用昵称，或直接填写 Android 包名。接受归电后会跳转到这个目标 App。
- MCP 新增 `get_guidian_state`、`set_guidian_config`、`trigger_guidian`、`mark_guidian_returned` 和轻量 `get_senses_state`。

> 归电只记录连接/回来时间、当前前台包名和拒绝理由，不读取聊天内容。

## v0.3.4.6 回家目标统一与许可补充

这一版主要修复公开版用户把回家模式目标改成 Claude / Gemini / 自定义包名后，通知详情页仍然写死打开 ChatGPT 的问题。

- 回家模式目标 App 支持填写 `ChatGPT`、`Claude`、`Gemini` 或任意有效 Android 包名。
- 通知详情页的“回到对方这里”按钮会读取同一个回家目标，不再固定打开 ChatGPT。
- 设置里的对方称呼会同步到“提醒”“看一眼”“回家模式”和门禁页，避免一处改名、一处仍显示默认称呼。
- 用户称呼仍可在设置里修改；为空时默认使用“宝宝”。
- 版本与更新面板新增许可摘要。
- 补充 LICENSE：允许个人学习、自用部署和本地修改；未经授权不得改名分发、发布衍生 APK、商业售卖或移除原作者说明。

## 许可与二次分发

本项目当前采用自定义个人使用许可，不是 MIT / Apache / GPL 等开放源代码许可证。你可以阅读源码、学习、个人自用部署和本地修改 UI；但未经项目作者明确许可，不允许改名重新发布、分发衍生 APK、商业售卖、提供付费代部署，也不允许移除原作者说明和许可文件。完整条款见 `LICENSE`。

## v0.3.4.5 轻量修复

这一版是公开版 hotfix，不合并私用声息功能，重点修复 v0.3.4.4 把部分用户自建 Render 域名误判为旧地址的问题。

- 不再按 `rork` 或具体域名黑名单拦截服务器地址。
- 所有用户自建的 `https://xxx.onrender.com` 都允许保存和连接。
- 连接失败时按真实原因显示日志：DNS 解析失败、Render 冷启动、Token 不一致、接口不匹配或服务器错误。
- 保留 v0.3.4 系列显示适配、版本与更新、禁用自动备份等修复。
- README 原有 Render 一键部署、本地 / 局域网部署、Hugging Face 部署和 MCP 教程全部保留。

## 目录说明

- `android/`：手机端 App，App 名为「掌心窗」。
- `server/`：统一后端，保存截图、命令队列、执行回传和手机生活状态。
- `mcp/`：MCP 服务，给支持 MCP 的客户端暴露工具。
- `docs/`：补充说明、MCP 工具清单和版本记录。

## 本版公开化改动

- UI 同步到 v0.3.4：总览 / 看见 / 守护 / 设置，顶部小标题栏，轻卡片，抽屉式功能收纳。
- 保留关系感，但新增称呼设置：可以改“老公”和“宝宝”等默认称呼，并同步到提醒、看一眼、回家模式和门禁页。
- 默认设备 ID 改为 `android-phone`，不带私人设备名。
- 默认天气地区改为通用示例，不带私人城市；用户可在“天气地区”抽屉里自行添加。
- 应用门禁同步私用版功能，但公开版不内置私人锁定理由和私人口令。
- 包名白名单包含 ChatGPT、Gemini、Claude、微博、X，并保留小红书、微信、QQ、抖音、Speedcat。回家目标 App 不再固定为 ChatGPT。
- README 保留 Render 一键部署和本地 / 局域网部署教程，MCP 工具清单补全到 v0.3.4。

## MCP 工具

详见 `docs/mcp.md`。常用工具包括：

- 看见与状态：`peek_screen`、`latest_screen`、`linjian_status`、`get_life_state`、`get_phone_state`、`get_screen_nodes`。
- 天气与提醒：`send_notification`、`send_weather_notification`、`set_alarm`。
- 手机控制：`open_app`、`phone_home`、`phone_back`、`phone_recents`、`tap`、`swipe`、`tap_text`、`input_text`、`run_sequence`、`run_preset`。
- 应用包名：`list_known_apps`、`save_known_app`。
- 小红书辅助：`draft_xhs_comment`、`xhs_comment`、`send_visible_comment_after_confirmation`。
- 应用门禁：`lock_app`、`unlock_app`、`temporary_unlock_app`、`extend_lock`、`deny_unlock_request`、`get_lock_state`、`set_emergency_passphrase`、`list_lockable_apps`。

## 手机端安装

最省心的方式：把项目上传 GitHub，打开 **Actions → Build Android Debug APK → Run workflow**，等构建完成后在 Artifacts 里下载 APK。

手机安装后：

1. 打开《掌心窗》。
2. 填统一后端地址，例如 `https://你的-server.onrender.com`。
3. 填 `LINJIAN_TOKEN`，必须和后端环境变量完全一致。
4. 设备 ID 默认 `android-phone`，多台设备时可以改成 `my-phone`、`pad` 等。
5. 打开无障碍服务；Android 13+ 还要允许通知权限。
6. 回到 App，点“启动”。
7. 点“给对方看一眼”，后端能收到截图就说明主链路通了。

## 部署教程 1：Render 一键 / 手动部署

### 方式一：点 README 顶部的一键部署按钮

1. 确认代码已经上传到公开仓库 `linzhi-524/linjian-peek-public`。
2. 点击 README 顶部的 **Deploy to Render** 按钮。Render 会读取仓库根目录的 `render.yaml`。
3. 确认创建两个 Web Service：
   - `zhangxinchuang-server`：手机端连接的统一后端。
   - `zhangxinchuang-mcp`：AI 客户端连接的 MCP 服务。
4. 部署完成后，手机 App 里填写 `zhangxinchuang-server` 的外部地址；AI 客户端里填写 `zhangxinchuang-mcp` 的 `/mcp` 或 `/sse` 地址。

> 一键部署会自动生成并共用 `LINJIAN_TOKEN`。如果后续手动改 Token，记得 server、mcp、手机端三处必须一致。

### 方式二：手动创建 Render 服务

下面是手动配置，适合一键部署失败时照着填。

### A. 部署后端 server

Render 新建 **Web Service**，连接你的 GitHub 仓库。

配置：

```text
Root Directory: server
Build Command: 留空 或 echo ok
Start Command: python linjian_server.py
```

环境变量：

```text
LINJIAN_TOKEN=自己生成的一长串随机 token
LINJIAN_HOST=0.0.0.0
LINJIAN_KEEP=3
```

生成 Token 的方法：

```bash
python3 - <<'PY'
import secrets
print(secrets.token_urlsafe(32))
PY
```

部署完成后，打开 Render 给你的地址，例如：

```text
https://your-peek-server.onrender.com/health
```

看到 `ok: true` 就说明后端在线。

### B. 部署 MCP

再新建一个 Render Web Service，仍然连接同一个仓库。

配置：

```text
Root Directory: mcp
Build Command: npm install
Start Command: npm start
```

环境变量：

```text
LINJIAN_URL=https://你的后端地址.onrender.com
LINJIAN_TOKEN=和后端完全一样的 token
LINJIAN_DEFAULT_DEVICE=android-phone
```

部署完成后，MCP 地址通常是：

```text
https://your-peek-mcp.onrender.com/mcp
```

如果你的客户端只支持 SSE，就用：

```text
https://your-peek-mcp.onrender.com/sse
```

## 部署教程 2：Hugging Face Spaces

Hugging Face Spaces 更适合公开展示或免费测试。建议分成两个 Space：一个跑 `server`，一个跑 `mcp`。

### A. server Space

1. 打开 Hugging Face，点 **New Space**。
2. Space SDK 选 **Docker**。
3. 新建后，把本仓库上传进去。
4. 在 Space 根目录新建一个 `Dockerfile`，内容如下：

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY server/ /app/
ENV LINJIAN_HOST=0.0.0.0
ENV PORT=7860
CMD ["python", "linjian_server.py"]
```

5. 在 Space 的 **Settings → Variables and secrets** 添加：

```text
LINJIAN_TOKEN=自己生成的一长串随机 token
LINJIAN_KEEP=3
```

6. 等 Space 构建完成，访问：

```text
https://你的用户名-your-server.hf.space/health
```

看到 `ok: true` 就成功。

### B. MCP Space

再建第二个 Docker Space，把本仓库上传进去，根目录 `Dockerfile` 改成：

```dockerfile
FROM node:20-slim
WORKDIR /app
COPY mcp/package*.json /app/
RUN npm install
COPY mcp/ /app/
ENV PORT=7860
CMD ["npm", "start"]
```

在 Space 的 Variables and secrets 添加：

```text
LINJIAN_URL=https://你的-server-space.hf.space
LINJIAN_TOKEN=和 server 完全一样的 token
LINJIAN_DEFAULT_DEVICE=android-phone
```

MCP 地址：

```text
https://你的用户名-your-mcp.hf.space/mcp
```

SSE 地址：

```text
https://你的用户名-your-mcp.hf.space/sse
```

## 部署教程 3：本地 / Codespaces

适合先测试，不一定要公网。

### A. 启动后端

```bash
cd server
python3 - <<'PY'
import secrets
print('LINJIAN_TOKEN=' + secrets.token_urlsafe(32))
PY
```

把输出的 Token 记下来，然后启动：

```bash
export LINJIAN_TOKEN='换成刚刚生成的token'
export LINJIAN_HOST=0.0.0.0
export LINJIAN_PORT=8513
python3 linjian_server.py
```

看到 `掌心窗 server started` 或访问 `/health` 正常即可。

### B. 启动 MCP

新开一个终端：

```bash
cd mcp
npm install
export LINJIAN_URL='http://127.0.0.1:8513'
export LINJIAN_TOKEN='和后端一样的token'
export LINJIAN_DEFAULT_DEVICE='android-phone'
npm start
```

本地 MCP 地址：

```text
http://127.0.0.1:8787/mcp
```

Codespaces 里要把端口 8513 和 8787 设为公开或转发，再把手机端服务器地址填成 8513 的公开地址。

## 常见问题

### 手机没有反应

先看这几项：

1. App 里服务器地址是否是完整 `https://...`，不要多一个斜杠。
2. 手机端 Token、server 环境变量、MCP 环境变量是否完全一致。
3. 手机端是否点了“启动”。
4. 无障碍服务是否开启。
5. Android 13+ 是否允许通知权限。
6. Render / Hugging Face 免费实例是否刚从休眠中醒来，第一次请求可能慢。

### 截图截到前一个页面

截图前加等待，例如 `wait_seconds=20`，或者先回到目标 App 前台再请求截图。

### 打不开目标 App

公开版不默认回 ChatGPT。请在 App 的“状态 → 回家模式 → 目标 App 包名”里填写你自己的目标包名，例如某个 AI 客户端或浏览器包名。也可以用 `save_known_app` 保存昵称，再用 `open_app` 打开。

### 小红书评论模式怎么用

- `mode=manual`：只写入草稿，不自动发送。
- `mode=auto`：追加 `author_tag` 后自动点发送。只在你明确授权时使用。

示例：

```json
{
  "text": "这个标题真的有点茶哈哈哈",
  "mode": "manual",
  "author_tag": "（AI助手发）"
}
```

## 安全边界

- Token 不能公开。
- MCP 地址如果内置了 Token，也不能公开。
- 不要接入陌生人提供的 MCP 客户端。
- 不要在他人设备上使用。
- 回家模式可以只开提醒，不开自动打开目标 App。
- 评论自动发送建议默认关闭，先用草稿模式确认。

- v0.2.2 hotfix: allow LAN HTTP backend for self-hosted users.


## v0.3.4.5 Render 地址说明

如果你的 Render 服务名里带 `rork`，这是允许的。v0.3.4.5 不再按域名关键词拦截服务器地址。

正确填写格式：

```
https://你的服务名.onrender.com
```

也可以误填 `/health` 或 `/api/poll`，App 会自动清理成主地址。

排查顺序：先用浏览器打开 `https://你的服务名.onrender.com/health`，确认服务能响应；再检查 App Token 是否与 Render 环境变量一致。

## v0.3.4.5 不再误拦 Render 域名

v0.3.4.4 曾把部分带 `rork` 的地址当作旧测试地址拦截。v0.3.4.5 已取消这个黑名单逻辑，改为按真实联网结果判断。

常见日志含义：

- `DNS 解析失败`：手机网络暂时找不到域名，确认地址无误，服务 Live，刚创建可等几分钟。
- `连接超时`：Render 免费服务可能在冷启动，等 1 分钟再试。
- `HTTP 401/403`：Token 不一致。
- `HTTP 404`：部署的后端接口不匹配。
- `HTTP 5xx`：服务器启动失败或内部错误，查看 Render Logs。
