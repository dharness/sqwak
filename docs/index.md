---
layout: default
processing_methods:
    - None
    - FFT
    - MFC
learning_algs:
    regression:
        - Ordinary Least Squares
        - Stochastic Gradient Descent
        - Bayesian Regression
        - Ridge Regression
        - Lasso
    classification:
        - Decision tree 
        - SVM
completed_experiments:
    - "Ordinary Least Squares|None"
    - "Ordinary Least Squares|FFT"
    - "Ordinary Least Squares|MFC"
    - "Stochastic Gradient Descent|None"
    - "Stochastic Gradient Descent|FFT"
    - "Bayesian Regression|None"
    - "Bayesian Regression|FFT"
    - "Bayesian Regression|MFC"
    - "Lasso|None"
    - "Lasso|FFT"
    - "Ridge Regression|None"
    - "Ridge Regression|FFT"
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
    {% for alg in page.learning_algs.regression %}
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

_click a cell to view_

_click the top banner to come back home_

### [](#header-3)

## [](#header-2)Classification

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
    {% for class_alg in page.learning_algs.classification %}
        <tr>
            <td>{{ class_alg }}</td>
            {% for method in page.processing_methods %}
                {% assign ex_type = class_alg | append: "|" | append: method %}
                {% if page.completed_experiments contains ex_type %}
                        {% for class_ex in site.experiments %}
                            {% if class_ex.processing_method == method and class_ex.learning_algs == alg %}
                                {% assign class_ex_link = site.baseurl | append: class_ex.url %}
                            {% endif %}
                        {% endfor %}
                    <td class="experiment-matrix__cell--complete" onclick="window.location.href='{{class_ex_link}}'">
                    </td>
                {% else %}
                    <td class="experiment-matrix__cell"></td>
                {% endif %}
            {% endfor %}
        </tr>
    {% endfor %}

</table>

### [](#header-3)
_____________________________________________

#### [](#header-4) All Experiments
<ul>
{% for ex in site.experiments %}
{% if ex.layout != "fullscreen_graph" %}
    <li>
        <a href="{{ site.baseurl }}{{ ex.url }}">{{ ex.title }}</a>
    </li>
{% endif %}
{% endfor %}
</ul>