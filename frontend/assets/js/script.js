var typed=new Typed(".auto-type",{strings:["Contents","Concepts","Passion"],typeSpeed:125,backSpeed:150,loop:!0,cursorChar:""}),typed1=new Typed(".auto-type1",{strings:["Contents","Concepts","Passion"],typeSpeed:125,backSpeed:150,loop:!0,cursorChar:""});

var faq = document.getElementsByClassName('faq-page');
var i;
for (i = 0; i < faq.length; i++) {
  faq[i].addEventListener('click', function () {
    /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
    this.classList.toggle('active');

    var body = this.nextElementSibling;
    if (body.style.display === 'block') {
      body.style.display = 'none';
    } else {
      body.style.display = 'block';
    }
  });
}
