---
title: Frontend Coding
sidebar: Handbook
showTitle: true
---

# Frontend Coding

## Tech stack

- HTML5
- CSS3
- JavaScript
- pre-compiled JavaScript libraries

## Team board

The main repo for the frontend team (issues, discussions, etc.) is located at serpcompany/_websites

- [Discussions](https://github.com/serpcompany/_websites/discussions): For swipe files, assets, references, questions, announcements, discussions, etc.
- [Projects](https://github.com/serpcompany/_websites/projects?query=is%3Aopen): Specific initiatives, with issues & non-issue todos.
- [Issues](https://github.com/serpcompany/_websites/issues): Items and that need to be attended to (todos, etc.)

## Team process

1. Web team should first build templates in the [serpcompany/serp-theme](https://github.com/serpcompany/serp-bootstrap-theme) repository
2. Once approved, we add components to the Storybook
3. Then transfer the pages into Django

Eventually we won't need anything except our storybook designs.



## Code Quality

### Naming conventions

Always look around the codebase for naming conventions, and follow the best practices of the environment (e.g. use `camelCase` variables in JS, `snake_case` in Python).


### Linting & Testing

<ul>
<li><a href="https://eslint.org/" target="_blank" rel="nofollow">HTML Syntax: ESLint</a></li>
<li><a href="https://learntheweb.courses/topics/html-semantics-checklist/" target="_blank" rel="nofollow">Semantic HTML Checklist (need to get this automated)</a></li>
<li><a href="https://validator.w3.org/" target="_blank" rel="nofollow">W3C Markup Validation</a></li>
<li><a href="https://github.com/GoogleChrome/lighthouse-ci" target="_blank" rel="nofollow">Google Lighthouse CI</a></li>
</ul>


### Storybook Testing
<ul>
<li><a href="https://storybook.js.org/docs/html/writing-tests/accessibility-testing" target="_blank" rel="nofollow">Accessibility</a></li>
<li><a href="https://storybook.js.org/docs/html/writing-tests/test-runner" target="_blank" rel="nofollow"><strong>Test runner</strong></a> to automatically test your entire Storybook and catch broken stories.</li>
<li><a href="https://storybook.js.org/docs/html/writing-tests/visual-testing" target="_blank" rel="nofollow"><strong>Visual tests</strong></a> capture a screenshot of every story then compare it against baselines to detect appearance and integration issues</li>
<li><a href="https://storybook.js.org/docs/html/writing-tests/accessibility-testing" target="_blank" rel="nofollow"><strong>Accessibility tests</strong></a> catch usability issues related to visual, hearing, mobility, cognitive, speech, or neurological disabilities</li>
<li><a href="https://storybook.js.org/docs/html/writing-tests/interaction-testing" target="_blank" rel="nofollow"><strong>Interaction tests</strong></a> verify component functionality by simulating user behaviour, firing events, and ensuring that state is updated as expected</li>
<li><a href="https://storybook.js.org/docs/html/writing-tests/test-coverage" target="_blank" rel="nofollow"><strong>Coverage tests</strong></a> to measure how much of your code is covered by your tests</li>
<li><a href="https://storybook.js.org/docs/html/writing-tests/snapshot-testing" target="_blank" rel="nofollow"><strong>Snapshot tests</strong></a> detect changes in the rendered markup to surface rendering errors or warnings</li>
<li><a href="https://storybook.js.org/docs/html/writing-tests/stories-in-end-to-end-tests" target="_blank" rel="nofollow"><strong>End-to-end tests</strong></a> for simulating real user scenarios</li>
<li><a href="https://storybook.js.org/docs/html/writing-tests/stories-in-unit-tests" target="_blank" rel="nofollow"><strong>Unit tests</strong></a> for functionality</li>
</ul>


