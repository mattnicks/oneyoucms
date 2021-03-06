import React, { Component } from 'react';
import FooterMenu from './header-nav/FooterMenu';
import Image from './Image.js';
import SocialLinks from './header-nav/SocialLinks';
import logo from '../assets/images/public-health-england-logo.png';

class Footer extends Component {
  render() {
    let { className, content, site } = this.props;

    if (!content) {
      return null;
    }

    let { image, links, social_media } = content;
    let tempImage = { link: logo, title: 'PHE logo' };

    return (
      <div className={className}>
        <div className ="container">
          <div className = "row">
            <div className ="col">
              <Image image={tempImage} height="68" className="page-footer__phe-logo" />
              <FooterMenu items={links} />
            </div>
            <div className ="col text-right">
              <SocialLinks links={social_media} site={site} />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Footer;
