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
