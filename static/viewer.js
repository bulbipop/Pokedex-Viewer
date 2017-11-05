function updateCount() {
    let total = document.querySelectorAll('#pokedex > img').length
    let missing = document.querySelectorAll('#pokedex > .gray').length
    document.querySelector('#count').innerHTML = total - missing + '/' + total
}

function check_pokedex(pkdx) {
    let id = 0

    for (let bit of pkdx) {
        id++
        if (Number(bit)) {
            document.querySelector('#p' + id).className = ''
        }
    }
    updateCount()
}

function check_road(pkmns) {
    html = ''
    for (let word of pkmns.split(' ')) {
        if (word[0] == 'l') {
            html += '<div>' + word
        } else if (word != '') {
            html += document.querySelector('#p' + word).outerHTML + '</div>'
        }
    }
    document.querySelector('#road').innerHTML = html
}

function reqAjax(url, return_func) {
    let req = new XMLHttpRequest()
    req.open('POST', url)

    req.onreadystatechange = function () {
      if (req.readyState === 4) {
        if (req.status === 200) {
            return_func(req.responseText)
        }
      }
    }
    req.send()
}

function luaOrManual(checked) {
    if (checked) {
        reqAjaxPkdx = setInterval(reqAjax, 5000, '/_update', check_pokedex)
        reqAjaxPkmns = setInterval(reqAjax, 5000, '/_update_road', check_road)
        document.querySelector("#ontheroadagain").hidden = false
    } else {
        clearInterval(reqAjaxPkdx)
        clearInterval(reqAjaxPkmns)
        document.querySelector("#ontheroadagain").hidden = true
    }
}

function manualClick(el) {
    if (!document.querySelector("#auto").checked) {
        if (el.target.className == '') {
            el.target.className = 'gray'
        } else {
            el.target.className = ''
        }
        updateCount()
    }
}

document.querySelectorAll('img').forEach(function(el) {
    el.addEventListener('click', manualClick)
})
