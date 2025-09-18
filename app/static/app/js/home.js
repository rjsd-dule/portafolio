// Toggle sidebar abierto/cerrado (diferencia móvil y desktop)
document.getElementById("toggleSidebar").addEventListener("click", function () {
    const sidebar = document.getElementById("sidebar");
    // No diferenciamos móvil o desktop, solo toggle de 'closed'
    sidebar.classList.toggle("closed");
});


// Dropdown perfil
const profileMenu = document.getElementById("profileMenu");
const profileCard = document.getElementById("profileCard");
const profileBtn = document.getElementById("profileBtn");
const profileArrow = document.getElementById("profileArrow");

function toggleProfileDropdown(e) {
    e.stopPropagation();
    profileCard.classList.toggle("show");
    profileMenu.classList.toggle("active");
    const expanded = profileMenu.getAttribute("aria-expanded") === "true";
    profileMenu.setAttribute("aria-expanded", String(!expanded));
}

profileBtn.addEventListener("click", toggleProfileDropdown);
profileArrow.addEventListener("click", toggleProfileDropdown);

document.addEventListener("click", function () {
    if (profileCard.classList.contains("show")) {
        profileCard.classList.remove("show");
        profileMenu.classList.remove("active");
        profileMenu.setAttribute("aria-expanded", "false");
    }
});
