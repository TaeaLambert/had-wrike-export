function send_google_sheet_id_to_hubspot_importer() {
  var google_sheet_id = SpreadsheetApp.getActiveSpreadsheet().getId();
  var url =
    "https://neo-sharepoint-and-googlesheet-intergration-oouurrzfmq-uc.a.run.app/google_sheets_import";
  var headers = {
    Accept: "application/json",
    "Content-Type": "application/json",
    "X-APIKEY": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJzdWIiOiIxMjM0NT",
  };
  var options = {
    method: "POST",
    contentType: "application/json",
    headers: headers,
    payload: JSON.stringify({
      google_sheet_id: google_sheet_id,
      worksheet: "Transformed - Import Sheet",
    }),
  };
  try {
    var response = UrlFetchApp.fetch(url, options);
  } catch (err) {
    console.log(err);
  }
  console.log(response);
  SwapDrawingOnActions("Upload Button", "_PleaseWait", "_Button");
}

function SwapDrawingOnActions(sheet, actionToFind, actionToReplaceWith) {
  let replaced = false;

  if ("string" === typeof sheet) {
    sheet = SpreadsheetApp.getActive().getSheetByName(sheet);
  }

  const drawings = sheet.getDrawings();
  for (var i = 0; i < drawings.length; i++) {
    const drawing = drawings[i];
    if (drawing.getOnAction() === actionToFind) {
      drawing.setOnAction(actionToReplaceWith);
      replaced = true;
      break;
    }
  }
  return replaced;
}
function _Button() {
  Browser.msgBox("Okay, we're about to do something important right now.");
  var replaced = false;
  while (replaced != true) {
    replaced = SwapDrawingOnActions("Upload Button", "_Button", "_PleaseWait");
    const drawings = SpreadsheetApp.getActive()
      .getSheetByName("Upload Button")
      .getDrawings();
    for (var i = 0; i < drawings.length; i++) {
      const drawing = drawings[i];
      if (drawing.getOnAction() === "_Button") {
        replaced = false;
      }
    }
  }
  send_google_sheet_id_to_hubspot_importer();
}

function _PleaseWait() {
  Browser.msgBox("Sorry, we're doing something important right now.");
}
