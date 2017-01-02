---
layout: default
---

<ul>
{% for ex in site.experiments %}
{% if ex.layout != "fullscreen_graph" %}
    <li>
        <a href="{{ site.baseurl }}{{ ex.url }}">{{ ex.title }}</a>
    </li>
{% endif %}
{% endfor %}
</ul>