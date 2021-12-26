"use strict";

// add empty news banner form
const addNewsBannerFormBtn = document.getElementById('add-news-banner-form');
const totalNewsBannerForms = document.getElementById('id_news_banner-TOTAL_FORMS');

addNewsBannerFormBtn.addEventListener('click', add_news_banner_form);

function add_news_banner_form(event) {
  if (event) {
    event.preventDefault()
  }
  const formCopyTarget = document.getElementById('news-banner-formset');
  const copyEmptyNewsBannerForm = document.getElementById('news-banner-empty-form').cloneNode(true);
  copyEmptyNewsBannerForm.setAttribute('class', 'col-md-4 align-self-end text-center news-banner-form');
  const currentNewsBannerFormsCount = document.getElementsByClassName('news-banner-form').length;
  copyEmptyNewsBannerForm.setAttribute('id', `form-${currentNewsBannerFormsCount}`);
  const regex = new RegExp('__prefix__', 'g');
  copyEmptyNewsBannerForm.innerHTML = copyEmptyNewsBannerForm.innerHTML.replace(regex, currentNewsBannerFormsCount);
  totalNewsBannerForms.setAttribute('value', currentNewsBannerFormsCount+1);
  // add empty form element to html form
  formCopyTarget.append(copyEmptyNewsBannerForm);
  // get image field and display uploaded image
  const imageField = document.getElementById(`id_news_banner-${currentNewsBannerFormsCount}-image`);
  const uploadedImage = document.getElementById(`id_news_banner-${currentNewsBannerFormsCount}-uploaded-image`);
  imageField.onchange = evt => {
    const [file] = imageField.files
    if (file) {
      uploadedImage.src = URL.createObjectURL(file);
      uploadedImage.setAttribute('class', '');
    }
  }
}