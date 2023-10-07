(function () {

    'use strict'

    let x1 = null,
        y1 = null,
        lastY = 1

    document.addEventListener('touchstart', e => {
        const fTouch = e.touches[0]
        x1 = fTouch.clientX
        y1 = fTouch.clientY
    }, false)

    document.addEventListener('touchmove', e => {
        if (!x1 || !y1) return false

        let box = document.querySelector('#wrapper')

        let lastS = document.documentElement.scrollTop

        let x2 = e.touches[0].clientX,
            y2 = e.touches[0].clientY

        let xDiff = x2 - x1,
            yDiff = y2 - y1

        if (Math.abs(xDiff) < Math.abs(yDiff)) {
            if (yDiff > 0) {
                if (lastS === 0 && (lastY - e.touches[0].clientY) < 0 && e.cancelable) {
                    e.preventDefault()
                    e.stopPropagation()
                    box.style.transform = 'translateY(100px)'
                    setTimeout(() => {
                        location.reload()
                    }, 500)
                }
            }
        }

        x1 = null
        y1 = null

        lastY = e.touches[0].clientY
    }, {passive: false})

    document.addEventListener('touchcancel', e => {
        document.querySelector('#wrapper').style.transform = 'translateY(0)'
    })

})()