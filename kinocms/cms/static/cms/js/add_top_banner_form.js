"use strict";

const addTopBannerFormBtn = document.getElementById('add-top-banner-form');
const totalTopBannerForms = document.getElementById('id_top_banner-TOTAL_FORMS');

addTopBannerFormBtn.addEventListener('click', add_top_banner_form);

function add_top_banner_form(event) {
  if (event) {
    event.preventDefault()
  }
  const formCopyTarget = document.getElementById('top-banner-formset');
  const copyEmptyTopBannerForm = document.getElementById('top-banner-empty-form').cloneNode(true);
  copyEmptyTopBannerForm.setAttribute('class', 'col-md-4 align-self-end text-center top-banner-form');
  const currentTopBannerFormsCount = document.getElementsByClassName('top-banner-form').length;
  copyEmptyTopBannerForm.setAttribute('id', `form-${currentTopBannerFormsCount}`);
  const regex = new RegExp('__prefix__', 'g');
  copyEmptyTopBannerForm.innerHTML = copyEmptyTopBannerForm.innerHTML.replace(regex, currentTopBannerFormsCount);
  totalTopBannerForms.setAttribute('value', currentTopBannerFormsCount+1);
  // add empty form element to html form
  formCopyTarget.append(copyEmptyTopBannerForm);
  // get image field and display uploaded image
  const imageField = document.getElementById(`id_top_banner-${currentTopBannerFormsCount}-image`);
  const uploadedImage = document.getElementById(`id_top_banner-${currentTopBannerFormsCount}-uploaded-image`);
  imageField.onchange = evt => {
    const [file] = imageField.files
    if (file) {
      uploadedImage.src = URL.createObjectURL(file);
      uploadedImage.setAttribute('class', '');
    }
  }
}

// check image size. submit form if all images fit
let imageInput;
let imageSizeStatus = [];
let topBannerForm = document.getElementById('topBannerForm');
topBannerForm.submit( function ( e ){
  e.preventDefault()
  let currentFormCount = document.getElementById('id_top_banner-TOTAL_FORMS');
  for (i=currentFormCount; i>=0; i--) {
    imageInput = document.getElementById(`id_top_banner-${i}-image`);
    let file = fileInput.files[0];
    if ( file ) {
      let img = new Image();

      img.src = URL.createObjectURL( file );

      img.onload = function() {
        let width = img.naturalWidth;
        let height = img.naturalHeight;

        URL.revokeObjectURL( img.src );

        if( width == 1000 && height == 190 ) {
          imageSizeStatus.push('OK');
          continue;
        }
        else {
          imageSizeStatus.push('FAIL');
          continue;
        };
      };
    };
    // no file go to next input
    else {
      continue;
    };
  }
  // check if any image from input failed size check
  if ( imageSizeStatus.includes('FAIL') ) {
    alert('Fail');
    };
  else {
    form.submit();
  };
});