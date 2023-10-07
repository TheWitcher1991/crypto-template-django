'use strict'

const walletTabs = (event, id) => {

    let tabcontent = document.querySelectorAll('.tab__content'),
        tablinks   = document.querySelectorAll('.tab__links');

    for (let i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = 'none'
    }

    for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(' tab__active', '');
    }

    document.querySelector(id).style.display = 'block'

    event.currentTarget.className += ' tab__active'

}