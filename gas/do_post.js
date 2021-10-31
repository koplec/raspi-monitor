function doPost(e) {
  let ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("raspberrypi-72");
  let data = JSON.parse(e.postData.getDataAsString());

  sheet.appendRow([data["time-stamp"], data["cpu-temp"]]);


  let output = ContentService.createTextOutput();
  output.setMimeType(ContentService.MimeType.JSON);
  output.setContent(JSON.stringify({ message: "success!" }));

  return output;
}
