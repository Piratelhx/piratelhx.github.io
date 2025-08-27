---
layout: page
title: 标签
permalink: /tags/
---

<style>
/* 全局样式重置 */
.tags-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

/* 标题样式 */
.page-title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 3rem;
}

/* Tag云样式 - 3D效果 */
.tag-cloud {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
  margin: 3rem 0;
  padding: 2rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.tag-bubble {
  position: relative;
  display: inline-flex;
  align-items: center;
  padding: 0.8rem 1.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-decoration: none;
  border-radius: 50px;
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
  overflow: hidden;
}

.tag-bubble::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
  transition: left 0.5s;
}

.tag-bubble:hover {
  transform: translateY(-8px) scale(1.05);
  box-shadow: 0 15px 35px rgba(102, 126, 234, 0.6);
  text-decoration: none;
  color: white;
}

.tag-bubble:hover::before {
  left: 100%;
}

.tag-count {
  background: rgba(255,255,255,0.3);
  padding: 0.3rem 0.6rem;
  border-radius: 20px;
  font-size: 0.8rem;
  margin-left: 0.5rem;
  font-weight: 700;
}

/* 分类卡片样式 */
.tags-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.tag-card {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
  border: 1px solid #e1e8ed;
  position: relative;
  overflow: hidden;
}

.tag-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.tag-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}

.tag-card-title {
  display: flex;
  align-items: center;
  font-size: 1.4rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 1.5rem;
}

.tag-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 1rem;
  font-size: 1.2rem;
}

.tag-posts-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.tag-post-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  margin: 0.5rem 0;
  background: #f8f9fa;
  border-radius: 12px;
  transition: all 0.3s ease;
  border-left: 4px solid transparent;
}

.tag-post-item:hover {
  background: #e3f2fd;
  border-left-color: #667eea;
  transform: translateX(10px);
}

.tag-post-item a {
  color: #2c3e50;
  text-decoration: none;
  font-weight: 600;
  flex: 1;
}

.tag-post-item a:hover {
  color: #667eea;
}

.post-date {
  color: #7f8c8d;
  font-size: 0.85rem;
  background: white;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  border: 1px solid #e1e8ed;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .tags-grid {
    grid-template-columns: 1fr;
  }
  
  .tag-cloud {
    padding: 1rem;
  }
  
  .tag-bubble {
    padding: 0.6rem 1rem;
    font-size: 0.85rem;
  }
}
</style>

<div class="tags-container">
  <h1 class="page-title">🏷️ 文章标签</h1>
  
  <!-- Tag云 -->
  <div class="tag-cloud">
    {% assign sorted_tags = site.tags | sort %}
    {% for tag in sorted_tags %}
      <a href="#{{ tag[0] | slugify }}" class="tag-bubble">
        {{ tag[0] }}
        <span class="tag-count">{{ tag[1].size }}</span>
      </a>
    {% endfor %}
  </div>
  
  <!-- 分类卡片 -->
  <div class="tags-grid">
    {% assign sorted_tags = site.tags | sort %}
    {% for tag in sorted_tags %}
    <div class="tag-card" id="{{ tag[0] | slugify }}">
      <h3 class="tag-card-title">
        <div class="tag-icon">🏷️</div>
        {{ tag[0] }}
      </h3>
      <ul class="tag-posts-list">
        {% assign sorted_posts = tag[1] | sort: 'date' | reverse %}
        {% for post in sorted_posts %}
        <li class="tag-post-item">
          <a href="{{ post.url }}">{{ post.title }}</a>
          <span class="post-date">{{ post.date | date: "%m-%d" }}</span>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endfor %}
  </div>
</div>