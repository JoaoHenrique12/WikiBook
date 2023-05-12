function trigger () {
    activate_typing_effect();
}

async function activate_typing_effect() {
    elements = document.querySelectorAll('.typed-text');
    for( el of elements ){
        txt = el.innerText;
        el.innerText = '';
        await typing(el, txt);
    }
}

function typing(el, txt) {
  return new Promise(resolve => {
    el.style.display = 'block';
    let i = 0;
    const speed = 70;

    function typer() {
      if (i < txt.length) {
        el.innerHTML += txt.charAt(i);
        i++;
        setTimeout(typer, speed);
      } else {
        el.classList.add('final-typed-text');
        resolve();
      }
    }

    typer();
  });
}

