"use strict";

const addTopBannerFormBtn = document.getElementById('add-top-banner-form');
const totalTopBannerForms = document.getElementById('id_top_banners-TOTAL_FORMS');

addTopBannerFormBtn.addEventListener('click', add_top_banner_form);

function add_top_banner_form(event) {
  if (event) {
    event.preventDefault()
  }
  const formCopyTarget = document.getElementById('top-banner-formset');
  const copyEmptyTopBannerForm = document.getElementById('top-banner-empty-form').cloneNode(true);
  copyEmptyTopBannerForm.setAttribute('class', 'col-6 col-md-4 top-banner-form');
  const currentTopBannerFormsCount = document.getElementsByClassName('top-banner-form').length;
  copyEmptyTopBannerForm.setAttribute('id', `form-${currentTopBannerFormsCount-1}`);
  const regex = new RegExp('__prefix__', 'g');
  copyEmptyTopBannerForm.innerHTML = copyEmptyTopBannerForm.innerHTML.replace(regex, currentTopBannerFormsCount-1);
  totalTopBannerForms.setAttribute('value', currentTopBannerFormsCount);
  // add empty form element to html form
  formCopyTarget.append(copyEmptyTopBannerForm);
}