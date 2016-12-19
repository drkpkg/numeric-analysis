$(function(){
    initValidate();
    $('#octave').hide();
    $('#t').on('change',function(){
        if($(this).val() == '1'){
            $('#octave').show();
        }else{
            $('#octave').hide();
        }
    });
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
        identifier  : 'a',
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
      n: {
        identifier  : 'n',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          },
          {
            type: 'integer',
            prompt: 'Tiene que ser un número'
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
      }
    }
  });
}

function SubmitForm(fields, board) {
    var valid = $(".ui.form").form('is valid');
    $.ajax({
        url: '/calcular_trapecio',
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