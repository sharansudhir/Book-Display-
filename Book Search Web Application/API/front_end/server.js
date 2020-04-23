$(document).ready(function() {

    $("#buttonsearch").click(function()
    {
        var search_term = $("#search").val();
        var s = {'search_term' : search_term}
        if(search_term == '')
        {
            alert("Enter Search Term")
        }
        else
        {
            $.ajax({
                type: 'POST',
                url: "http://34.200.121.45:5100/logs",
                data: JSON.stringify(s),
                dataType:'json',
            }).done(function (data) { 
                console.log(data)
             });


            $.ajax({
                type: 'POST',
                url: "http://34.200.121.45:5000/search",
                data: JSON.stringify(s),
                dataType:'json',
            }).done(function(data)
            {
                console.log(data);

                if(data.length == 0)
                {
                    document.getElementById('showData').innerHTML = "No Result Found"
                }
                else
                {
                    var d = data

                    $.ajax({
                        type: 'POST',
                        url: "http://34.200.121.45:5200/catalogue",
                        data: JSON.stringify(d),
                        dataType:'json',
                    }).done(function (x)
                     {
                         console.log(x)
                       })

                    var col = [];
                     for (var i = 0; i < data.length; i++) 
                     {
                         for (var key in data[i]) 
                         {
                             if (col.indexOf(key) === -1) 
                             {
                                 col.push(key);
                             }
                        }
                     }

                     console.log(col)
                     var table = document.createElement("table");

                     var tr = table.insertRow(-1);                   // TABLE ROW.

                     for (var i = 0; i < col.length; i++)
                      {
                         var th = document.createElement("th");      // TABLE HEADER.
                         th.innerHTML = col[i];
                         tr.appendChild(th);
                     }

                     for (var i = 0; i < data.length; i++) {

                        tr = table.insertRow(-1);
            
                        for (var j = 0; j < col.length; j++) {
                            var tabCell = tr.insertCell(-1);
                            tabCell.innerHTML = data[i][col[j]];
                        }
                    }
                    var divContainer = document.getElementById("showData");
                    divContainer.innerHTML = "";
                    divContainer.appendChild(table);
                }

            });
        }

    }); 

    $("#button_notes").click(function()
    {
        var search_term = $("#search").val();
        var note = $("#notes").val()
        

        if(search_term == '' || note == '')
        {
            alert("Note or Search term not entered")
        }
        else
        {
            notes = search_term + "," + note;
            s = {keyword : notes}

            $.ajax({
                type: 'POST',
                url: "http://34.200.121.45:5300/notes",
                data: JSON.stringify(s),
                dataType:'json',
            }).done(function (data) { 
                console.log(data)
             });
        }


    });

    $("#button_notes_search").click(function()
    { 
        var note_term = $("#notes_search").val()

        if(note_term == '')
        {
            alert("Note Term to be searched not entered")
        }
        else
        {
         
            $.ajax({
                type: 'POST',
                url: "http://34.200.121.45:5300/notes_search",
                data: JSON.stringify(note_term),
                dataType:'json',
            }).done(function (data) { 
                console.log(data)

                if(data.length == 0)
                {
                    document.getElementById('showData').innerHTML = "No Result Found"
                }
                else
                {
                    document.getElementById('showData').innerHTML = "Keyword: "+note_term+ "<br>"+ "Note Saved: "+data[note_term]
                }
             });
        }
    });
});