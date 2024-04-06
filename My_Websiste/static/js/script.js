let menu = document.querySelector('#menu-bars');
let header = document.querySelector('header');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    header.classList.toggle('active');
}

window.onscroll = () =>{
    menu.classList.remove('fa-times');
    header.classList.remove('active');
}

let cursor1 = document.querySelector('.cursor-1');
let cursor2 = document.querySelector('.cursor-2');

window.onmousemove = (e) =>{
    cursor1.style.top = e.pageY + 'px';
    cursor1.style.left = e.pageX + 'px';
    cursor2.style.top = e.pageY + 'px';
    cursor2.style.left = e.pageX + 'px';
}

document.querySelectorAll('a').forEach(links =>{

    links.onmouseenter = () =>{
        cursor1.classList.add('active');
        cursor2.classList.add('active');
    }

    links.onmouseleave = () =>{
        cursor1.classList.remove('active');
        cursor2.classList.remove('active');
    }

});

// landing page starts
window.onscroll = function() {
    if (document.body.scrollTop > 0 || document.documentElement.scrollTop > 0 ) {
        document.getElementById('navbar').classList.add('scrolled');
    } else {
        document.getElementById('navbar').classList.remove('scrolled');
    }
}


// Function to toggle the "Read More" functionality
  var postText = posted-text.querySelector('.posted-text');
  var readMoreLink = posted-text.querySelector('.read-more');

  readMoreLinks.forEach(function(link) {
    link.addEventListener('click', function(event) {
      event.preventDefault();
      var blog = event.target.closest('.blog');
      toggleReadMore(blog);
    });
  });

// Function to toggle between truncated and full text
  function toggleText() {
    postText.classList.toggle('truncate');
    readMoreLink.textContent = postText.classList.contains('truncate') ? 'Read More' : 'Read Less';
  }

// Add event listener to the "Read More" link
  readMoreLink.addEventListener('click', toggleText);

// AOS
AOS.init({
    duration: 800,
});