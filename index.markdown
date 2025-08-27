---
layout: default
---

<div class="catalogue">
  {% for post in site.posts %}
    <a href="{{ post.url | prepend: site.baseurl }}" class="catalogue-item">
      <div>
        <time datetime="{{ post.date }}" class="catalogue-time">{{ post.date | date: "%B %d, %Y" }}</time>
        <h1 class="catalogue-title">{{ post.title }}</h1>
        <div class="catalogue-line"></div>

        <p>
          {% if post.description %}
            {{ post.description }}
          {% else %}
            {{ post.content | truncatewords: 30 | strip_html }}
          {% endif %}
        </p>

      </div>
    </a>
  {% endfor %}
</div>

{% if site.posts.size == 0 %}
<div class="catalogue">
  <div class="catalogue-item">
    <div>
      <h1 class="catalogue-title">欢迎来到我的博客！</h1>
      <div class="catalogue-line"></div>
      <p>还没有文章，敬请期待...</p>
    </div>
  </div>
</div>
{% endif %}

<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path | prepend: site.baseurl }}" class="left arrow">&#8592;</a>
  {% endif %}
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path | prepend: site.baseurl }}" class="right arrow">&#8594;</a>
  {% endif %}

  <span>{{ paginator.page }}</span>
</div>
