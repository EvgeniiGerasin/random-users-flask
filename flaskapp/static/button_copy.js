function myFunction(id) {
    a = document.querySelector(id).textContent
    navigator.clipboard.writeText(a)
}
