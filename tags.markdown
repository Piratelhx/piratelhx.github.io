---
layout: page
title: 标签
permalink: /tags/
---

<link rel="stylesheet" href="{{ '/assets/css/tags.css' | relative_url }}">

<div class="tags-header">
  <h1 class="tags-title">文章标签</h1>
</div>

<div class="tag-cloud">
{% assign sorted_tags = site.tags | sort %}
{% for tag in sorted_tags %}
  <a href="#{{ tag[0] | slugify }}" class="tag-item">
    {{ tag[0] }} ({{ tag[1].size }})
  </a>
{% endfor %}
</div>

{% for tag in sorted_tags %}
<section class="tag-section" id="{{ tag[0] | slugify }}">
  <h2 class="tag-section-title">{{ tag[0] }}</h2>
  <ul class="post-list">
    {% assign sorted_posts = tag[1] | sort: 'date' | reverse %}
    {% for post in sorted_posts %}
      <li class="post-list-item">
        <a href="{{ post.url | relative_url }}" class="post-link">{{ post.title }}</a>
        <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      </li>
    {% endfor %}
  </ul>
</section>
{% endfor %}