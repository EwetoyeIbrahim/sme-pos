$(document).ready(function() {
    var t = $('#myTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'print',
                customize: function ( win ) {
                    $(win.document.body)
                        .css( 'font-size', '10pt' )
                        .prepend(
                            '<img src="http://datatables.net/media/images/logo-fade.png" style="position:absolute; top:0; left:0;" />'
                        );
 
                    $(win.document.body).find( 'table' )
                        .addClass( 'compact' )
                        .css( 'font-size', 'inherit' );
                }
            }
        ]
    });
        var counter = 1;
        $('#addRow').on( 'submit', function () {
            var row = table.insertRow(-1);
            cart_form = document.forms["cart-form"];
            prod_obj = cart_form.elements["prod-select"]
                .options[cart_form.elements["prod-select"].selectedIndex];
            //row.insertCell(0).innerHTML = prod_obj.getAttribute("prod_sku");
            //row.insertCell(1).innerHTML = prod_obj.getAttribute("prod_name");
            qty = document.getElementById("input_qty").value;
            //row.insertCell(2).innerHTML = qty;
            price = document.getElementById("input_price").value;
            //row.insertCell(3).innerHTML = price;
            //row.insertCell(4).innerHTML = qty * price;
            //row.insertCell(5).innerHTML = '<i class="fas fa-minus-circle text-danger" type="button" value="Delete" onclick="deleteRow(this)"></i>';}
        
            t.row.add( [
                prod_obj.getAttribute("prod_sku"),
                prod_obj.getAttribute("prod_name"),
                qty,
                price,
                qty * price,
                '<i class="fas fa-minus-circle text-danger" type="button" value="Delete" onclick="deleteRow(this)"></i>',
            ] ).draw( false );
     
        } );
    } );


  
function rowAdder() {
    // This function adds new row(s) to the table
    var t_body = document.getElementById("myTable").getElementsByTagName("tbody")[0];
    console.log(t_body)
    var row = t_body.insertRow(-1);
    cart_form = document.forms["cart-form"];
    prod_obj = cart_form.elements["prod-select"]
        .options[cart_form.elements["prod-select"].selectedIndex];
    row.insertCell(0).innerHTML = prod_obj.getAttribute("prod_sku");
    name_cell = row.insertCell(1)
    name_cell.setAttribute("id", prod_obj.getAttribute("value"))
    name_cell.innerHTML = prod_obj.getAttribute("prod_name");
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

function printData()
{
   var divToPrint=document.getElementById("myTable");
   newWin= window.open("");
   newWin.document.write(divToPrint.outerHTML);
   newWin.print();
   newWin.close();
}

$('#printbtn').on('click',function(){
printData();
})