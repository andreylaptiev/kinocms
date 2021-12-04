"use strict";

const addFilmBannersFormBtn = document.getElementById('add-film-banners-form');
const totalFilmBannersForms = document.getElementById('id_form-TOTAL_FORMS');

addFilmBannersFormBtn.addEventListener('click', add_new_form);

function add_new_form(event) {
  if (event) {
    event.preventDefault()
  }
  const formCopyTarget = document.getElementById('film-banners-list');
  const copyEmptyFormEl = document.getElementById('empty-form').cloneNode(true);
  copyEmptyFormEl.setAttribute('class', 'col-6 col-md-4 film-banners-form');
  const currentFilmBannersFormsCount = document.getElementsByClassName('film-banners-form').length;
  copyEmptyFormEl.setAttribute('id', `form-${currentFilmBannersFormsCount-1}`);
  const regex = new RegExp('__prefix__', 'g');
  copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFilmBannersFormsCount-1);
  totalFilmBannersForms.setAttribute('value', currentFilmBannersFormsCount);
  // add empty form element to html form
  formCopyTarget.append(copyEmptyFormEl);
}