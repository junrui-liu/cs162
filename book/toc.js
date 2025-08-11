// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded "><a href="syllabus.html"><strong aria-hidden="true">1.</strong> Syllabus 📝</a></li><li class="chapter-item expanded "><a href="calendar.html"><strong aria-hidden="true">2.</strong> Calendar 📅</a></li><li class="chapter-item expanded "><a href="lectures.html"><strong aria-hidden="true">3.</strong> Lectures 🧑‍🏫</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="lecture-notes/0624.html"><strong aria-hidden="true">3.1.</strong> Intro, Syntax I</a></li><li class="chapter-item expanded "><a href="lecture-notes/0625.html"><strong aria-hidden="true">3.2.</strong> Syntax II, Inference Rules</a></li><li class="chapter-item expanded "><a href="lecture-notes/0626.html"><strong aria-hidden="true">3.3.</strong> Operational Semantics</a></li><li class="chapter-item expanded "><a href="lecture-notes/0701.html"><strong aria-hidden="true">3.4.</strong> Inference Rules Workshop</a></li><li class="chapter-item expanded "><a href="lecture-notes/0702.html"><strong aria-hidden="true">3.5.</strong> Variables</a></li><li class="chapter-item expanded "><a href="lecture-notes/0703.html"><strong aria-hidden="true">3.6.</strong> Lambda Calculus</a></li><li class="chapter-item expanded "><a href="lecture-notes/0708.html"><strong aria-hidden="true">3.7.</strong> Call-by</a></li><li class="chapter-item expanded "><a href="lecture-notes/0709.html"><strong aria-hidden="true">3.8.</strong> Rice&#39;s Theorem, Soundness &amp; Completeness</a></li><li class="chapter-item expanded "><a href="lecture-notes/0710.html"><strong aria-hidden="true">3.9.</strong> Types</a></li><li class="chapter-item expanded "><a href="lecture-notes/0716.html"><strong aria-hidden="true">3.10.</strong> Type Soundness</a></li><li class="chapter-item expanded "><a href="lecture-notes/0717.html"><strong aria-hidden="true">3.11.</strong> Bidirectional Typing</a></li><li class="chapter-item expanded "><a href="lecture-notes/0722.html"><strong aria-hidden="true">3.12.</strong> Sum Types</a></li><li class="chapter-item expanded "><a href="lecture-notes/0723.html"><strong aria-hidden="true">3.13.</strong> Pattern Matching</a></li></ol></li><li class="chapter-item expanded "><a href="assignments.html"><strong aria-hidden="true">4.</strong> Homework Assignments 📚</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="assignments/hw1/index.html"><strong aria-hidden="true">4.1.</strong> HW1</a></li><li class="chapter-item expanded "><a href="assignments/hw2/index.html"><strong aria-hidden="true">4.2.</strong> HW2</a></li><li class="chapter-item expanded "><a href="assignments/hw3/index.html"><strong aria-hidden="true">4.3.</strong> HW3</a></li><li class="chapter-item expanded "><a href="assignments/hw4/index.html"><strong aria-hidden="true">4.4.</strong> HW4</a></li></ol></li><li class="chapter-item expanded "><a href="reflections.html"><strong aria-hidden="true">5.</strong> Reflections 💭</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="reflections/week1.html"><strong aria-hidden="true">5.1.</strong> Software Correctness</a></li><li class="chapter-item expanded "><a href="reflections/week2.html"><strong aria-hidden="true">5.2.</strong> Language Adoption</a></li><li class="chapter-item expanded "><a href="reflections/week3.html"><strong aria-hidden="true">5.3.</strong> Static Typing</a></li><li class="chapter-item expanded "><a href="reflections/week4.html"><strong aria-hidden="true">5.4.</strong> Feminism in PL</a></li><li class="chapter-item expanded "><a href="reflections/week5.html"><strong aria-hidden="true">5.5.</strong> Propositions as Types</a></li><li class="chapter-item expanded "><a href="reflections/week6.html"><strong aria-hidden="true">5.6.</strong> Future of PL</a></li></ol></li><li class="chapter-item expanded "><div><strong aria-hidden="true">6.</strong> Discussion Sections 🗣️</div></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split("#")[0];
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);
