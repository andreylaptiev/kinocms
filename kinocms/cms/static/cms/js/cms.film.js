"use strict";

/*
  Add empty ImageForm
  Display uploaded image
*/
const addImageFormButton = document.getElementById('add-image-form');
const totalImageForms = document.getElementById('id_form-TOTAL_FORMS');

addImageFormButton.addEventListener('click', addImageForm);

function addImageForm(event) {
    if (event) {
    event.preventDefault()
  }
  const formCopyTarget = document.getElementById('image-formset');
  const copyEmptyImageForm = document.getElementById('image-empty-form').cloneNode(true);
  copyEmptyImageForm.setAttribute('class', 'col-md-4 image-form');
  copyEmptyImageForm.setAttribute('class', 'col-md-4 align-self-end text-center image-form');
  const currentImageFormsCount = document.getElementsByClassName('image-form').length;
  copyEmptyImageForm.setAttribute('id', `form-${currentImageFormsCount}`);
  const regex = new RegExp('__prefix__', 'g');
  copyEmptyImageForm.innerHTML = copyEmptyImageForm.innerHTML.replace(regex, currentImageFormsCount);
  totalImageForms.setAttribute('value', currentImageFormsCount+1);
  // add empty form element to html form
  formCopyTarget.append(copyEmptyImageForm);
  // get image field and display uploaded image
  const imageField = document.getElementById(`id_form-${currentImageFormsCount}-image`);
  const uploadedImage = document.getElementById(`id_form-${currentImageFormsCount}-uploaded-image`);
  imageField.onchange = evt => {
    const [file] = imageField.files
    if (file) {
      uploadedImage.src = URL.createObjectURL(file);
      uploadedImage.setAttribute('class', '');
    };
  };
};
