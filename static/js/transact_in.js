$(document).ready(function() {
    $('#myTable').DataTable();
    } );
    
    
function rowAdder() {
    // This function adds new row(s) to the table
    var table = document.getElementById("myTable");
    var row = table.insertRow(-1);
    cart_form = document.forms["cart-form"];
    prod_obj = cart_form.elements["prod-select"]
        .options[cart_form.elements["prod-select"].selectedIndex];
    row.insertCell(0).innerHTML = prod_obj.getAttribute("prod_sku");
    row.insertCell(1).innerHTML = prod_obj.getAttribute("prod_name");
    qty = document.getElementById("input_qty").value;
    row.insertCell(2).innerHTML = qty;
    price = document.getElementById("input_price").value;
    row.insertCell(3).innerHTML = price;
    row.insertCell(4).innerHTML = qty * price;
    row.insertCell(5).innerHTML = '<i class="fas fa-minus-circle text-danger" type="button" value="Delete" onclick="deleteRow(this)"></i>';
}

function deleteRow(r) {
var i = r.parentNode.parentNode.rowIndex;
document.getElementById("myTable").deleteRow(i);
}
