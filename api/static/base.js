const filterbtn = document.querySelector('.nav-view');
const navDropBox = document.querySelector('.nav-drop');
let j = 0;
function checkNavDrop(e) {
    return (e.target === navDropBox ||
        e.target.parentElement === navDropBox ||
        e.target.parentElement.parentElement === navDropBox ||
        e.target.parentElement.parentElement.parentElement === navDropBox ||
        e.target.parentElement.parentElement.parentElement.parentElement === navDropBox)
}

document.addEventListener('click', (e) => {
    if (j % 2 == 0) {
        if (checkNavDrop(e)) {
            navDropBox.style.display = 'block';
        }
        if (e.target === filterbtn ||
            e.target.parentElement === filterbtn ||
            e.target.parentElement.parentElement === filterbtn ||
            e.target.parentElement.parentElement.parentElement === filterbtn) {
            navDropBox.style.display = 'block';
            j++;
            console.log(j);
            }
    } else {
        try {
            if (checkNavDrop(e)) {
                navDropBox.style.display = 'block';
            } else {
                console.log(e.target);
                navDropBox.style.display = 'none';
                j++;
                console.log(j);
            }
        } catch (error) {
            navDropBox.style.display = 'none';
            j++;
            console.log(j);
        }
    }
});


const hearts = document.querySelectorAll('.heart-svg');
hearts.forEach(heart => {
    let heartVar = 0;
    heart.addEventListener('click', () => {
        if (heartVar == 0) {
            heart.firstElementChild.style.fill = 'rgb(235, 0, 65, 1)';
            heartVar = 1;
        } else {
            heart.firstElementChild.style.fill = 'rgba(0, 0, 0, 0.5)';
            heartVar = 0;
        }
    })
})

document.addEventListener('load', () => {
    let html = document.querySelector("html");
    let cleanHTML = html.innerHTML.replace("&#xFEFF; ", '');
    html.innerHTML = cleanHTML;

})


