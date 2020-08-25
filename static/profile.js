let curcolor = "black";

$(document).ready(function(){
    let drawarea=document.getElementById("myCanvas");
    let rows=30;
    let cols=30;
    let id = 0;

    for(i=0; i<rows; i++){
        drawarea.innerHTML+="<tr class='table_row'></tr>";
    }

    for(j=0; j<cols; j++){
        $('tr').append("<td class='cell' id='p"+id+"'></td>");
        id++;
    }

    document.getElementById("myCanvas").addEventListener('mousedown', e => {

        if (!e.target.matches('td')) {
            return false;
        }
        setCellColor(e.target, curcolor);

    });

    document.getElementById("myCanvas").addEventListener('dblclick', e => {

        if (!e.target.matches('td')) {
            return false;
        }
        setCellColor(e.target, "white");

    });

    document.getElementById("cpicker").addEventListener('change', e => {

        curcolor = e.target.value;

    });

});


function setCellColor(cell, color) {
    cell.style.backgroundColor = color;
}


function id_color_array(u) {
    let pixels = {};
    let user = u;
    const cells = document.querySelectorAll('.cell');

    for (i = 0; i < cells.length; i++) {
      cells[i].id = "p" + i;
      if (cells[i].style.backgroundColor != "") {
        pixels['p' + i] = cells[i].style.backgroundColor;
      }
    }

    const data = JSON.stringify(pixels);
    const xhr = new XMLHttpRequest();

    xhr.open("POST", "/canvas/"+user);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(data);
}


function load(u) {
    let pixels = {};
    let user = u;
    const cells = document.querySelectorAll('.cell');
    for (i = 0; i < cells.length; i++) {
      cells[i].id = "p" + i;                          // setting IDs for the cells
    }
    let data;

    const xhr = new XMLHttpRequest();
    xhr.open("GET", "/canvas/"+user, true);        // making GET request
    xhr.send();

    xhr.onload = function () {
      data = JSON.parse(xhr.responseText);
      let keys = Object.keys(data);
      for (let i = 0; i < keys.length; i++) {
        let color = data[keys[i]];                // changing the color with the data received
        document.getElementById(keys[i]).style.backgroundColor = color;
      }
    }
}


function wipe() {
    const cells = document.querySelectorAll('.cell');
    for (i = 0; i < cells.length; i++) {
        setCellColor(document.getElementById("p" + i), "white");
    }
}