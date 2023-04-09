function trigger () {
    activate_typing_effect();
}

function activate_typing_effect() {
    elements = document.querySelectorAll('.typed-text');
    for( el of elements ){
        txt = el.innerText;
        el.innerText = '';
        typing(el, txt);
    }
}

function typing (el, txt) {
    let p = document.createElement('p');
    p.style.display = 'inline';

    let cursor = document.createElement('span');
    cursor.classList.add('cursor');
    cursor.innerText = '|';

    el.appendChild(p);
    el.appendChild(cursor);

    let i = 0;
    let speed = 70;

    function typer(){
        if (i < txt.length) {
            p.innerText += txt.charAt(i);
            i++;
            setTimeout(typer, speed)
        }
    }

    typer();
}