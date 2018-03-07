import Page from '../Page';
import withOwnContent from './withOwnContent';

/**
 *  Shelf Sample Page uses the withOwnContent higher order component to return a page
 *  but using local static content.
 */
const sampleShelves = {
  title: 'Shelf Samples',
  body: [
    {
      id: 'carousel-1',
      type: 'carousel_shelf',
      value: {
        heading: 'Sample Carousel Shelf',
        items: [
          {
            id: 'carousel-promo-shelf-1',
            type: 'promo_shelf',
            value: {
              heading: 'html::Active <span class="marker">10</span> App',
              body: 'Did you know that a brisk 10 minute walk counts as exercise?\nGet started with our free app',
              cta_button_label: 'Download',
              cta_button_link: 'http://www.somewebsite.co.uk',
              background_image: 'http://aaa.bbb.ccc/gb.png',
              meta_layout: 'full_width',
              meta_variant: 'main-banner'
            }
          },
          {
            id: 'carousel-promo-shelf-2',
            type: 'promo_shelf',
            value: {
              heading: 'html::Active <span class="marker">10</span> App',
              body: 'Did you know that a brisk 10 minute walk counts as exercise?\nGet started with our free app',
              cta_button_label: 'Download',
              cta_button_link: 'http://www.somewebsite.co.uk',
              background_image: 'http://aaa.bbb.ccc/gb.png',
              meta_layout: 'full_width',
              meta_variant: 'main-banner'
            }
          }
        ],
        meta_variant: 'blue_background'
      }
    },
    {
      id: 'grid-shelf-1',
      type: 'grid_shelf',
      value: {
        heading: 'Sample Grid Shelf',
        rows_to_show: 1,
        items: [
          {
            id: 'video-teaser-1',
            type: 'video_teaser',
            value: {
              heading: 'Walk the walk, talk the talk 2',
              body: 'Share walking stories and your progress with others online',
              video: '5520584848001',
              cta: {
                link_text: 'Find out more',
                link_external: 'http://www.somewebsite.co.uk'
              },
              meta_variant: 'yellow'
            }
          },
          {
            id: 'video-teaser-2',
            type: 'video_teaser',
            value: {
              heading: 'Walk the walk, talk the talk',
              body: 'Share walking stories and your progress with others online',
              video: '5669668082001',
              cta: {
                link_text: 'Find out more',
                link_external: 'http://www.somewebsite.co.uk'
              }
            }
          },
          {
            id: 'video-teaser-3',
            type: 'video_teaser',
            value: {
              heading: 'Walk the walk, talk the talk',
              body: 'Share walking stories and your progress with others online',
              video: '',
              cta: {
                link_text: 'Find out more',
                link_external: 'http://www.somewebsite.co.uk'
              }
            }
          },
          {
            id: 'video-teaser-4',
            type: 'video_teaser',
            value: {
              heading: 'Walk the walk, talk the talk',
              body: 'Share walking stories and your progress with others online',
              image: {
                title: 'IMage name'
              },
              video: '123456',
              cta: {
                link_text: 'Find out more',
                link_external: 'http://www.edfs.co.uk'
              }
            }
          },
          {
            id: 'app-teaser-1',
            type: 'app_teaser',
            value: {
              heading: 'html::Download the  <strong><span class="text-color--secondary">Wellmind</span> App</strong>',
              body: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt',
              image: {
                title: 'Image name'
              },
              cta_appstore: {
                link_external: 'http://www.edfs.co.uk'
              },
              cta_googleplay: {
                link_external: 'https://play.google.com/store/apps/details?id=com.bluestepsolutions.wellmind&hl=en_GB'
              },
            }
          },
          {
            id: 'oneyou1-teaser-1',
            type: 'oneyou1_teaser',
            value: {
              heading: 'Be Active With a Disability',
              body: 'There are so many ways to move - whatever your situation. Get ideas on the EDFS website',
              image: {
                title: '',
                link: ''
              },
              cta: [
                {
                  link_text: 'Link 1 text',
                  link_external: 'http://www.edfs.co.uk'
                },
                {
                  link_text: 'Link 2 text',
                  link_page: 6
                },
                {
                  link_text: 'Link 3 text',
                  link_external: 'http://www.edfs.co.uk'
                }
              ]
            }
          },
          {
            id: 'oneyou2-teaser-2',
            type: 'oneyou1_teaser',
            value: {
              heading: 'Be Active With a Disability',
              body: 'There are so many ways to move - whatever your situation. Get ideas on the EDFS website',
              cta: {
                link_text: 'Link 1 text',
                link_external: 'http://www.edfs.co.uk'
              },
            }
          }
        ],
        meta_variant: 'blue_background'
      }
    },
    {
       id: 'weeww',
       type: 'section_heading_shelf',
       value: {
           heading: 'This is a section heading',
           shelf_id: 'test-section-heading-1',
           meta_layout: 'section_heading',
       }
    },
    {
      id: 'page-heading-shelf-1',
      type: 'page_heading_shelf',
      value: {
        heading: 'Move More',
        body: 'Moving is good for your body and mind. Try these easy ways to move more each day.',
        background_image: 'http://aaa.bbb.ccc/gb.png',
        meta_layout: 'page_header',
        meta_variant: 'home-page'
      }
    },
    {
      id: 'page-heading-shelf-2',
      type: 'page_heading_shelf',
      value: {
        heading: 'Move More',
        body: 'Moving is good for your body and mind. Try these easy ways to move more each day.',
        background_image: 'http://aaa.bbb.ccc/gb.png',
        meta_layout: 'page_header',
        meta_variant: 'sub-page'
      }
    },
    {
      id: 'banner-shelf-1',
      type: 'banner_shelf',
      value: {
        heading: 'html::Active <span class="marker">10</span> App',
        body: 'Did you know that a brisk 10 minute walk counts as exercise?\nGet started with our free app',
        cta: {
          link_text: 'Download',
          link_external: 'http://www.edfs.co.uk'
        },
        background_image: 'http://aaa.bbb.ccc/gb.png',
        meta_layout: 'full_width',
        meta_variant: 'promo'
      }
    },
    {
      id: 'promo-shelf-1',
      type: 'promo_shelf',
      value: {
        heading: 'html::How are <span class="marker">you</span>? Quiz',
        cta: {
          link_text: 'Have a go',
          link_external: 'http://www.edfs.co.uk'
        },
        meta_layout: 'cta_on_right',
        meta_variant: 'promo'
      }
    },
    {
      id: 'promo-shelf-2',
      type: 'promo_shelf',
      value: {
        heading: 'html::How are <span class="marker">you</span>? Quiz',
        cta: {
          link_text: 'Have a go',
          link_external: 'http://www.edfs.co.uk'
        },
        meta_layout: 'cta_on_left',
        meta_variant: 'promo'
      }
    },
    {
      id: 'promo-shelf-3',
      type: 'promo_shelf',
      value: {
        heading: 'html::Tell us what <span class="marker">you</span> Think',
        cta: {
          link_text: 'Send a message',
          link_external: 'http://www.edfs.co.uk'
        },
        meta_layout: 'cta_on_right',
        meta_variant: 'promo'
      }
    },
    {
      id: 'basic-cta-shelf-1',
      type: 'promo_shelf',
      value: {
        heading: 'html::<span class="text-light">Over 40?</span><br />Check Your Health',
        background_image: 'http://aaa.bbb.ccc/gb.png',
        meta_variant: 'extra-height'
      }
    }
  ]
};

export default withOwnContent(Page, sampleShelves);
