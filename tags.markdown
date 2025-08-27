---
layout: page
title: 标签
permalink: /tags/
---

<link rel="stylesheet" href="{{ '/assets/css/tags.css' | relative_url }}">

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
      <article class="post-card" data-tags="{% for tag in post.tags %}{{ tag | slugify }} {% endfor %}">
        <p class="post-card-date">{{ post.date | date: "%Y-%m-%d" }}</p>
        <a href="{{ post.url | relative_url }}" class="post-card-title">{{ post.title }}</a>
        <div class="post-card-tags">
          {% for tag in post.tags %}
            <a href="#" class="post-card-tag">{{ tag }}</a>
          {% endfor %}
        </div>
      </article>
    {% endfor %}
  </main>
</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
    const filterButtons = document.querySelectorAll('.tag-filter-button');
    const postCards = document.querySelectorAll('.post-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', function () {
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            const selectedTag = this.getAttribute('data-tag');

            // Filter posts
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