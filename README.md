# Django_blog_system

## 🚀 项目概览 (Overview)

这是一个基于 Django 开发的综合性 Web 平台，集成了**公开博客 (Blog)** 与 **私人笔记 (Learning Log)** 两大核心业务。项目不仅实现了基础的 CRUD（增删改查）功能，还深度集成了用户认证系统、多级权限校验机制以及响应式 UI 交互。

### 核心亮点：

* **双系统并行**：公共博客广场与完全私密的个人笔记本。
* **附件管理**：支持博文图片与文档附件的上传与下载。
* **多级权限**：<span style="color:red;">独立实现了“所有者校验”与“超级用户特权”逻辑。</span>
* **现代 UI**：基于 Bootstrap 5 的全站响应式设计，适配移动端。

---

## 🛠️ 技术架构 (Architecture)

项目遵循 Django 标准的 **MTV (Model-Template-View)** 架构：

* **Models**: 包含 `Topic`, `Entry`, `BlogPost` 等模型，支持外键关联与 `FileField` 附件存储。
* **Templates**: 采用模板继承，利用 `django-bootstrap5` 渲染响应式表单。
* **Views**: 封装了 `_check_topic_owner` 权限钩子，并集成了 `request.FILES` 处理流。

---

## ✨ 主要功能 (Features)

### 1. 账户认证系统 (Auth)

* 用户自主注册 (Register)、登录 (Login) 与注销 (Logout)。
* 注册后自动登录，登录状态全站 Session 跟踪。

### 2. 博客系统 (Blog with Attachments)

* **公共阅读**：所有人均可查看博文内容。
* **附件支持**：发布博文时支持上传 PDF、DOCX、图片等附件。
* **管理权限**：仅所有者可编辑博文；**超级用户 (Superuser)** 拥有全局删除权限。

### 3. 私人笔记本 (Learning Log)

* **数据隔离**：Topic 与用户绑定，非所有者无法通过 URL 越权访问。
* **交互优化**：集成 **Breadcrumbs (面包屑导航)**，支持多层级快速回退。

### 4. 安全性增强

* **二次确认流**：删除操作前弹出 Bootstrap 警示确认页，防止误删。
* **后端硬拦截**：视图层强制执行权限校验，确保 API 接口安全。

---

## 📦 安装与运行 (Setup)

1. **克隆项目**
```bash
git clone https://github.com/chenyitingkitty20051126-lgtm/Django_blog_system.git
cd 项目名

```


2. **安装依赖**
```bash
pip install -r requirements.txt

```


3. **初始化数据库**
```bash
python manage.py makemigrations
python manage.py migrate

```


4. **创建超级用户 (用于管理权限测试)**
```bash
python manage.py createsuperuser

```


5. **启动服务器**
```bash
python manage.py runserver

```


访问: `http://127.0.0.1:8000/`

---

## 📸 运行截图 (Screenshots)

| 登录界面 (Auth) | 博客列表 (Blog) | 笔记详情 (Note) |
| <img width="1654" height="785" alt="登陆界面" src="https://github.com/user-attachments/assets/a24bb475-04c8-47b3-93b4-16f8120dd3a1" /> | <img width="1112" height="802" alt="blog界面" src="https://github.com/user-attachments/assets/27b6fdc1-cdb0-4723-a049-b71bf8c4b1a4" /> | <img width="1919" height="1001" alt="topics界面" src="https://github.com/user-attachments/assets/ebccf10c-8b79-4050-a2e5-8987a4304343" /> |

---

## 📄 开源协议 (License)

本项目遵循 [MIT License](https://www.google.com/search?q=LICENSE)。
