function trigger() {
  activate_typing_effect();
}

async function activate_typing_effect() {
  elements = document.querySelectorAll(".typed-text");
  for (el of elements) {
    txt = el.innerText;
    el.innerText = "";
    await typing(el, txt);
  }
}

function typing(el, txt) {
  return new Promise((resolve) => {
    el.style.display = "block";
    let i = 0;
    const speed = 70;

    function typer() {
      if (i < txt.length) {
        el.innerHTML += txt.charAt(i);
        i++;
        setTimeout(typer, speed);
      } else {
        el.classList.add("final-typed-text");
        resolve();
      }
    }

    typer();
  });
}

function remove_field_errors_dialog() {
  dialog_error = document.querySelector(".error-form");
  back_wall = document.querySelector(".back-wall");

  dialog_error.remove();
  back_wall.remove();
}

function remove_field_sucess_dialog() {
  dialog_sucess = document.querySelector(".sucess-form");
  back_wall = document.querySelector(".back-wall");

  dialog_sucess.remove();
  back_wall.remove();
}
