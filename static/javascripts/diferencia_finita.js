$(function(){
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
      x: {
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
      t: {
        identifier  : 't',
        rules: [
          {
            type   : 'empty',
            prompt : 'Seleccione valor'
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
        url: '/calcular_diferencia_finita',
        type: 'POST',
        data: fields,
        success: function(data){
            $('#solution').val(data.sections);
        }
    });
}

function drawPoints(board, a, b, error){
    board.create('point', [a,b],{name: error+'%', withLabel:true});
}