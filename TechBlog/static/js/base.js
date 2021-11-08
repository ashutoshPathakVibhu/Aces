// // you can use app's unique identifier here
// const LOCAL_STORAGE_KEY = "toggle-bootstrap-theme";

// const LOCAL_META_DATA = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));

// // you can change this url as needed
// const DARK_THEME_PATH = "https://bootswatch.com/4/cyborg/bootstrap.min.css";

// const DARK_STYLE_LINK = document.getElementById("dark-theme-style");
// const THEME_TOGGLER = document.getElementById("theme-toggler");

// let isDark = LOCAL_META_DATA && LOCAL_META_DATA.isDark;

// // check if user has already selected dark theme earlier
// if (isDark) {
//   enableDarkTheme();
// } else {
//   disableDarkTheme();
// }


// /**
//  * Apart from toggling themes, this will also store user's theme preference in local storage.
//  * So when user visits next time, we can load the same theme.
//  *
//  */
// function toggleTheme() {
//   isDark = !isDark;
//   if (isDark) {
//     enableDarkTheme();
//   } else {
//     disableDarkTheme();
//   }
//   const META = { isDark };
//   localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(META));
// }

// function enableDarkTheme() {
//   DARK_STYLE_LINK.setAttribute("href", DARK_THEME_PATH);
//   THEME_TOGGLER.innerHTML = "🌙 ";
// }

// function disableDarkTheme() {
//   DARK_STYLE_LINK.setAttribute("href", "");
//   THEME_TOGGLER.innerHTML = "🌞 ";
// }

$(document).ready(function(){
  $("#selector").change(function(){
    $("body").toggleClass("navbar-dark bg-dark");
    $("nav").toggleClass("navbar-dark bg-dark");
    $(".custom-control-label").toggleClass("text-white");
    $("h2").toggleClass("text-white");
    $("h6").toggleClass("text-white");
    $("h4").toggleClass("text-white");
    $("div").toggleClass("bg-dark");
    $("a").toggleClass("text-white");
    $("p").toggleClass("text-white");
    $("span").toggleClass("text-white");
    $("strong").toggleClass("text-white");
    $("small").toggleClass("text-white");
    $(".card-title").toggleClass("text-white");
    $(".card-text").toggleClass("text-white");
    // $(".btn").toggleClass("text-white");
    $(".fas").toggleClass("text-white");
  });
});