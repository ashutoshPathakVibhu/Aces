// // you can use app's unique identifier here
const LOCAL_STORAGE_KEY = "toggle-bootstrap-theme";

const LOCAL_META_DATA = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));

const THEME_TOGGLER = document.getElementById("theme-toggler");

let isDark = LOCAL_META_DATA && LOCAL_META_DATA.isDark;

// check if user has already selected dark theme earlier
if (isDark) {
  enableDarkTheme();
} else {
  disableDarkTheme();
}


// /**
//  * Apart from toggling themes, this will also store user's theme preference in local storage.
//  * So when user visits next time, we can load the same theme.
//  *
//  */
function toggle() {
  isDark = !isDark;
  if (isDark) {
    enableDarkTheme();
  } else {
    disableDarkTheme();
  }
  const META = { isDark };
  localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(META));
}

function enableDarkTheme() {
  THEME_TOGGLER.innerHTML = "🌙 ";
  let d=document.getElementsByTagName("div");
  for(let i=0;i<d.length;i++){
    d[i].classList.add("navbar-dark");
    d[i].classList.add("bg-dark");
  }
  let b=document.getElementsByTagName("body");
  for(let i=0;i<b.length;i++){
    b[i].classList.add("navbar-dark");
    b[i].classList.add("bg-dark");
  }
  let n=document.getElementsByTagName("nav");
  for(let i=0;i<n.length;i++){
    n[i].classList.add("navbar-dark");
    n[i].classList.add("bg-dark");
  }
  let H2=document.getElementsByTagName("h2");
  for(let i=0;i<H2.length;i++){
    H2[i].classList.add("text-white");
  }
  let H4=document.getElementsByTagName("h4");
  for(let i=0;i<H4.length;i++){
    H4[i].classList.add("text-white");
  }
  let H6=document.getElementsByTagName("h6");
  for(let i=0;i<H6.length;i++){
    H6[i].classList.add("text-white");
  }
  let A=document.getElementsByTagName("a");
  for(let i=0;i<A.length;i++){
    A[i].classList.add("text-white");
  }
  let P=document.getElementsByTagName("p");
  for(let i=0;i<P.length;i++){
    P[i].classList.add("text-white");
  }
  let SPAN=document.getElementsByTagName("span");
  for(let i=0;i<SPAN.length;i++){
    SPAN[i].classList.add("text-white");
  }
  let STRONG=document.getElementsByTagName("strong");
  for(let i=0;i<STRONG.length;i++){
    STRONG[i].classList.add("text-white");
  }
  let SMALL=document.getElementsByTagName("small");
  for(let i=0;i<SMALL.length;i++){
    SMALL[i].classList.add("text-white");
  }
}

function disableDarkTheme() {
  THEME_TOGGLER.innerHTML = "🌞 ";
  let d=document.getElementsByTagName("div");
  for(let i=0;i<d.length;i++){
    d[i].classList.remove("navbar-dark");
    d[i].classList.remove("bg-dark");
  }
  let b=document.getElementsByTagName("body");
  for(let i=0;i<b.length;i++){
    b[i].classList.remove("navbar-dark");
    b[i].classList.remove("bg-dark");
  }
  let n=document.getElementsByTagName("nav");
  for(let i=0;i<n.length;i++){
    n[i].classList.remove("navbar-dark");
    n[i].classList.remove("bg-dark");
  }
  let H2=document.getElementsByTagName("h2");
  for(let i=0;i<H2.length;i++){
    H2[i].classList.remove("text-white");
  }
  let H4=document.getElementsByTagName("h4");
  for(let i=0;i<H4.length;i++){
    H4[i].classList.remove("text-white");
  }
  let H6=document.getElementsByTagName("h6");
  for(let i=0;i<H6.length;i++){
    H6[i].classList.remove("text-white");
  }
  let A=document.getElementsByTagName("a");
  for(let i=0;i<A.length;i++){
    A[i].classList.remove("text-white");
  }
  let P=document.getElementsByTagName("p");
  for(let i=0;i<P.length;i++){
    P[i].classList.remove("text-white");
  }
  let SPAN=document.getElementsByTagName("span");
  for(let i=0;i<SPAN.length;i++){
    SPAN[i].classList.remove("text-white");
  }
  let STRONG=document.getElementsByTagName("strong");
  for(let i=0;i<STRONG.length;i++){
    STRONG[i].classList.remove("text-white");
  }
  let SMALL=document.getElementsByTagName("small");
  for(let i=0;i<SMALL.length;i++){
    SMALL[i].classList.remove("text-white");
  }
}