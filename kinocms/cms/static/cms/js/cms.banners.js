'use strict';

const addTopBannerFormButton = document.getElementById('add-top-banner-form');
const totalTopBannerForms = document.getElementById('id_top_banner-TOTAL_FORMS');

addTopBannerFormButton.addEventListener('click', addTopBannerForm);

function addTopBannerForm(event) {
  if (event) {
    event.preventDefault()
  }
  const formCopyTarget = document.getElementById('top-banner-formset');
  const copyEmptyTopBannerForm = document.getElementById('top-banner-empty-form').cloneNode(true);
  copyEmptyTopBannerForm.setAttribute('class', 'col-md-4 align-self-end justify-content-center top-banner-form');
  const currentTopBannerFormsCount = document.getElementsByClassName('top-banner-form').length;
  copyEmptyTopBannerForm.setAttribute('id', `form-${currentTopBannerFormsCount}`);
  const regex = new RegExp('__prefix__', 'g');
  copyEmptyTopBannerForm.innerHTML = copyEmptyTopBannerForm.innerHTML.replace(regex, currentTopBannerFormsCount);
  totalTopBannerForms.setAttribute('value', currentTopBannerFormsCount+1);
  // add empty form element to html form
  formCopyTarget.append(copyEmptyTopBannerForm);
  // get image field and display uploaded image
  const imageField = document.getElementById(`id_top_banner-${currentTopBannerFormsCount}-image`);
  const uploadedTopBannerImage = document.getElementById(`id_top_banner-${currentTopBannerFormsCount}-uploaded-image`);
  imageField.onchange = evt => {
    const [file] = imageField.files
    if (file) {
      uploadedTopBannerImage.src = URL.createObjectURL(file);
      uploadedTopBannerImage.setAttribute('class', '');
      // check image size
      let img = new Image();
      img.src = uploadedTopBannerImage.src;
      img.onload = function() {
        let width = img.naturalWidth;
        let height = img.naturalHeight;

        URL.revokeObjectURL( img.src );
        // if image size matches requirements then 'add' and 'submit' buttons are enabled (disabled if not)
        if( width == 1000 && height == 190 ) {
          document.getElementById('add-top-banner-form').disabled = false;
          document.getElementById('submit-top-banner-form').disabled = false;
          return
        }
        else {
          document.getElementById('add-top-banner-form').disabled = true;
          document.getElementById('submit-top-banner-form').disabled = true;
          return
        };
      };
    };
  };
};


/*
  Display and check size of uploaded background banner
*/
const backgroundBannerImageField = document.getElementById('id_image')
const uploadedBackgroundBanner = document.getElementById('background-banner-uploaded-image')

backgroundBannerImageField.onchange = evt => {
  const [file] = backgroundBannerImageField.files
  if (file) {
    uploadedBackgroundBanner.src = URL.createObjectURL(file);
    uploadedBackgroundBanner.setAttribute('class', '');
    // check image size
    let img = new Image();
    img.src = uploadedBackgroundBanner.src;
    img.onload = function() {
      let width = img.naturalWidth;
      let height = img.naturalHeight;

      URL.revokeObjectURL( img.src );
      // disable 'submit' button unless image size matches required
      if( width == 2000 && height == 3000 ) {
        document.getElementById('submit-background-banner-form').disabled = false;
        document.getElementById('delete-background-banner-form').disabled = false;
        return
      }
      else {
        document.getElementById('submit-background-banner-form').disabled = true;
        document.getElementById('delete-background-banner-form').disabled = true;
        return
      };
    };
  };
};


/*
  Add empty news banner form
  Display uploaded image and check its size
*/
const addNewsBannerFormButton = document.getElementById('add-news-banner-form');
const totalNewsBannerForms = document.getElementById('id_news_banner-TOTAL_FORMS');

addNewsBannerFormButton.addEventListener('click', addNewsBannerForm);

function addNewsBannerForm(event) {
  if (event) {
    event.preventDefault()
  }
  const formCopyTarget = document.getElementById('news-banner-formset');
  const copyEmptyNewsBannerForm = document.getElementById('news-banner-empty-form').cloneNode(true);
  copyEmptyNewsBannerForm.setAttribute('class', 'col-md-4 align-self-end news-banner-form');
  const currentNewsBannerFormsCount = document.getElementsByClassName('news-banner-form').length;
  copyEmptyNewsBannerForm.setAttribute('id', `form-${currentNewsBannerFormsCount}`);
  const regex = new RegExp('__prefix__', 'g');
  copyEmptyNewsBannerForm.innerHTML = copyEmptyNewsBannerForm.innerHTML.replace(regex, currentNewsBannerFormsCount);
  totalNewsBannerForms.setAttribute('value', currentNewsBannerFormsCount+1);
  // add empty form element to html form
  formCopyTarget.append(copyEmptyNewsBannerForm);
  // get image field and display uploaded image
  const imageField = document.getElementById(`id_news_banner-${currentNewsBannerFormsCount}-image`);
  const uploadedNewsBannerImage = document.getElementById(`id_news_banner-${currentNewsBannerFormsCount}-uploaded-image`);
  imageField.onchange = evt => {
    const [file] = imageField.files
    if (file) {
      uploadedNewsBannerImage.src = URL.createObjectURL(file);
      uploadedNewsBannerImage.setAttribute('class', '');
      // check image size
      let img = new Image();
      img.src = uploadedNewsBannerImage.src;
      img.onload = function() {
        let width = img.naturalWidth;
        let height = img.naturalHeight;

        URL.revokeObjectURL( img.src );
        // if image size matches requirements then 'add' and 'submit' buttons are enabled (disabled if not)
        if( width == 1000 && height == 190 ) {
          document.getElementById('add-news-banner-form').disabled = false;
          document.getElementById('submit-news-banner-form').disabled = false;
          return
        }
        else {
          document.getElementById('add-news-banner-form').disabled = true;
          document.getElementById('submit-news-banner-form').disabled = true;
          return
        };
      };
    };
  };
};