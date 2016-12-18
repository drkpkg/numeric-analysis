$(function(){
    var board = JXG.JSXGraph.initBoard('box', {boundingbox: [-10, 10, 10, -10],
                                              axis:true,
                                              zoom: {
                                                  factorX:1.25,
                                                  factorY:1.25,
                                                  wheel:true,
                                                  eps: 0.1
                                                 }
                                              });
    initValidate(board);
});

function initValidate(board){
  $('#form')
  .form({
    onSuccess: function(event, fields) {
        SubmitForm(fields, board);
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
        identifier  : 'a',
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
      b: {
        identifier  : 'b',
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

function SubmitForm(fields, board) {
    var valid = $(".ui.form").form('is valid');
    $.ajax({
        url: '/calcular_biseccion',
        type: 'POST',
        data: fields,
        success: function(data){
            $.each(data.data, function(index, element){
                drawPoints(board, element.a,element.b, element.error);
            });
        }
    });
}

function drawPoints(board, a, b, error){
    board.create('point', [a,b],{name: error+'%', withLabel:true});
}