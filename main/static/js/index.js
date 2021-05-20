let button = document.querySelector('#button')
button.addEventListener('click', change_color)

function change_color() {
    if (document.body.className == '') {
        document.body.className = 'body1'
        document.cookie = "claas="
    } else if (document.body.className = 'body1') {
        // document.body.style='background:red;'
        document.body.className = ''
        document.cookie = "claas="
    }

}