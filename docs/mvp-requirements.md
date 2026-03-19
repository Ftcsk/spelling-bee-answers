# Spelling Bee Answers — MVP 需求文档

**版本：** v1.0  
**日期：** 2026-03-19  
**负责人：** 小战（战略顾问）

---

## 一、产品目标

打造一个专注于 NYT Spelling Bee 每日答案的内容型 SEO 站，目标：

- 6个月内进入 "spelling bee answers today" 关键词 Google 前5
- 月均 UV 达到 30,000+
- 通过广告 + 联盟变现，月收入 $200+

**核心价值主张：** 更新最快、存档最全、附带词义解释 — 三点差异化超越现有竞品。

---

## 二、目标用户

- 每天玩 NYT Spelling Bee 的英语用户（主要在美国）
- 卡关时搜索答案的休闲玩家
- 学习英语词汇的学习者

---

## 三、核心功能（MVP 范围）

### 3.1 今日答案页（P0）
- 展示当日所有有效单词列表
- 高亮标注 Pangram（全字母词）
- 显示字母格（中心字母 + 外围6个字母）
- 更新时间戳（UTC 0:00 后自动/手动更新）

### 3.2 历史存档页（P0）
- 按日期索引，URL 格式：`/answers/YYYY-MM-DD`
- 支持按月浏览
- 从2024年起补全历史数据

### 3.3 词义详情页（P1 — 差异化核心）
- URL 格式：`/words/[word]`
- 包含：词义、词性、例句、发音
- 关联出现该词的历史日期

### 3.4 提示页（P1）
- URL：`/hints/today`
- 分级提示：字母数量 → 首字母 → 完整答案
- 降低跳出率，增加停留时长

### 3.5 搜索功能（P2）
- 按日期搜索历史答案
- 按单词搜索出现记录

---

## 四、页面结构

```
/                          首页（今日答案）
/answers/                  存档列表页
/answers/YYYY-MM-DD        每日答案详情页
/hints/today               今日提示页
/words/                    词汇索引页
/words/[word]              单词详情页
/about                     关于页
/sitemap.xml               站点地图（SEO必须）
```

---

## 五、技术栈

| 层级 | 技术选型 | 理由 |
|------|----------|------|
| 框架 | Astro | 静态生成，Core Web Vitals 优秀，SEO友好 |
| 样式 | Tailwind CSS | 快速开发，移动端优先 |
| 数据存储 | JSON 文件 / Markdown | MVP阶段无需数据库，简单可维护 |
| 部署 | Vercel / Cloudflare Pages | 免费，全球CDN，自动部署 |
| 域名 | spellingbeeanswers.today 或类似 | 含关键词，有利于SEO |

**SEO 技术要求：**
- 每页生成 `<title>` + `<meta description>`（含日期关键词）
- Article schema markup（Google 精选摘要）
- FAQ schema（提示页）
- sitemap.xml 自动生成
- robots.txt 配置
- Open Graph 标签（社交分享）

---

## 六、关键词策略

### 核心主词
- `spelling bee answers today`（月搜索量 ~60,000）
- `nyt spelling bee answers`（月搜索量 ~40,000）
- `spelling bee answers [日期]`（长尾积累）

### 长尾词矩阵

| 意图 | 关键词示例 |
|------|-----------|
| 今日答案 | spelling bee answers today march 2026 |
| Pangram | spelling bee pangram today |
| 历史查询 | spelling bee answers yesterday / archive |
| 词义学习 | spelling bee word definitions |
| 攻略技巧 | spelling bee hints today / tips |

### URL SEO 规范
- 今日页：`/` 或 `/answers/today`（301重定向到当日日期URL）
- 日期页：`/answers/2026-03-19`（含日期，精准匹配搜索词）
- Title 模板：`NYT Spelling Bee Answers Today - March 19, 2026 | [SiteName]`

---

## 七、变现方向

### 阶段一：广告（上线即可）
- Google AdSense 申请（需要一定内容量）
- 或 Ezoic（门槛更低）
- 预期 CPM：$3–8，月收入 $150–600（稳定后）

### 阶段二：联盟营销（上线1个月后）
- NYT 订阅联盟（官方有 affiliate 计划）
- 词汇学习工具推荐（Vocabulary.com、Quizlet）

### 阶段三：邮件订阅（上线3个月后）
- 每日答案邮件推送
- 积累私域流量，降低对搜索引擎依赖

---

## 八、上线里程碑

| 阶段 | 时间 | 目标 |
|------|------|------|
| MVP 搭建 | 第1周 | 今日答案页 + 基础存档页上线 |
| 内容补全 | 第2–4周 | 补全2024年至今历史数据，词义页上线 |
| SEO 优化 | 第2个月 | Schema markup、sitemap、速度优化 |
| 流量增长 | 第3–6个月 | 目标进入核心词前5，月UV 30,000+ |
| 变现启动 | 第2个月 | AdSense 申请，联盟链接接入 |

---

## 九、验收标准

- [ ] 今日答案页在 NYT 发布后30分钟内更新
- [ ] 历史存档页覆盖2024年至今所有日期
- [ ] Lighthouse 性能分数 ≥ 90（移动端）
- [ ] 每页包含正确的 title、meta description、schema markup
- [ ] sitemap.xml 正确生成并提交 Google Search Console
- [ ] 移动端布局无错位，字体可读性良好
