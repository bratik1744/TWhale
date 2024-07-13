document.addEventListener("DOMContentLoaded", function(){
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl);
    });
  });



// function search_animal() {
//     let input = document.getElementById('searchFilter').value
//     input = input.toLowerCase();
//     let x = document.getElementsByClassName('list-group-item');
  
//     for (i = 0; i < x.length; i++) {
//       if (x[i].innerHTML.toLowerCase().includes(input)) {
//         x[i].style.display = "block";
//         console.log(x[i].getAttribute("title"));
//       }
//       else {
//         x[i].style.display = "none";
//       }
//     }
// }


function filterList() {
    var input, filter, ul, li, a, i, txtValue, titleValue;
    input = document.getElementById('searchFilter');
    filter = input.value.toLowerCase();
    ul = document.getElementById("tickerList");
    li = ul.getElementsByClassName('list-group-item');
  
    for (i = 0; i < li.length; i++) {
      a = li[i];
      txtValue = a.textContent || a.innerText;
      titleValue = a.getAttribute("data-description");
      console.log(titleValue);
      if (txtValue.toLowerCase().includes(filter) || (titleValue && titleValue.toLowerCase().includes(filter))) {
        li[i].style.display = "block";
      } else {
        li[i].style.display = "none";
      }
    }
  }