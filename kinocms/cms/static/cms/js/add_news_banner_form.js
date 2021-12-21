"use strict";

// add empty news banner form
const addNewsBannerFormBtn = document.getElementById('add-news-banner-form');
const totalNewsBannerForms = document.getElementById('id_news_banners-TOTAL_FORMS');

addNewsBannerFormBtn.addEventListener('click', add_news_banner_form);

function add_news_banner_form(event) {
  if (event) {
    event.preventDefault()
  }
  const formCopyTarget = document.getElementById('news-banner-formset');
  const copyEmptyNewsBannerForm = document.getElementById('news-banner-empty-form').cloneNode(true);
  copyEmptyNewsBannerForm.setAttribute('class', 'col-6 col-md-4 news-banner-form');
  const currentNewsBannerFormsCount = document.getElementsByClassName('news-banner-form').length;
  copyEmptyNewsBannerForm.setAttribute('id', `form-${currentNewsBannerFormsCount-1}`);
  const regex = new RegExp('__prefix__', 'g');
  copyEmptyNewsBannerForm.innerHTML = copyEmptyNewsBannerForm.innerHTML.replace(regex, currentNewsBannerFormsCount-1);
  totalNewsBannerForms.setAttribute('value', currentNewsBannerFormsCount);
  // add empty form element to html form
  formCopyTarget.append(copyEmptyNewsBannerForm);
}