(function () {

    'use strict'

    document.addEventListener('DOMContentLoaded', function (e) {

        document.addEventListener('mouseup', function (event) {
            let e = document.querySelector('.bell__popup');
            if (!e.contains(event.target)) e.classList.remove('bell__pop-active')
        })


        document.querySelector('.bth__popup')?.addEventListener('click', function (e) {
            if (e.target.closest('.bth-p__container') === null) {
                this.style.display = 'none'
                e.target.closest('.bth-p__container').style.display = 'none'
            }
        })

        let popups = document.querySelectorAll('.bth__popup')

        for (let i = 0; i < popups.length; i++) {
            popups[i].addEventListener('click', function (e) {
                if (e.target.closest('.bth-p__container') === null) {
                    this.style.display = 'none'
                    e.target.closest('.bth-p__container').style.display = 'none'
                }
            })
        }

        document.querySelector('#defTab')?.click()

        document.querySelector('.dt__wrap')?.addEventListener('click', e => {
            e.preventDefault()
            document.querySelector('.dt__popup').classList.toggle('dt__active')
        })

        document.querySelector('.bell__bth')?.addEventListener('click', e => {
            e.preventDefault()
            document.querySelector('.bell__popup').classList.toggle('bell__pop-active')
        })

        /*document.querySelector('.cart__add')?.addEventListener('click', e => {
            e.preventDefault()
            document.querySelector('.bth__popup').style.display = 'flex'
            document.querySelector('.bth-p__container').style.display = 'block'
        })*/

        document.querySelector('.cart__get')?.addEventListener('click', e => {
            e.preventDefault()
            // document.querySelector('.popup__get').style.display = 'block'
            document.querySelector('.bth__get-p').style.display = 'flex'
            document.querySelector('.get__popup').style.display = 'block'
        })

        document.querySelector('.cart__add')?.addEventListener('click', e => {
            e.preventDefault()
            document.querySelector('.bth__farm-p').style.display = 'flex'
            document.querySelector('.farm__popup').style.display = 'block'
        })

        document.querySelector('.cart__chart')?.addEventListener('click', e => {
            e.preventDefault()
            document.querySelector('.bth__chart-p').style.display = 'flex'
            document.querySelector('.chart__popup').style.display = 'block'
        })

        document.querySelector('.cart__send')?.addEventListener('click', e => {
            e.preventDefault()
            document.querySelector('.popup__send').style.display = 'block'
        })

        let popupClose = document.querySelectorAll('.pop__close')

        for (let i = 0; i < popupClose.length; i++) {
            popupClose[i].addEventListener('click', function (e) {
                e.preventDefault()
                this.parentElement.parentElement.style.display = 'none'
            })
        }

    })

})()