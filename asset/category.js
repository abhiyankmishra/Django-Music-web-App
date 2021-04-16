


$(document).ready(function (){
    $('#cid').append($('<option>').text('-Select Category-'))
    $('#stext').keyup(function(){
//    $('#btn').click(function(){--------------use it ,if you want to use btn
       $.getJSON('http://127.0.0.1:8000/usrsrchsngjson/',{ajax:true,pat:$('#stext').val()},function (data) {
       htm=""
       htm+="<div class='row'>"





       $.each(data,function(index,item){
                        htm+="<div class='col-md-4'>"
						htm+="<div class='category-item'>"
						htm+="<img src='/static/"+item[11]+"' ><br>"
						htm+="<div class='ci-text'>"
						htm+="<h4>"+item[3]+"</h4>"
						htm+="<p>"+item[4]+"/p>"
						htm+="</div>"
						htm+="<a href='/usrplaysngpg?sng="+item+"' class='ci-link'><i class='fa fa-play'></i></a>"
						htm+="</div><br>"
					    htm+="</div>"
    })
    htm+="</div>"
    $('#result').html(htm)
    })
    })

    $.getJSON('http://127.0.0.1:8000/catdatashowjson/',{ajax:true},function (data) {

       $.each(data,function(index,item){

        $('#cid').append($('<option>').text(item[1]).val(item[0]))
       })
    })


    $('#cid').change(function () {

     $.getJSON('http://127.0.0.1:8000/subcatdatashowjson/',{ajax:true,cid:$('#cid').val()},function (data) {

      $('#scid').empty()

          $('#scid').append($('<option>').text('-Select SubCategory-'))

       $.each(data,function(index,item){


        $('#scid').append($('<option>').text(item[2]).val(item[0]))

       })

    })


    })

})
