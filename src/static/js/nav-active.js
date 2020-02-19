let navs = document.getElementsByClassName("nav-link");
for (let i=0; i<navs.length; i++) {
    if (navs[i].text.includes('New') !== true) {
        // nav-link elements from nav that can get class 'active'
        if (navs[i].text === linkActive) {
            navs[i].classList.add("active");
        }
    }
}
