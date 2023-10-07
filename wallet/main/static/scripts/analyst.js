'use strict'

const analystTabs = (event, id) => {

    let tabcontent = document.querySelectorAll('.chart__content'),
        tablinks   = document.querySelectorAll('.line__links');

    for (let i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = 'none'
    }

    for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(' line__active', '');
    }

    document.querySelector(id).style.display = 'block'

    event.currentTarget.className += ' line__active'

}

document.addEventListener('DOMContentLoaded', function (e) {

    document.querySelector('.cb__popup')?.addEventListener('click', e => {
        e.preventDefault()
        // document.querySelector('.popup__get').style.display = 'block'
        document.querySelector('.bth__popup').style.display = 'flex'
        document.querySelector('.bth-p__container').style.display = 'block'
    })

})
