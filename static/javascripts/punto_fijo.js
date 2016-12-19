$(function(){
//    var board = JXG.JSXGraph.initBoard('box', {boundingbox: [-10, 10, 10, -10],
//                                              axis:true,
//                                              zoom: {
//                                                  factorX:1.25,
//                                                  factorY:1.25,
//                                                  wheel:true,
//                                                  eps: 0.1
//                                                 }
//                                              });
    initValidate();
});

function initValidate(){
  $('#form')
  .form({
    onSuccess: function(event, fields) {
        SubmitForm(fields);
        event.preventDefault();
    },
    on: 'blur',
    fields: {
      equation: {
        identifier  : 'equation',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          }
        ]
      },
      a: {
        identifier  : 'x',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          },
          {
            type: 'decimal',
            prompt: 'Tiene que ser un número'
          },
          {
            type: 'decimal[0..]',
            prompt: 'Numero tiene que ser mayor a cero'
          }
        ]
      },
      error: {
        identifier  : 'error',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          },
          {
            type: 'decimal',
            prompt: 'Tiene que ser un número'
          }
        ]
      }
    }
  });
}

function SubmitForm(fields) {
    var valid = $(".ui.form").form('is valid');
    $.ajax({
        url: '/calcular_punto_fijo',
        type: 'POST',
        data: fields,
        success: function(data){
            $('#tboby-list').empty();
            $.each(data.data, function(index, element){
//                console.log("<tr><td>" + element.x + "</td><td>"+ element.error + "</td></tr>");
                $('#tboby-list').append("<tr><td>" + element.x + "</td><td>"+ element.error + "%</td></tr>");
            });
        }
    });
}

//function drawPoints(board, a, b, error){
//    board.create('point', [a,b],{name: error+'%', withLabel:true});
//}