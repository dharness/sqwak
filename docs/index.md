---
layout: default
processing_methods:
    - None
    - FFT
    - MFC
    - Equalized
learning_algs:
    - Ordinary Least Squares
    - Ridge Regression
    - Lasso
    - Stochastic Gradient Descent
    - Bayesian Regression
completed_experiments:
    - "Ordinary Least Squares|None"
    - "Ordinary Least Squares|FFT"
    - "Stochastic Gradient Descent|None"
    - "Stochastic Gradient Descent|FFT"
---

<h1 id="#header-1" style="display: none"></h1>
<style>
    .experiment-matrix__cell {
        background: rgba(211, 84, 69, 0.5);
    }
    .experiment-matrix__cell--complete {
        background: rgba(114, 201, 56, 0.5)
    }
    .experiment-matrix__cell--complete:hover {
        cursor: pointer;
        background: rgb(114, 201, 56);
    }
    .experiment-matrix__cell:hover {
        background: rgb(211, 84, 69);
    }
</style>


## [](#header-2)Regression

<table>
    <tr>
        <th colspan="1"></th>
        <th colspan="{{4}}">Pre-processing</th>
    </tr>
    <tr>
        <th>Learning Algorithm</th>
        {% for method in page.processing_methods %}
            <td>{{ method }}</td>
        {% endfor %}
    </tr>
    {% for alg in page.learning_algs %}
        <tr>
            <td>{{ alg }}</td>
            {% for method in page.processing_methods %}
                {% assign ex_type = alg | append: "|" | append: method %}
                {% if page.completed_experiments contains ex_type %}
                        {% for ex in site.experiments %}
                            {% if ex.processing_method == method and ex.learning_alg == alg %}
                                {% assign ex_link = site.baseurl | append: ex.url %}
                            {% endif %}
                        {% endfor %}
                    <td class="experiment-matrix__cell--complete" onclick="window.location.href='{{ex_link}}'">
                    </td>
                {% else %}
                    <td class="experiment-matrix__cell"></td>
                {% endif %}
            {% endfor %}
        </tr>
    {% endfor %}

</table>

### [](#header-3)

#### [](#header-4) Experiment Lists

<ul>
{% for ex in site.experiments %}
{% if ex.layout != "fullscreen_graph" %}
    <li>
        <a href="{{ site.baseurl }}{{ ex.url }}">{{ ex.title }}</a>
    </li>
{% endif %}
{% endfor %}
</ul>


## [](#header-2)Classification