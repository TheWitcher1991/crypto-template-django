'use strict'

document.addEventListener('mouseup', function (event) {
    let e = document.querySelector('.dt__popup');
    if (!e.contains(event.target)) e.classList.remove('dt__active')
})

const copyAddress = () => {
    let inp = document.createElement('input')
    inp.value = document.querySelector('.deposit-address').textContent;
    document.body.appendChild(inp)
    inp.select()

    if (document.execCommand('copy')) alert('Адрес скопирован')
    document.body.removeChild(inp)
}