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
      equation_a: {
        identifier  : 'equation_a',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          }
        ]
      },
      equation_b: {
        identifier  : 'equation_b',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          }
        ]
      }
    }
  });
}

function SubmitForm(fields) {
    var valid = $(".ui.form").form('is valid');
    $.ajax({
        url: '/calcular_horner',
        type: 'POST',
        data: fields,
        success: function(data){
            $('#quotient').val(data.data.quotient);
            $('#residue').val(data.data.residue);
        }
    });
}

//function drawPoints(board, a, b, error){
//    board.create('point', [a,b],{name: error+'%', withLabel:true});
//}