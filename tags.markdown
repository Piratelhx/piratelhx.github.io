---
layout: page
title: 标签
permalink: /tags/
---

# 文章标签

这里将显示所有文章的标签分类。

{% assign tags = site.tags | sort %}
{% for tag in tags %}
  <h3>{{ tag[0] }}</h3>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}