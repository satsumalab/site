[![Netlify Status](https://api.netlify.com/api/v1/badges/76963489-0a23-4cd5-b203-0ce329e02437/deploy-status)](https://app.netlify.com/sites/satsuma/deploys)

# Satsuma Research Group Site
This is the Satsuma Research Group Site, built using Hugo with theme Research Group by Wowchemy. More details on the theme and extra documentation below. The site itself is hosted on Netlify, when changes are pushed to the *main* branch they are deployed on netlify and live at [satsuma.netlify.app](https://satsuma.netlify.app/). 

**All research group members are entitled to update content and are strongly encouraged to as soon as possible!** Please read below and if still unsure, just ask!

Hopefully this format will make the process painless to collaboratively update the group site. With Hugo all that is left you to do is fill in the content! So please read the guides below on how to add content.

# Adding content
1) Clone this repository to your local computer for the first time otherwise pull the latest changes.
2) Make changes to the site in the *dev* branch, commit with a short description of what changes you made and push.
3) Push changes to the dev branch on github, check that it builds properly.
4) Make a pull request to the main branch.
5) Finalise the pull request to update the live site!

All content editing should be done in [/content/](/content).

## Profiles
Profiles are under [/content/authors](/content/authors).
To create a profile:
1) Duplicate the example folder within [/content/authors](/content/authors). Rename it to a shorthand for your name e.g. Joseph Jacob is joe. This is where your profile with be stored.
2) Delete avatar.jpg and replace with your own profile pic titling avatar, it can be either .jpg or .png.
3) Edit \_index.md to your details. Leave superuser as false. Leave url under organisations empty. Your bio will be under the ---. Please don't edit email, highlight_name and user_groups.
4) Feel free to edit social icons as you wish, more should be [https://sourcethemes.com/academic/docs/page-builder/#icons](available).
5) Finally, remove the top 8 lines.
6) All done! continue the instruction on adding content.

If in doubt, feel free to check other profile pages!

## Papers
## News

---
## Wowchemy's Research Group Template for [Hugo](https://github.com/gohugoio/hugo)

The **Research Group Template** empowers your research group to easily create a beautiful website with a stunning homepage, news, academic publications, events, team profiles, and a contact form.

[Check out the latest demo](https://research-group.netlify.app/) of what you'll get in less than 5 minutes, or [view the showcase](https://wowchemy.com/user-stories/).

_[**Wowchemy**](https://wowchemy.com) makes it easy to create a beautiful website for free. Edit your site in Markdown, Jupyter, or RStudio (via Blogdown), generate it with Hugo, and deploy with GitHub or Netlify. Customize anything on your site with widgets, themes, and language packs._

- 👉 [**Get Started**](https://wowchemy.com/templates/)
- 📚 [View the **documentation**](https://wowchemy.com/docs/)
- 💬 [Chat with the **Wowchemy community**](https://discord.gg/z8wNYzb) or [**Hugo community**](https://discourse.gohugo.io)
- 🐦 Twitter: [@wowchemy](https://twitter.com/wowchemy) [@GeorgeCushen](https://twitter.com/GeorgeCushen) [#MadeWithWowchemy](https://twitter.com/search?q=(%23MadeWithWowchemy%20OR%20%23MadeWithAcademic)&src=typed_query)
- 💡 [Request a **feature** or report a **bug** for _Wowchemy_](https://github.com/wowchemy/wowchemy-hugo-modules/issues)
- ⬆️ **Updating Wowchemy?** View the [Update Guide](https://wowchemy.com/docs/update/) and [Release Notes](https://github.com/wowchemy/wowchemy-hugo-modules/releases)

## Crowd-funded open-source software

To help us develop this template and software sustainably under the MIT license, we ask all individuals and businesses that use it to help support its ongoing maintenance and development via sponsorship.

### [❤️ Click here to unlock rewards with sponsorship](https://wowchemy.com/sponsor/)

## Ecosystem

* **[Hugo Academic CLI](https://github.com/wowchemy/hugo-academic-cli/):** Automatically import publications from BibTeX
