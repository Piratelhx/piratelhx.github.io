---
layout: page
title: 标签
permalink: /tags/
---

<style>
.tag-cloud {
  margin: 2rem 0;
  text-align: center;
}

.tag-item {
  display: inline-block;
  margin: 0.3rem;
  padding: 0.4rem 0.8rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-decoration: none;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s ease;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.tag-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  text-decoration: none;
  color: white;
}

.tag-section {
  margin: 2rem 0;
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 10px;
  border-left: 4px solid #667eea;
}

.tag-title {
  color: #333;
  font-size: 1.3rem;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
}

.tag-title::before {
  content: "🏷️";
  margin-right: 0.5rem;
}

.tag-posts {
  list-style: none;
  padding: 0;
}

.tag-posts li {
  margin: 0.5rem 0;
  padding: 0.5rem;
  background: white;
  border-radius: 5px;
  border-left: 3px solid #667eea;
  transition: all 0.2s ease;
}

.tag-posts li:hover {
  transform: translateX(5px);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.tag-posts a {
  color: #333;
  text-decoration: none;
  font-weight: 500;
}

.tag-posts a:hover {
  color: #667eea;
}

.post-count {
  background: #667eea;
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 10px;
  font-size: 0.8rem;
  margin-left: 0.5rem;
}
</style>

# 📚 文章标签

<div class="tag-cloud">
{% assign sorted_tags = site.tags | sort %}
{% for tag in sorted_tags %}
  <a href="#{{ tag[0] | slugify }}" class="tag-item">
    {{ tag[0] }} <span class="post-count">{{ tag[1].size }}</span>
  </a>
{% endfor %}
</div>

---

{% assign sorted_tags = site.tags | sort %}
{% for tag in sorted_tags %}
<div class="tag-section" id="{{ tag[0] | slugify }}">
  <h3 class="tag-title">{{ tag[0] }}</h3>
  <ul class="tag-posts">
    {% assign sorted_posts = tag[1] | sort: 'date' | reverse %}
    {% for post in sorted_posts %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <small style="color: #666; margin-left: 0.5rem;">{{ post.date | date: "%Y-%m-%d" }}</small>
      </li>
    {% endfor %}
  </ul>
</div>
{% endfor %}