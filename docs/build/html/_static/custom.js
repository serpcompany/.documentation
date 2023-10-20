document.addEventListener("DOMContentLoaded", function() {
    const tocSections = document.querySelectorAll(".wy-menu-vertical ul");

    tocSections.forEach((section) => {
        const parentListItem = section.parentElement;

        if (parentListItem.tagName === "LI") {
            const expandSpan = document.createElement("span");
            expandSpan.className = "toctree-expand";
            expandSpan.innerHTML = "▶"; // a right-pointing triangle
            parentListItem.insertBefore(expandSpan, parentListItem.firstElementChild);

            expandSpan.addEventListener("click", function() {
                if (parentListItem.classList.contains("current")) {
                    parentListItem.classList.remove("current");
                    expandSpan.innerHTML = "▶";
                } else {
                    parentListItem.classList.add("current");
                    expandSpan.innerHTML = "▼"; // a down-pointing triangle
                }
            });
        }
    });
});

window.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.wy-menu-vertical li.toctree-l1').forEach((li) => {
        li.addEventListener('click', function(e) {
            if (e.target === this || e.target.tagName === 'A' && e.target.parentElement === this) {
                this.classList.toggle('current');
            }
        });
    });
});
