'use strict'

const RegError = text => {
    document.body.innerHTML += `
        <div class="msg__box msg__box-active">
             <p><i class="fa-solid fa-info"></i> ${text}</p>
            <div class="msg__progress">
        </div>
    `
    setTimeout(() => {
        document.querySelector('.msg__box').remove()
    }, 7000)
}