"use strict";

// add empty image form
/* currentImageFormsCount and totalImageFormsCount are different
from banner formsets implementation because we already have
formset_manager BEFORE adding new empty forms (because
we add it manually to html code). In banner formsets
formset_manager creates when we add first empty form (it creates
with banner_formset.as_p).
*/
const addImageFormBtn = document.getElementById('add-image-form');
const totalImageForms = document.getElementById('id_form-TOTAL_FORMS');

addImageFormBtn.addEventListener('click', add_image_form);

function add_image_form(event) {
  if (event) {
    event.preventDefault()
  }
  const formCopyTarget = document.getElementById('image-formset');
  const copyEmptyImageForm = document.getElementById('image-empty-form').cloneNode(true);
  copyEmptyImageForm.setAttribute('class', 'col-md-4 image-form');
  const currentImageFormsCount = document.getElementsByClassName('image-form').length;
  copyEmptyImageForm.setAttribute('id', `form-${currentImageFormsCount}`);
  const regex = new RegExp('__prefix__', 'g');
  copyEmptyImageForm.innerHTML = copyEmptyImageForm.innerHTML.replace(regex, currentImageFormsCount);
  totalImageForms.setAttribute('value', currentImageFormsCount+1);
  // add empty form element to html form
  formCopyTarget.append(copyEmptyImageForm);
}