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
      equations: {
        identifier  : 'equations',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          }
        ]
      },
      limit: {
        identifier  : 'limit',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          },
          {
            type: 'integer',
            prompt: 'Tiene que ser un entero'
          }
        ]
      }
    }
  });
}

function SubmitForm(fields) {
    var valid = $(".ui.form").form('is valid');
    $.ajax({
        url: '/calcular_jacobi',
        type: 'POST',
        data: fields,
        success: function(data){
            $('#solution').val('')
            $('#solution_sections').val('')
            $('#solution').val(data.eqc);
            $('#solution_sections').val(data.sections);
        }
    });
}

//function drawPoints(board, a, b, error){
//    board.create('point', [a,b],{name: error+'%', withLabel:true});
//}