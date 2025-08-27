---
layout: default
title: Home
---

<ul class="post-list">
  {% for post in paginator.posts %}
    <li class="post-list-item">
      <p class="post-meta">{{ post.date | date: "%Y年%m月%d日" }}</p>
      <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <div class="post-excerpt">
        {{ post.description | strip_html | truncatewords: 30 }}
      </div>
      <div class="post-tags">
        {% for tag in post.tags %}
          {% assign tag_slug = tag | slugify %}
          <a href="{{ site.baseurl }}/tags/#{{ tag_slug }}" 
             class="post-tag {% if tag_slug == 'rag' %}rag{% elsif tag_slug == 'ai' %}ai{% else %}tech{% endif %}">
            {{ tag }}
          </a>
        {% endfor %}
      </div>
    </li>
  {% endfor %}
</ul>

<!-- Pagination -->
<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path }}" class="previous">上一页</a>
  {% else %}
    <span class="previous disabled">上一页</span>
  {% endif %}
  
  <span class="page_number">第 {{ paginator.page }} 页 / 共 {{ paginator.total_pages }} 页</span>
  
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path }}" class="next">下一页</a>
  {% else %}
    <span class="next disabled">下一页</span>
  {% endif %}
</div>
