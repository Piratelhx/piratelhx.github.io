---
layout: default
title: 标签
permalink: /tags/
---

<div class="tags-container">
  <header class="tags-header">
    <h1 class="tags-title">文章标签</h1>
    <p class="tags-subtitle">在这里发现、筛选和浏览文章。</p>
  </header>

  <section class="tags-filter-section">
    <h2 class="filter-title">所有标签</h2>
    <div class="tags-list">
      <button class="tag-filter-button active" data-tag="all">全部 ({{ site.posts.size }})</button>
      {% assign sorted_tags = site.tags | sort %}
      {% for tag in sorted_tags %}
        <button class="tag-filter-button" data-tag="{{ tag[0] | slugify }}">{{ tag[0] }} ({{ tag[1].size }})</button>
      {% endfor %}
    </div>
  </section>

  <main class="posts-grid">
    {% for post in site.posts %}
      <a class="post-card" href="{{ post.url | relative_url }}" data-tags="{% for tag in post.tags %}{{ tag | slugify }} {% endfor %}">
        <p class="post-card-date">{{ post.date | date: "%Y-%m-%d" }}</p>
        <h3 class="post-card-title">{{ post.title }}</h3>
        <div class="post-card-tags">
          {% for tag in post.tags %}
            <span class="post-card-tag">{{ tag }}</span>
          {% endfor %}
        </div>
      </a>
    {% endfor %}
  </main>
</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
    const filterButtons = document.querySelectorAll('.tag-filter-button');
    const postCards = document.querySelectorAll('.post-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            const selectedTag = this.getAttribute('data-tag');

            postCards.forEach(card => {
                const postTags = card.getAttribute('data-tags');
                if (selectedTag === 'all' || postTags.includes(selectedTag)) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});
</script>