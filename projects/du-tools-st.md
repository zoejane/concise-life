# 自怼圈 st 统计工具

## Plan

- [DebugUself/du4proto at DU_tools](https://github.com/DebugUself/du4proto/tree/DU_tools)
- 跟随 commits history 系统学习整个工具是怎么一步步 develop 出来的
- 了解现有 st 代码大意
- 修订现有代码的错误

### 目标

- 跟随 commits history, 记录项目的展开，了解代码到意思

### commits hitory 学习笔记

	
#### br(init.) collection tools for DU

.gitignore

- Ulysses `.Ulysses*·`
- mac `.DS_Store`
- python 版本 gitignore

LICENCE

- BSD 2-Clause License
- Copyright (c) 2017, Debug U self ~ 自怼圈

README.md

- 标题
- 背景
- 分析
- 进展

```
# 自制工具集
~ 各种嗯哼的观察...

## 背景

## 分析

## 进展

170406 DAMA init
```

#### feat(st) 原型内测

st/README.md

```
# st
~ status for DU

## 原型

- 快速逐步自动化统计怼员行为

## 进展

- 170407 迁移
- 170315 原型
- 170310 起念
```

gh_comments.py

- 作用：抓取 github 的 comments 内容
- 环境: pygithub + python2 （pip install PyGithub）
- 展现形式

```
Zoom.Quiet
2017-04-03 12:56:02
S01E01/du_s01e01_zoejane.md : 11
@zoejane 最好直接文字, 这样大家好针对性的讨论? 
```

PyGithub

- [Main class: Github — PyGithub 1.25.2 documentation](http://pygithub.readthedocs.io/en/latest/github.html)

```
for repo in g.get_user().get_repos():
    print repo.name
```
