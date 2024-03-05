
let dropZone = document.getElementById('drop_zone');
let dropZone_p = document.getElementById('drop_zone_p');

dropZone.addEventListener('dragover', function(e) {
  e.preventDefault();
  dropZone.style.border = '2px dashed #000';
  dropZone_p.style.color = 'red';
  dropZone_p.innerHTML = 'Drop';
}); 

dropZone.addEventListener('dragleave', function(e) {
  e.preventDefault();
  dropZone.style.border = '2px dashed #ccc';
  dropZone_p.style.color = '#ccc';
  dropZone_p.innerHTML = 'Drop files here';
});


dropZone.addEventListener('drop', function(e) {
  e.preventDefault();
  dropZone.style.border = '2px dashed #ccc';
  dropZone_p.style.color = '#ccc';
  dropZone_p.innerHTML = 'Drop files here';
 
  let file = e.dataTransfer.files[0];
  if (file.type === 'application/pdf') {
    alert('File uploaded successfully');
  }else{
    alert('Please upload a valid PDF file');
  }
});