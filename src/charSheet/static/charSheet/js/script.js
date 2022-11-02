
window.onload = () => {
    document.querySelectorAll('.readonly').forEach(element => console.log(element.addEventListener("click", readonly)))
}

function readonly(evt) {
    evt.target.checked = true
}