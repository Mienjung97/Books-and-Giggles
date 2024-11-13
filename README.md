# **Books and Giggles**

Books and Giggles is a fictional online book store that sells a small amount of books from the categories "Historic fiction", "Fantasy", "Science Fiction", "Illustrated books" as well as German originals translated into english, current bestsellers and more. Users are supposed to feel right at home and wanting to stay to browse books or find out information about the authors that we have in stock. The users have the capability to contact the sites admin for suggestions or issues, they can sign up for the sites newsletter and find lots of interesting information throughout the page.

[Access live website here](https://books-and-giggles-dcc63078a535.herokuapp.com/)

![Books and Giggles responsive design](readme/assets/images/responsiveness_bandg.PNG)
<br>

This fictional site was created for Portfolio Project #5 (Full-Stack Toolkit) - Diploma in Full Stack Software Development Diploma at the [Code Institute](https://www.codeinstitute.net). This webpage does not sell any real goods, nor does any payment information get stored.



# Table of Content

* [**Project**](<#project>)
    * [Objective](<#objective>)
    * [Site Users Goal](<#site-users-goal>)
    * [Site Owners Goal](<#site-owners-goal>)
    * [Business Model](<#business-model>)
    * [Marketing Techniques](<#marketing-techniques>)
    * [Project Management](<#project-management>)
    * [Database Schema](<#database-schema>)

* [**User Experience (UX)**](<#user-experience-ux>)
    * [Wireframes](<#wireframes>)
    * [User Stories](<#user-stories>)
    * [Site Structure](<#site-structure>)
    * [Design Choices](<#design-choices>)

* [**Features**](<#features>)

* [**Existing Features**](<#existing-features>)
    * [Navigational Features](<#navigation>)
    * [General Features](<#footer>)
    * [E-commerce Features](<#home>)
    * [Confirmation Features](<#about>)
    * [Admin Features](<#faq>)


* [**Future Features**](<#future-features>)

* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks & Software](<#frameworks--software>)
    * [Libraries](<#libraries>)

* [**Testing**](<#testing>)
    * [Testing User Stories](<#testing-user-stories>)
    * [Code Validation](<#code-validation>)
    * [Additional Testing](<#additional-testing>)
    * [Bugs](<#bugs>)
* [Deployment](<#deployment>)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)



<hr>
<hr>

# Project

Everything on this webpage is for educational purposes only, documentation on where pictures and information are coming from is in the credit section

## Objective
The idea of creating an online book store came to me from multiple angles - I am not an avid reader, nor do I own a lot of books (most of them are featured on this website) - but there is a deep connection on why I choose to make this my final project for the Code Institute Full Stack Software Developer course: My grandparents were both really into books, my grandmother loved the Angelique series, as well as many other historical fiction books, my grandfather has always enjoyed any kind of illustraded books, mostly of nature, mountains and animals. Unfortunatly, my grandfather passed in July and my grnadmother shortly after starting the project. My partner is also an avid reader, who suggested the idea to me - so I decided to create this project in memory of my grandparents and in dedication to my mother, partner and all the "book worms" in my family. Most of the books featured on this page are owend and were reccomended by them.

### Site Users Goal
Site users can browse through the webpage to gain inspiration for their next book or book series, as well as about the authors themselves. The website is easy to navigate and has an easy checkout procedure. Any user can contact the sites admin for questions, issues or ideas, as well as subscribing to the "Books and Giggles Newsletter" to stay up to date with inventory, promotions and sales. On the about page, the user can learn about the  and all possible questions are answered on the FAQ page. It is easy to create a profile, so that the user can save their information for their next purchaise and keep track of previous orders, but the creation of a profile is not necessary to order.

### Site Owners Goal
Besides providing a fully functional and welcoming E-commerce book store, the admin can modify all important data either via frontend implementation, like adding, editing or deleting products, authors and FAQ items, or through the admin panel, like changing the about page or editing categories. Any contact request will be send to the admin panel, providing important information like name and email. The admin can keep track of orders and collects payment info via [stripe](https://stripe.com) and collects the email addresses on [brevo](https://www.brevo.com/) with the option to send out customized newsletters. More information about all [features](<#existing-features>) and the [future features](<#future-features>) are below.

[Back to top](<#table-of-content>)

## Business Model
Books and Giggles is a Business to Consumer (B2C) E-commerce platform that sells books to everyone. The store has both low priced books for all ages, in addition classics, contemporary books to dystopian sience fiction and true stories about war. Also the store sells a high priced book, intended for collectors.

While providing everything a readers heart could wish for, Books and Giggles encourages their users to interact with the sites owners to make sure the store lives up to its potential. The philosophy behind the store is to be as accommodating for its users as possible. Customer support is an integral part of the business to rather have a smaller, but loyal customer base than to try and focus to become the biggest book store. 

More information about how this would be possible are in the [future features](<#future-features>) section.

[Back to top](<#table-of-content>)

## Marketing Techniques
After doing the callanges from the LMS, I have decided to implement good SEO as well as getting the e-mail marketing in form of the newsletter the main objective. If the website would be an actual E-commerce webpage, I would start by doing social media marketing by myself, as well as paying for targeted social media ads on Facebook and Instagram, as well as Sponsored posts with book influencers on various platforms like TikTok, Instagram and more. For more information, visit the last section of the marketing challange below.

### Challanges
Below are the results of compleating the three challanges from the LMS SEO and Web Marketing lessons:

<details><summary><b>Challanges</b></summary>
<br>

#### SEO Challange:

<details><summary><b>SEO Challange</b></summary>
<br>
<hr>

1. Brainstorm your general topics
<br>

- Historic fiction
- Fantasy
- Science Fiction
- Bestsellers
- German Authors
- Illustrated books

<hr>

2. Brain dump possible keywords for each of the general topics
<br>

Historic fiction:

- Classic novels
- Fiction bestsellers
- War novels
- Angélique series

Fantasy:

- Epic fantasy books
- Fantasy series
- Magic and wizards
- Fary tales

Science Fiction:

- Space books
- Dystopian sci-fi
- Time travel stories
- Alien invasion

Bestsellers:

- Top-rated books
- New releases
- Award-winning novels
- Popular authors

German Authors:

- Wolfgang Hohlbein
- Gebrüder Grimm (Brothers Grimm)
- Sebastian Fitzek
- Michael Ende

Illustrated books:

- Animals
- Geograpics
- History

<hr>

4. Ensure you have a selection of short and long-tail keywords
<br>

Short-tail:

- Fiction books
- Fantasy novels
- Sci-fi stories
- Bestsellers
- German books
- Warhammer 40K
- Historical fiction

Long-tail:

- Best epic fantasy series
- Top-rated science fiction books
- Popular contemporary fiction authors
- Award-winning historic fiction
- Best illustarated books of all time
- Best releases of this year
- Popular german books
- Books about the horrors of war 

<hr>

5. Final Keyword Selection
<br>

- Online fiction bookstore
- Fantasy and sci-fi novels
- Bestselling fiction books
- Epic fantasy series
- Space science fiction
- Contemporary fiction bestsellers
- Dystopian sci-fi novels
- Award-winning fantasy authors
- New sci-fi releases
- Top-rated fantasy books
- Popular fiction writers
- Award-winning historical fiction
- Illustraed books for everyone
- German Authors

[Back to top](<#table-of-content>)

</details><br/>

<hr>


#### Content Challenge

<details><summary><b>Content Challenge</b></summary>
<br>

<hr>

1. What do your users need?
<br>

- Easy navigation through specific genres, categories and/or authors
- General overview of inventory/options/authors
- Detailed book information (and maybe reviews) on detail page
- Easy checkout
- Contact option for questions, ideas and problem solving

<hr>

2. What information and features can you provide to meet those needs?
<br>

- Implement an advanced search function with filters for genres, authors, and publication dates
- Create a homepage with featured books, new releases, and bestsellers
- On the detail page, provide comprehensive book descriptions, including plot summaries, author bios (and maybe reader reviews)
- Implement a streamlined, user-friendly checkout process with easy payment option(s)
- Include a prominent "Contact Us" page with various contact methods (email, phone, chat) and a FAQ section

<hr>

3. How can you make the information easy to understand?
<br>

- Use clear, concise language in book descriptions and website copy
- Implement a user-friendly interface with intuitive category organization
- Include visual elements like book covers to enhance comprehension
- Offer sorting options (e.g., by popularity, rating, or release date) to help users find relevant titles quickly
- Include a search bar

<hr>

4. How can you demonstrate expertise, authoritativeness and trustworthiness in your content?
<br>

- Highlight your store's specialization in specific genres (e.g., historical fiction, fantasy, sci-fi)
- Provide in-depth, well-researched book descriptions (and author biographies)
- Display customer ratings and reviews prominently (optional)
- Include an "About Us" page detailing your company's history and expertise in the book industry

<hr>

5. Would there be other pages within your own site you could link to from your chosen page? (optional)
<br>

- Link to related books within the same genre or by the same author
- Create "You might also like" sections on book detail pages
- Link to thematic reading lists or curated collections
- Connect author pages to their respective books

<hr>

6. Are there opportunities to link back to external websites that already rank highly on Google?
<br>

- Link to official author websites or social media profiles
- Include links to reputable book review sites or literary awards
- Connect to relevant Wikipedia pages for historical context in historical fiction
- Link to publisher websites for additional book information
- Partner with genre-specific blogs or forums for cross-promotion

<hr>

7. How can you help users discover other relevant parts of your web application?
<br>

- Create a "Featured Books" carousel on the homepage and category pages
- Use tags to connect books with similar themes, styles, or time periods
- Develop a newsletter to keep users informed about new releases and promotions
- Create genre-specific landing pages with curated content and featured authors

[Back to top](<#table-of-content>)

</details><br/>

<hr>


#### Marketing Types Challenge

<details><summary><b>Marketing Types Challenge</b></summary>
<br>

<hr>

1. Who are your users?
<br>

- Avid readers of fiction, fantasy, and science fiction
- Book collectors interested in illustrated editions
- Fans of bestselling books
- Readers interested in German literature (in original or translation)
- Adults and young adults who prefer online shopping for books

<hr>

2. Which online platforms would you find lots of your users?
<br>

- Goodreads
- Reddit (especially subreddits like r/books)
- TikTok
- Instagram
- Facebook

<hr>

3. Would your users use social media? If yes, which platforms do you think you would find them on?
<br>

- Instagram (bookstagram community)
- TikTok (BookTok)
- Reddit (especially subreddits like r/books)
- Twitter 
- Facebook (book groups)
- Pinterest (for visual content related to books and reading)

<hr>

4. What do your users need? Could you meet that need with useful content? If yes, how could you best deliver that content to them?
<br>

- Book recommendations
- Reviews and ratings
- Information about new releases
- Author insights

Content ideas: 
<br>

- Blog posts featuring book reviews and genre discussions
- Author interviews
- Reading lists and themed book collections
- Behind-the-scenes looks at illustrated books

Delivery methods:
<br>

- Email newsletters
- Social media posts (especially visual content for Instagram and TikTok)
- YouTube videos for in-depth book discussions or author interviews
- Regular blog posts on the website (if blog is implemented/not planned for PP5)

<hr>

5. Would your business run sales or offer discounts? How do you think your users would most like to hear about these offers?
<br>

- Email newsletters
- Push notifications (if we have a mobile app)
- Social media posts, especially time-limited offers on Instagram Stories or other social media platforms

<hr>

6. What are the goals of your business? Which marketing strategies would offer the best ways to meet those goals?
<br>

- Increase sales and customer base
- Establish the store as a go-to source for fiction, fantasy, and sci-fi books
- Build a community of engaged readers
- Marketing strategies:
- Content marketing (blog posts, videos, podcasts)
- Social media marketing, especially on Instagram and TikTok
- Influencer partnerships with BookTubers or Bookstagrammers
- Email marketing for personalized recommendations and offers
- SEO optimization to improve visibility in search results
- Retargeting ads to re-engage visitors who didn't make a purchase

<hr>

7. Would your business have a budget to spend on advertising? Or would it need to work with free or low cost options to market itself?
<br>

Paid (small budget):
<br>

- Targeted social media ads on Facebook and Instagram
- Sponsored posts with mid-tier book influencers

Free:
<br>

- Organic social media growth
- Content marketing through our blog and social channels
- Email marketing to our subscriber list

Long-term:
<br>

- Partnerships with authors for virtual events or Q&As
- Participation in online book communities and forums

<details><summary><b>Facebook Mockup</b></summary>

![Facebook Mockup](readme/assets/images/wireframes/FB_mockup.PNG)

</details><br/>

</details><br/>

</details><br/>


[Back to top](<#table-of-content>)

<hr>


## Project Management

### Github Board
For organizing and planning my project, I have used the [Github board](https://github.com/users/Mienjung97/projects/9/views/1), which has helped me a lot with planning out and fulfilling the acceptance criterias. I have thoroughly kept the user stories up to date with the coding progress. Additionally, I have used multiple .txt files to keep up with ideas, documentation, my mentor meetings and bugs to implement in this documentation. 

<details><summary><b>Github Board</b></summary>

<br>
This picture does not show all user stories. Visit my Github board (link above) to see all user stories.
<br>
<br>

![User Stories](readme/assets/images/github_board.PNG)

![User Story Example](readme/assets/images/user_story_example.PNG)

</details><br/>

## Database Schema


The database schema was created with [BugBytes](https://www.youtube.com/watch?v=qzrE7cfc_3Q&t=478s) YouTube video and the corresponding tool [dreampuf](https://dreampuf.github.io/GraphvizOnline/). Due to health issues I could not completely follow my time plan, therefore I was unable to create a database schema myself, which was planned to be done with [Lucid](https://lucid.app/documents#/home?folder_id=recent).

* **Product** - Handles all products
* **Author** - Handles all authors - connected to the product model
* **Categories** - Handles all categories - connected to the product model
* **Cover** - Handles the cover types available - connected to the product model
* **Order** - Handles all orders
* **OrderLineItem** - Handler between the products and a users order for checkout
* **Profile** - Handles the user profile information (full name, delivery information and order history for the specific user). There is a one-to-one relation to the user model to connect it to the standard user model.
* **About** - Handles the about information provided through the admin panel
* **FAQ** - Handles all frequently asked questions
* **Contact** - Handles all contact requests and sends them to the admin panel
* **All-Auth** - Various models included due to all-auth that handle users, email addresses and more

<details><summary><b>Database Schema (Auto generated)</b></summary>
<br>

![Database Schema](readme/assets/images/graphviz.png)
</details><br/>


# User Experience (UX)

## Wireframes
The wireframes for the site were created in the software [Balsamiq](https://balsamiq.com). The wireframes have been created for desktop, tablet and mobile devices. The text content wasn't finalized during the wireframe process. Also I have decided to only focus on the user side since the admin frontend capabilities are less important for styling. For the Facebook mock up i have used the provided template from [Code Institute](https://codeinstitute.net/)

<details><summary><b>Wireframes: Home</b></summary>

![Wireframes Home Desktop](readme/assets/images/wireframes/home_wf.PNG)

[Back to top](<#table-of-content>)

</details><br/>

<details><summary><b>Wireframes: Products</b></summary>

![Wireframes Products Desktop](readme/assets/images/wireframes/products_wf.PNG)

[Back to top](<#table-of-content>)

</details><br/>

<details><summary><b>Wireframes: Product Detail View</b></summary>

![Wireframes Product Detail View Desktop](readme/assets/images/wireframes/product_detail_wf.PNG)

[Back to top](<#table-of-content>)

</details><br/>

<details><summary><b>Wireframes: Authors</b></summary>

![Wireframes Authors Desktop](readme/assets/images/wireframes/authors_wf.PNG)

[Back to top](<#table-of-content>)

</details><br/>

<details><summary><b>Wireframes: Profile</b></summary>

![Wireframes Profile](readme/assets/images/wireframes/profile_wf.PNG)

[Back to top](<#table-of-content>)

</details><br/>

<details><summary><b>Wireframes: About</b></summary>

![Wireframes About Desktop](readme/assets/images/wireframes/about_wf.PNG)

[Back to top](<#table-of-content>)
)
</details><br/>

<details><summary><b>Wireframes: FAQ</b></summary>

![Wireframes FAQ Desktop](readme/assets/images/wireframes/faq_wf.PNG)

[Back to top](<#table-of-content>)

</details><br/>

<details><summary><b>Wireframes: Contact Us</b></summary>

![Wireframes Contact Us Desktop](readme/assets/images/wireframes/contact_wf.PNG)

[Back to top](<#table-of-content>)

</details><br/>

<details><summary><b>Wireframes: Newsletter</b></summary>

![Wireframes Newsletter Desktop](readme/assets/images/wireframes/newsletter_wf.PNG)

[Back to top](<#table-of-content>)

</details><br/>

<details><summary><b>Facebook Mockup</b></summary>

![Facebook Mockup](readme/assets/images/wireframes/FB_mockup.PNG)

[Back to top](<#table-of-content>)

</details><br/>

## User Stories

<details><summary><b>Site User</b></summary>

### Site User
|  | | |
|:-------:|:--------|:--------|
| As a Site User | I can enter the page on the 'home' page so that I can see bestsellers and new books immediately | &check; |
| As a Site User | I can see all products and sort them to my preferences so that I can browse all books to see what is interesting for me | &cross; |
| As a Site User | I can view detailed information about a book so that I can make an informed purchase decision | &check; |
| As a Site User | I can browse books by categories so that I can find books I'm interested in | &check; |
| As a Site User | I can sort by categories so that I can search for books which category interests me | &check; |
| As a Site User | I can use a search function so that I can find specific books quickly | &check; |
| As a Site User | I can access an authors page so that I can serach for books from a specific author | &check; |
| As a Site User | I can see pictures and infos about authors so that I can get background info on who wrote the book | &check; |
| As a Site User | I can create an account so that I can make purchases and access personalized features | &check; |
| As a Site User | I can log in to my account so that I can access my profile | &check; |
| As a Site User | I can view my order history so that I can track the status of my current and past orders | &check; |
| As a Site User | I can add books to my shopping cart so that I can purchase multiple items at once | &check; |
| As a Site User | I can edit the contents in the shopping cart so that I do not buy items or quantities I do not want | &check; |
| As a Site User | I can proceed through an easy checkout process so that I can complete my purchase without problems | &check; |
| As a Site User | I can safely process payments so that my financial information is secure | &check; |
| As a Site User | I can enter and save my delivery information in my profile so that I can use it for future purchases | &check; |
| As a Site User | I will get an email confirmation after a purchase so that I know the order has been placed and I get additional info about it | &check; |
| As a Site User | I can reset my password so that I am not excluded from the page if I forgot my old password | &check; |
| As a Site User | I can access a contact form so that I can submit questions or feedback to the bookstore | &check; |
| As a Site User | I can access the FAQ page so that I get all answers to frequently asked questions | &check; |
| As a Site User | I can view an 'About Us' page so that I can learn more about the bookstore and its expertise | &check; |
| As a Site User | I can subscribe to a newsletter so that I can receive updates about new releases and promotions | &check; |
| As a Site User | I cannot access an invalid url so that a custom error page will give me the information on what went wrong | &check; |
| As a Site User | I can receive a discount and/or free shipping when my purchase exceeds a certain amount so that I am encouraged to place larger orders | &check; |


</details><br/>

<details><summary><b>Site Admin</b></summary>


### Site Admin

|  | | |
|:-------:|:--------|:--------|
| As a Site Admin | I can add new books to the store and remove old ones so that I can keep the catalog up-to-date | &check; |
| As a Site Admin | I can create and manage book categories so that I can keep the store organized | &check; |
| As a Site Admin | I can manage user accounts so that there are no unwatend customers | &check; |
| As a Site Admin | I can manage the content of the "About Us" page and other static pages so that I can keep the information current | &check; |
| As a Site Admin | I can change questions and answers for the FAQ page so that I do not have to go through the admin panel | &check; |

</details><br/>

<details><summary><b>Developer</b></summary>

### Deleloper

|  | | |
|:-------:|:--------|:--------|
| As a Developer | I can implement SEO best practices so that the website ranks higher in search engine results | &check; |
| As a Developer | I can implement secure coding practices so that the application is protected against common vulnerabilities | &check; |

</details><br/>

<details><summary><b>Epics</b></summary>

### Epics

The following describes the epics of which each user story has one. To see which user story has which epic, please visit the [Github board](https://github.com/users/Mienjung97/projects/9/views/1).

* Epic 1: User Authentication and Profile Management
* Epic 2: Product Browsing and Search
* Epic 3: Shopping Cart and Checkout
* Epic 4: Order Management
* Epic 5: Content Management
* Epic 6: Marketing and Communication
* Epic 7: Admin Functionality
* Epic 8: Security and Authentication

</details><br/>

[Back to top](<#table-of-content>)

## Site Structure

Books and Giggles has been designed so that any user can access every feature without having a profile (User profile and order history excluded), including ordering. The website also has been structured so that every feature works on all screen sizes. 

When a user enters the site, the header has all navigation elements and the body displays a simple text and a caroussel, each redirecting the user towards the corresponding product page. The user can also access every books detail page or get information about the authors on the "Authors" page.

The admin has multiple front end admin capabilities, like adding, editing or deleting products, authors and FAQ items, as well as adding categories. Through the admin panel to which a superuser has a direct button, every other functionality, like recieving the contact requests, is available. 

## Design Choices

### Color Scheme
The color scheme, as well as the styling ideas were developed while coding to mimic the colors of books, paper and bindings

[Coolors](https://coolors.co/) was used to create the color palette:

<details><summary><b>Color Palette</b></summary>
<br>
<br>

![Color Palette image](readme/assets/images/colors.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Typography
The fonts used for the site are 'Playfair Display'. Fallback font is sans-serif.

'Playfair Display' is used on the whole webpage. Choosing this font family was because I thought it would fit the theme.

<details><summary><b>Playfair Display</b></summary>
<br>
<br>

![Google Fonts Playfair Display](readme/assets/images/fonts.PNG)

</details><br/>

[Back to top](<#table-of-content>)

# Features
This section is devided in [Existing Features](<#existing-features>) and [Future Features](<#future-features>) since there are more features needed for the production ready page.

## Existing Features

This section will be devided into multiple sub sections:

## Navigational Features

<details><summary><b>Open</b></summary>

### Navigation
The styling of the navigation bar was heavily influenced by the [Boutique ADO](https://boutique-ado-mj-102bd7708d45.herokuapp.com/) walkthough website, while I tried to keep it as clean as possible. The only differences are between Admins and any other users - in addition to the usual navigation, the admin also has a "Product Management" option in the profile dropdown.

The following is devided into mobile and desktop views, showing how each individual dropdown menu looks according to the screen size:

<details><summary><b>Navigation Large</b></summary>

* Main Navigation:

![Navigation](readme/assets/images/features/nav-bar-bg.PNG)

* Dropdown Books

![Dropdown Books](readme/assets/images/features/books_dd_bg.PNG)

* Dropdown Categories

![Dropdown Categories](readme/assets/images/features/categories_dd_bg.PNG)

* Dropdown About Us

![Dropdown About Us](readme/assets/images/features/about_dd_bg.PNG)

* Dropdown Profile

![Dropdown Profile](readme/assets/images/features/account_dd_bg.PNG)

* Dropdown Profile Admin

![Dropdown Profile Admin](readme/assets/images/features/account_admin_dd_bg.PNG)

[Back to top](<#table-of-content>)

</details><br/>


<details><summary><b>Navigation Small</b></summary>

* Small Navigation:

![Navigation Collapsed](readme/assets/images/features/nav_collapsed_sm.PNG)

* Small Navigation opened

![Navigation Open](readme/assets/images/features/nav_open_sm.PNG)

* Dropdown Books 

![Dropdown Books](readme/assets/images/features/nav_books_sm.PNG)

* Dropdown Categories 

![Dropdown Categories](readme/assets/images/features/nav_categories_sm.PNG)

* Dropdown About Us 

![Dropdown About Us](readme/assets/images/features/nav_about_sm.PNG)

* Dropdown Profile 

![Dropdown Profile](readme/assets/images/features/account_dd_sm.PNG)

* Dropdown Search 

![Dropdown Search](readme/assets/images/features/search_sm.PNG)

* Dropdown Profile Admin 

![Dropdown Profile Admin](readme/assets/images/features/account_admin_dd_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Footer
The desktop footer shows links to all social media platforms, as well as links for the contact and newsletter page. The latter ones are only in the main navigation for mobile screens available:

<details><summary><b>Footer</b></summary>

* Footer Dekstop

![Footer Dekstop](readme/assets/images/features/footer_bg.PNG)

* Footer Mobile

![Footer Mobile](readme/assets/images/features/footer_sm.PNG)

</details><br/>

[Back to top](<#table-of-content>)

</details><br/>


## General Features

<details><summary><b>Open</b></summary>

### Home
The home page is simplistic, easy to navigate and fully responsive: 

<details><summary><b>Home</b></summary>

* Home Dekstop

![Home Dekstop](readme/assets/images/features/home_bg.PNG)

* Home Mobile

![Home Mobile](readme/assets/images/features/home_sm.PNG)

* Delivery banner that informs the user about minimum order amount before getting free shipping

![Delivery Banner](readme/assets/images/features/delivery_banner_bg.PNG)

* Carousell that displays categories like "Bestsellers", "Our Recommendations" and more

![Home Carousell](readme/assets/images/features/carousell_bg.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Authors
The Authors page is simplistic, easy to navigate and fully responsive. It shows all authors that have a book the the store, including a small description and if it was available, a picture of the author (otherwise a placeholder image). When the user clicks the author, he will be redirected to a page that shows only books made by ckicked author. 

<details><summary><b>Home</b></summary>

* Authors Dekstop

![Authors Dekstop](readme/assets/images/features/authors_bg.PNG)

* Authors Mobile

![Authors Mobile](readme/assets/images/features/authors_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>


### About
The About page features a welcoming picture, as well as information about the store and its ideology. 

<details><summary><b>About</b></summary>

* About Dekstop

![About Dekstop](readme/assets/images/features/about_bg.PNG)

* About Mobile

![About Mobile](readme/assets/images/features/about_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### FAQ
On the FAQ page, an admin can add questions with their corresponding answer, so that users of the webpage always have their questions answered. The admin is encouraged to add questions that have been asked via the contact page to the FAQ page.

<details><summary><b>FAQ</b></summary>

* FAQ Dekstop Collapsed

![FAQ Dekstop Collapsed](readme/assets/images/features/faq.PNG)

* FAQ Dekstop Open

![FAQ Dekstop Open](readme/assets/images/features/faq_open.PNG)

* FAQ Mobile Open

![FAQ Mobile Open](readme/assets/images/features/faq_sm.PNG)


[Back to top](<#table-of-content>)

</details><br/>

### Contact Page
The Contact Us page features a a form which includes *Name*, *email*, *subject* and *message* that gets send directly towards the admin panel.

<details><summary><b>Contact Page</b></summary>

* Contact Dekstop

![Contact Dekstop](readme/assets/images/features/contact_bg.PNG)

* Contact Mobile

![Contact Mobile](readme/assets/images/features/contact_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Newsletter
The Newsletter used in this project was designed and set up with [Brevo](https://www.brevo.com/). At the moment, a user will only get a newsletter subscription confirmation email, but brevo allows to schedule outgoing emails and a variety of other possible marketing option.

<details><summary><b>Newsletter</b></summary>

* Newsletter Dekstop

![Newsletter Dekstop](readme/assets/images/features/newsletter_bg.PNG)

* Newsletter Mobile

![Newsletter Mobile](readme/assets/images/features/newsletter_sm.PNG)

* Newsletter Confirmation Mail

![Newsletter confirmation](readme/assets/images/newsletter_confirmation.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Products Page
The Products page shows all available books in the store with a picture, name of the book, the author, what kind of cover it has, all categories it belongs to and the price of the item. The user has to click on the cover picture to get redirected to the detail view. The products page is devided into 4 collumns, which are getting reduced to just one collumn, depending on the screen size.

<details><summary><b>Products Page</b></summary>

* Products Dekstop

![Products Dekstop](readme/assets/images/features/products_bg.PNG)

* Products Tablet Big

![Products Tablet Big](readme/assets/images/features/products_t_bg.PNG)

* Products Tablet Small

![Products Tablet Small](readme/assets/images/features/products_t_sm.PNG)

* Products Mobile

![Products Mobile](readme/assets/images/features/products_sm.PNG)

* Product Search Dekstop

![Product Search Dekstop](readme/assets/images/features/product_search.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Product Detail Page
In the Product detail Page, the user gets all the information of each individual item. Not every book has all fields filled out, but mostly, all of the fields are filled out. 

The fields which are available:

* Picture
* Name
* Author
* SKU
* Price
* Page count
* Publisher
* Year published
* ISBN
* Description1
* Description2
* Extra Info
* Type of cover

<details><summary><b>Product Detail View</b></summary>

* Product Detail View Dekstop

![Product Detail View Dekstop](readme/assets/images/features/product_detail_bg.PNG)

* Product Detail View Mobile

![Product Detail View Mobile](readme/assets/images/features/product_detail_sm.PNG)

<details><summary><b>Sorting</b></summary>
The user has the option to sort by price, name and author, both in ascending and descending order.


* Dekstop Sorting high to low price

![Newsletter Dekstop](readme/assets/images/features/sorting_high_low.PNG)

* Dekstop Sorting low to high price

![Newsletter Mobile](readme/assets/images/features/sorting_low_high.PNG)

* Dekstop Sorting

![Dekstop Sorting](readme/assets/images/features/sort_bg.jpg)

* Mobile Sorting

![Mobile Sorting](readme/assets/images/features/sort_sm.jpg)

</details><br/>

</details><br/>

[Back to top](<#table-of-content>)

</details><br/>

## E-commerce Features

<details><summary><b>Open</b></summary>

### Shopping Bag
The shopping bag does exactly what a shopping bag should do: You can add and remove items, as well as adjusting the quantity of each item in the bag. The bag displays the nessesary information about the product or products the user would like to purchase like name, picture and price. Depending on mobile or desktop view, the layout is a bit different, to make the process to the checkout page as easy as possible. The shopping bag also informs the user about delivery costs or if the minimum for free delivery has been reached.

<details><summary><b>Shopping Bag</b></summary>

* Shopping Bag Dekstop: Empty

![Shopping Bag Dekstop](readme/assets/images/features/shopping_bag_empty_bg.PNG)

* Shopping Bag Dekstop: No delivery cost

![Shopping Bag Dekstop](readme/assets/images/features/shopping_bag_no_delivery_bg.PNG)

* Shopping Bag Dekstop: Delivery cost

![Shopping Bag Dekstop](readme/assets/images/features/shopping_bag_delivery_bg.PNG)

* Shopping Bag Mobile: Empty

![Shopping Bag Mobile](readme/assets/images/features/shopping_bag_empty_sm.PNG)

* Shopping Bag Mobile: No delivery cost

![Shopping Bag Mobile](readme/assets/images/features/shopping_bag_no_delivery_sm.PNG)

* Shopping Bag Mobile: Delivery cost

![Shopping Bag Mobile](readme/assets/images/features/shopping_bag_delivery_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Checkout
In the checkout view, the user has to provide their name, email, shipping details and credit card details. If the user already has a profile, they can save the information to their profile or if they have already filled out all infos, either through an earlier purchase or by filling out the profile form manually, the checkout form will be pre populated (excluding the payment information).

<details><summary><b>Checkout</b></summary>

* Checkout Dekstop

![Checkout Dekstop](readme/assets/images/features/checkout_bg.PNG)

* Checkout Mobile

![Checkout Mobile](readme/assets/images/features/checkout_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Checkout Success
The checkout success page provides the user with their order details, including an order summary, order number and the info that a confirmation mail will be send to the by the user provided email address.

<details><summary><b>Checkout Success</b></summary>

* Checkout Success Dekstop

![Checkout Success Dekstop](readme/assets/images/features/checkout_success_bg.PNG)

* Checkout Success Mobile

![Checkout Success Mobile](readme/assets/images/features/checkout_success_sm.PNG)

</details><br/>

[Back to top](<#table-of-content>)

## Profile Features

<details><summary><b>Open</b></summary>


### Register
The sign up page is a modified all auth template that fullfills the basic "sign up" features like email and password input and validation and a user name. Also it gives the user twice the option to change to the "sign in" page.

<details><summary><b>Register</b></summary>

* Sign up Desktop

![Sign up Dekstop](readme/assets/images/features/signup_bg.PNG)

* Sign up Mobile

![Sign up Mobile](readme/assets/images/features/signup_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Log In
The Log in page is a modified all auth template that fullfills the basic "sign in" features. The user has to provide an email or username as well as their password. Also it gives the user the option to change to the "sign up" page or to reset their password.

<details><summary><b>Sign In</b></summary>

* Sign In Desktop

![Sign In Dekstop](readme/assets/images/features/signin_bg.PNG)

* Sign In Mobile

![Sign In Mobile](readme/assets/images/features/signin_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Logout
The Logout page is a modified all auth template that fullfills the basic "logout" features - it loggs the user out.

<details><summary><b>Logout</b></summary>

* Logout Dekstop

![Logout Dekstop](readme/assets/images/features/signout_bg.PNG)

* Logout Mobile

![Logout Mobile](readme/assets/images/features/signout_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>


### Reset Password
The Reset Password page is a modified all auth template that fullfills the basic "Reset Password" features. A user must provide their email and will get an email with a link to reset their password

<details><summary><b>Reset Password</b></summary>

* Reset Password Dekstop

![Logout Dekstop](readme/assets/images/features/reset_pw_bg.PNG)

* Reset Password Mobile

![Logout Mobile](readme/assets/images/features/reset_pw_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>


### Profile
The profile page consists of two parts: The users profile info, including name, email and shipping address and as the second part the order history. If a user clicks on one of the order history items, they will be rediredted to the corresponding checkout success page.

<details><summary><b>Profile</b></summary>

* Profile Dekstop

![Profile Dekstop](readme/assets/images/features/profile_page_bg.PNG)

* Profile Mobile

![Profile Mobile](readme/assets/images/features/profile_page_sm.PNG)

* Change Password 

![Change Password](readme/assets/images/features/change_pw.PNG)

</details><br/>

[Back to top](<#table-of-content>)

</details><br/>

</details><br/>

## Confirmation Features

<details><summary><b>Open</b></summary>

### Pop Up Messages
There are a variety of different Pop Up messages - depending on what the user (or admin) wants to do, most functionalities are connected to a notification. In general, there are different types of messages:

* Success messages: any action the user does which requires a positive feedback, like adding items to the cart, logging in or an admin updates the database successfully
* Info messages: mostly admin related, which informs about editing the database, or when a user clicks a past oder summary
* Warning message: for endusers, this only appears when the stripe public key is missing - the admin will be presented with this message if they want to delete a product or author
* Error message: this message either informs the user about an error that occured, or if a normal user tries to use an admin path
* Newsletter error message: if the user enters an invalid email format, an error message will appear
* Newsletter success message: if the user subscribes to the newsletter, a success message will appear

Site note: the admin success messages look different than for the users: users only get success confirmation for interacting with the store, so they will be shown a summary of their shopping bag, while the admin does not get the preview (reason: the admin gets success messages more frequently and usually does not shop in their own store).

Below you can see some examples, more are in this [folder](readme/assets/images/features/msg/).

<details><summary><b>Messages</b></summary>

* Success Message without shopping bag

![Success Message](readme/assets/images/features/msg/msg_success_signin.PNG)

* Success Message: Shopping bag with delivery cost

![Success Message](readme/assets/images/features/msg/msg_success_add_to_bag_delivery.PNG)

* Success Message: Shopping bag without delivery cost

![Success Message](readme/assets/images/features/msg/msg_success_add_to_bag_no_delivery.PNG)

* Info Message: Order history

![Info Message](readme/assets/images/features/msg/msg_alert_order_history.PNG)

* Warning Message: Deleting a product

![Warning Message](readme/assets/images/features/msg/msg_warning_product.PNG)

* Error Message: Wrong path

![Warning Message](readme/assets/images/features/msg/msg_error.PNG)

* Newsletter Error / Success Message (There is a visual bug in the desktop version, more in the "Bugs" section)

![Warning Message](readme/assets/images/features/msg/newsletter_error_sm.PNG)

![Warning Message](readme/assets/images/features/msg/newsletter_success_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Confirmation Emails
When a user registers, they have to confirm their email address with a link they will be provided with in an email. Also if a user places an order, they will get an email confirmation with the details of the order.

<details><summary><b>Confirmation Emails</b></summary>

* Confirm email address

![Confirm Email Address](readme/assets/images/features/email_confirm_account.PNG)

* Order summary email

![Order Summary Email](readme/assets/images/features/email_order_summary.PNG)

</details><br/>

[Back to top](<#table-of-content>)

</details><br/>


## Admin Features

<details><summary><b>Open</b></summary>

### Product Management
When a superuser is logged in, they will get another item in the account dropdown labled "Product Management". On this page, they have the option to navigate to the admin panel without having to modify the url and to add a product, category, author or a FAQ item.

<details><summary><b>Product Management</b></summary>

* Desktop Product Management Panel

![Desktop Product Management Panel](readme/assets/images/features/product_management_bg.PNG)

* Mobile Product Management Panel

![Mobile Product Management Panel](readme/assets/images/features/product_management_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Add Product
This is the front end page where an admin can add a product.

<details><summary><b>Add Product</b></summary>

* Add Product Full Form

![Add Product Full Form](readme/assets/images/features/add_product_form.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Edit Product
This is the front end page where an admin can edit a product. The button on the product detail page works visually the same as the "Delete FAQ" button

<details><summary><b>Edit Product</b></summary>

* Edit Product Form

![Edit Product Form](readme/assets/images/features/edit_product.PNG)

* Edit Product Button

![Edit Product](readme/assets/images/features/edit_product_btn.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Delete Product
This is the front end page where an admin can delete a product.

<details><summary><b>Delete Product</b></summary>

* Desktop Delete Product Confirmation Page

![Desktop Delete Product Confirmation Page](readme/assets/images/features/delete_product_bg.PNG)

* Mobile Delete Product Confirmation Page

![Mobile Delete Product Confirmation Page](readme/assets/images/features/delete_product_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Add Author
This is the front end page where an admin can add an author. All "Add ..." forms are only shown as desktop version, the mobile versions look like the "Add Category" mobile view.

<details><summary><b>Add Author</b></summary>

* Add Author

![Desktop Add Author](readme/assets/images/features/add_author.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Edit Author
This is the front end page where an admin can edit an author.

<details><summary><b>Edit Author</b></summary>

* Desktop Edit Author

![Desktop Edit Author](readme/assets/images/features/edit_author_bg.PNG)

* Mobile Edit Author

![Mobile Edit Author](readme/assets/images/features/edit_author_sm.PNG)

* Edit / Delete Author Button

![Edit Author Button](readme/assets/images/features/author_admin_btn.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Delete Author
This is the front end page where an admin can delete an author.

<details><summary><b>Delete Author</b></summary>

* Desktop Delete Author

![Desktop Delete Author](readme/assets/images/features/delete_author_bg.PNG)

* Mobile Delete Author

![Mobile Delete Author](readme/assets/images/features/delete_author_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Add Category
This is the front end page where an admin can add a category. This form is shown in the mobile view as an example on how the other "Add ..." forms look like on a mobile view

<details><summary><b>Add Category</b></summary>

* Mobile Add Category

![Mobile Add Category](readme/assets/images/features/add_category_sm.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Add FAQ
This is the front end page where an admin can add a FAQ item.

<details><summary><b>Add FAQ</b></summary>

* Desktop Add FAQ Item

![Desktop Add FAQ Item](readme/assets/images/features/add_faq.PNG)

* Desktop Add FAQ Frontend Button

![Desktop Add FAQ Frontend Button](readme/assets/images/features/add_faq_btn.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Edit FAQ
This is the front end page where an admin can add a FAQ item.

<details><summary><b>Edit FAQ</b></summary>

* Desktop Edit FAQ Item

![Desktop Edit FAQ Item](readme/assets/images/features/edit_faq.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Delete FAQ
Deleting an FAQ item is the only front end delete option that does not have its own confirmation page, just a "Delete" button. The reason for this is that deleting an FAQ item vy accident, it only has a small impact on the website and can be re implemented quite easy. Deleting an author or a product would have bigger consequences, therefore they have the delete page.

<details><summary><b>Delete FAQ</b></summary>

* Desktop Delete FAQ Button

![Desktop Delete FAQ Button](readme/assets/images/features/faq_delete.PNG)

* Desktop Delete FAQ Button Hovered

![Desktop Delete FAQ Button Hovered](readme/assets/images/features/faq_delete_hover.PNG)

[Back to top](<#table-of-content>)

</details><br/>


### Admin Panel
On the admin panel, an admin can access all profiles, email addresses, order, products and every other model. Everything has full CRUD functionality, so all features that do not have a corresponding front end page can be modified here.

<details><summary><b>Admin Panel</b></summary>

* Desktop Admin Panel

![Desktop Admin Panel](readme/assets/images/features/admin_panel.PNG)

</details><br/>

[Back to top](<#table-of-content>)

</details><br/>

</details><br/>

## Future Features

### Marketing

* For a live website, future features include all the marketing ideas I came up with in in the marketing challange
* An extension of the newsletter: Besides only getting a confirmation email, I would implement another email, timed possibly 24 hours after signing up, giving some sort of discount to make the user come back to the page. Also a bi-weekly or monthly newsletter should be implemented

### Features

* Adding the remaining user stories
* Admin capability: Responding to contact requests via the website
* Bugfixes (see "Bugs" section)
* Adding a "Back to log in" button to the confirmation page which a user gets after resetting their password
* Implementing some kind of discounts or loyalty rewards (user story)
* Add a contact us modification so that the user gets the notification via email with their whole request
* Change the Product model so that the cover is non nullable
* Add e-books to the stores inventory
* Implement a function that keeps track of the inventory so that an admin can specify on how many products are available
* Extend the search function to also include the FAQ and About page
* If an admin deletes an author or category, corresponding relations between the deleted models and the products should be applied
* Adding an "Out of stock" label which disables the possibility to order an item, but it can still be displayed on the page

[Back to top](<#table-of-content>)

# Technologies Used

## Languages

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the site.
* [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website

## Frameworks & Software

* [Bootstrap](https://getbootstrap.com/) - A CSS framework that helps building solid, responsive, mobile-first sites
* [Django](https://www.djangoproject.com/) - A model-view-template framework used to create the Books and Giggles site
* [Balsamiq](https://balsamiq.com/) - Used to create the wireframe
* [Github](https://github.com/) - Used to host and edit the website
* [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal in [Gitpod](https://www.gitpod.io) used to push changes to the GitHub repository
* [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used to test performance of site
* [Multi Mockup](https://techsini.com/multi-mockup/) - Used for responsiveness check
* [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) - Used to create a *.dot file of all models in the project
* [dreampuf](https://dreampuf.github.io/GraphvizOnline/) - Creates visually appealing database diagrams of *.dot files
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to debug and test responsiveness
* [AWS](https://aws.amazon.com/) - Amazon Web Services - used to host all static files and pictures from the project in a S3 Bucket
* [Stripe](https://stripe.com/) - A service provider to handle all payments on the website
* [HTML Validation](https://validator.w3.org/) - Used to validate HTML code
* [CSS Validation](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
* [PEP8CI Validation](https://pep8ci.herokuapp.com/) - Used to validate the Python Code
* [JSHint Validation](https://jshint.com/) - Used to validate JavaScript code

[Back to top](<#table-of-content>)

## Libraries
The libraries used in this project are located in the requirements.txt file and have been documented below

* [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI
* [boto3](https://pypi.org/project/boto3/) - Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2. Boto3 is maintained and published by Amazon Web Services
* [botocore](https://pypi.org/project/botocore/) - A low-level interface to a growing number of Amazon Web Services. The botocore package is the foundation for the AWS CLI as well as boto3. Botocore is maintained and published by Amazon Web Services
* [click](https://pypi.org/project/django-click/) - django-click is a library to easily write Django management commands using the click command line library
* [Colorama](https://pypi.org/project/colorama/) - Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows
* [crispy-bootstrap4](https://pypi.org/project/crispy-bootstrap4/) - Bootstrap5 template pack for django-crispy-forms
* [CSSbeautifier](https://pypi.org/project/cssbeautifier/) - Beautify, unpack or deobfuscate CSS
* [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/) - This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application
* [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
* [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
* [django-countries](https://pypi.org/project/django-countries/) - A Django application that provides country choices for use with forms, flag icons static files, and a country field for models
* [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) - Used to integrate Django DRY forms in the project
* [django-extensions](https://pypi.org/project/django-extensions/) - Django Extensions is a collection of custom extensions for the Django Framework
* [django-storages](https://pypi.org/project/django-storages/) - django-storages is a project to provide a variety of storage backends in a single library
* [django-summernote](https://pypi.org/project/django-summernote/) - Summernote is a simple WYSIWYG editor which allows you to embed Summernote into Django very handy. Support admin mixins and widgets
* [djLint](https://pypi.org/project/djlint/) - djLint is a community build project to and add consistency to html templates
* [EditorConfig](https://pypi.org/project/EditorConfig/) - EditorConfig makes it easy to maintain the correct coding style when switching between different text editors and between different projects. The EditorConfig project maintains a file format and plugins for various text editors which allow this file format to be read and used by those editors
* [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy
* [html-tag-names](https://pypi.org/project/html-tag-names/) - This is a list of HTML tag names. It includes ancient (for example, nextid and basefont) and modern (for example, shadow and template) names from the HTML living standard. The repo includes scripts to regenerate the data from the specs
* [html-void-elements](https://pypi.org/project/html-void-elements/) - Similar to "html-tag-names"
* [jmespath](https://pypi.org/project/jmespath/) - JMESPath (pronounced “james path”) allows you to declaratively specify how to extract elements from a JSON document
* [jsbeautifier](https://pypi.org/project/jsbeautifier/) - Beautify, unpack or deobfuscate JavaScript. Handles popular online obfuscators
* [oauthlib](https://pypi.org/project/oauthlib/) - OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework
* [pathspec](https://pypi.org/project/pathspec/) - pathspec is a utility library for pattern matching of file paths. So far this only includes Git’s wildmatch pattern matching which itself is derived from Rsync’s wildmatch. Git uses wildmatch for its gitignore files
* [pillow](https://pypi.org/project/pillow/) - The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities
* [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
* [PyJWT](https://pypi.org/project/PyJWT/) - A Python implementation of RFC 7519
* [python3-openid](https://pypi.org/project/python3-openid/) - OpenID support for modern servers and consumers
* [regex](https://pypi.org/project/regex/) - This regex implementation is backwards-compatible with the standard ‘re’ module, but offers additional functionality like enabling other Python threads to run concurrently
* [requests-oauhlib](https://pypi.org/project/requests-oauthlib/) - Provides first-class OAuth library support for Requests
* [s3transfer](https://pypi.org/project/s3transfer/) - S3transfer is a Python library for managing Amazon S3 transfers. This project is maintained and published by Amazon Web Services
* [sqlparse](https://pypi.org/project/sqlparse/) - sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements
* [stripe](https://pypi.org/project/stripe/) - A Python library for Stripe’s API
* [tqdm](https://pypi.org/project/tqdm/) - Instantly make your loops show a smart progress meter when coding in the console

[Back to top](<#table-of-content>)

# Testing

## Testing User Stories

## Code Validation
The code on the 'Books and Giggles' site has been tested through W3C Markup Validation Service, W3C CSS Validation Service, JSHint and the CodeInstutute pep8 validator. A few errors were found the W3C Markup Validation Service but could either be quite easily fixed (see bugs section) or have to do with third party code, especially Stripe, AWS and Brevo. 

### Markup Validation
While validating the HTML code, I encountered only a few errors. Since the Markup validator is not an admin user, I could only validate the pages availabe for endusers via url input - so with use of the chrome developer tools I validated every admin related page via direct input. The only errors that came up are due to third party code. Proof for all validations are in this [folder](readme/assets/images/validation/html). From my previous project, I know that summernote, wich I use for the "About" page, can throw "font element" errors, which might not be included since I have not updated the content on the "About" page yet.

The following shows some validations, especially the ones that had an error:


<details><summary><b>HTML Validation URL input</b></summary>

Password Change (Errors):

![HTML Result Password Change](readme/assets/images/validation/html/pw_change_html_val.PNG)

Home page (Warnings):

![HTML Result Home Page](readme/assets/images/validation/html/home_html_val.PNG)

Newsletter page (no errors or warnings):

![HTML Result About Page](readme/assets/images/validation/html/newsletter_html_val.PNG)

</details><br/>

<details><summary><b>HTML Validation direct input</b></summary>

Admin pages via direct input:

Product Management page (Errors):

![HTML Result Checkout Page](readme/assets/images/validation/html/product_management_html_val.PNG)

Checkout page (Errors):

![HTML Result Checkout Page](readme/assets/images/validation/html/checkout_html_di_val.PNG)

Delete author page (Errors):

![HTML Result Delete Author](readme/assets/images/validation/html/delete_author_html_val.PNG)


</details><br/>

[Back to top](<#table-of-content>)

### CSS Validaton
When validating my own code the W3C CSS Validator reports no errors. The only errors shown are via url input, which have to do with the third party newsletter provider

<details><summary><b>CSS Validation Result</b></summary>

base.css:

![CSS Result](readme/assets/images/validation/static/css/base_val.PNG)

profile.css:

![CSS Result](readme/assets/images/validation/static/css/profile_css_val.PNG)

checkout.css:

![CSS Result](readme/assets/images/validation/static/css/checkout_css_val.PNG)

URL input:

![CSS Result](readme/assets/images/validation/static/css/url_css_val.PNG)
</details><br/>

[Back to top](<#table-of-content>)

### PEP Validation
To validate the python files, I have used the [pep8 CodeInstitute linter](https://pep8ci.herokuapp.com/) I have tested all python files in my project without getting any errors. The documentation can be found in the [folder](readme/assets/images/validation/python). Every picture is labled with the first word as the corresponding app and the name of the python file. 45 out of the 47 files reported no error - just the webhook.py file in the checkout app, as well as in the settings the "AUTH_PASSWORD_VALIDATORS" were longer than 79 lines. Both files have been fixed.

[Back to top](<#table-of-content>)

### JavaScript Validation
The JSHint validator results can be seen below, only 3 files are shown. the rest of the validation can be found in this [folder](readme/assets/images/validation/static/js)

No errors were returned when passing through JSHint, the tests reported undefined variables and gave out a total of 8 warnings. None of these are problematic. 

<details><summary><b>JSHint Validation Result</b></summary>

stripe_elemets:

![JSHint Validation Stripe](readme/assets/images/validation/static/js/stripe_elements_js_val.PNG)

Quantity input form:

![JSHint Validation Quantity Input](readme/assets/images/validation/static/js/quantity_input_js_val.PNG)

JS for the newsletter:

![JSHint Validation Newsletter](readme/assets/images/validation/static/js/newsletter_js_val.PNG)

[Back to top](<#table-of-content>)

</details><br/>

### Manual Testing

All the manual testing can be found in this [file](MANUAL_TESTING.md)

### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Multi Device Mockup Generator](https://techsini.com/multi-mockup/).

| Desktop    | Display <1200px       | Display >1200px    |
|------------|-----------------------|--------------------|
| Render     | pass                  | pass               |
| Images     | pass                  | pass               |
| Links      | pass                  | pass               |

| Tablet     | iPad Air              | Asus Zenbook Fold  | iPad Mini | iPad Pro |
|------------|-----------------------|--------------------|-----------|----------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

| Phone      | Galaxy S20 Ultra      | iPhone 12Pro/14 Pro Max    | Pixel 7 / 7 Pro      |
|------------|-----------------------|----------------------------|----------------------|
| Render     | pass                  | pass                       | pass      | pass     |
| Images     | pass                  | pass                       | pass      | pass     |
| Links      | pass                  | pass                       | pass      | pass     |

[Back to top](<#table-of-content>)

### Browser Compatibility
* Google Chrome Version (version 130.0.6723.117)
* Mozilla Firefox (version 132.0.1) - website works fully, but the both the fonts and some formatting is wrong
* Microsoft Edge (version 130.0.2849.80)

[Back to top](<#table-of-content>)

### Lighthouse
Google Lighthouse in Chrome Developer Tools was used to test the application within the areas of *Performance*, *Accessibility*, *Best Practices* and *SEO*. 

The test results have been mostly positive, besides the performance score (between x and y), as well as accessibility. The latter one has especially on the desktop version (all pages) and the shopping bag and product detail page issues, since there are labels missing for most buttons. I decided that this is not an issue for now since the products are not meant for the visually impaired. In the future features, I do want to implement these as well so that the page is also accessable for the visually impaired, so that they are also able to shop for books as e.g. gifts. 

I have tested every page from Books and Giggles with lighthouse, every picture can be found in this [folder](readme/assets/images/validation/lighthouse)

[Back to top](<#table-of-content>)

### Peer Review
Additional testing of the application was conducted by people outside of the software development field by friends and family. No errors and no issues with design or handling of the site were found. Also my webpage has been tested by fellow Code Insititute students Marcellio and Jan with the same result.

[Back to top](<#table-of-content>)

# Bugs

## Fixed Bugs

**10.10.24**
Cloned my project to another private repo to try out models and products fixtures (to not create problems in real repo) -> Had issues with the database and migrations -> with tutor support I was able to delete the db and implement the new models and test fixtures

**17.10.24**
after the clone, I had a copy of my project in my project -> deleted it after research on if that would create problems in the project (it did not)

**18.10.24**
For search queries, since author and category are own models, the search didnt work -> included classes in the view with name and friendly name -> this gave duplicate resulats, therefore distinct() function was added to new "products" variable

**19.10.24**
Sorting after category -> shows more products than in the store (duplicate books) -> will tackle later -> Deleted sorting option

**23.10.24**
Stripe will not work as intended - in webhook_handler I renamed "shopping_bag" to "bag" while getting the metadata, but set the following variables as "shopping_bag" -> name error -> fixed the code

**04.11.24**
When trying to edit a product, the edit author page appears -> URL mistake. Fix: Edited the urls.py file

**09.11.2024**
I want to make author friendly_name mandatory for added models Fix: make friendls_name nullable, then run "python3 manage.py makemigrations products --empty" -> migrate by hand (help by AI and Tutor Support)

### Bugs from Boutique ADO

**30.10.24**
Minus quantity button does not work. Fix: in JS code, change targeted IDs to target classes -> change "#" to "." to target classes -> did not fix the issue:

**13.11.2024**
Finally fixed the quantity_input_form JS code with the help of Oisin from tutor support by rewriting all variables

**11.11.2024**
Validation errors:

* Mobile-top-header throws HTML errors: li item is child of menu item. Fix: Add an ul tag with corresponding classes (Tutor support helped)
* Element p not allowed as child of element strong in this context. -> custom_clearable_file_input has that set up. Solution: removed "strong"
* custom_clearable_file_input: "Error: Bad value auto !important for attribute width on element img: Expected a digit but saw a instead" -> added a div -> did not fix the error

[Back to top](<#table-of-content>)

## Known Bugs

All known bugs are supposed to be fixed before "Future Features" are going to be implemented.

* if the user changes the quantity of an item in the shopping bag to 0, 0 amount of items will be ordered, but it will still show up in the order summary and confirmation mail as "0x book"
* If a user has saved their name and email once in the checkout form and saves it, it will save it to their profile, but not to the details, if they want to buy a new book -> identified the problem: checkout view is getting data from the django user model, not the profile data -> update view of checkout to get info from profile, then update profile model to change django user model when updated
* In the add_product page, the borders are not round like in every other form
* If a user clicks fast on "add to bag" button, the item will be added multiple times
* After coming to the checkout success page, when the user clicks the "Now check out our newst..." (redirect to multiple categories) button, the same issue as with the "categories" bug happens. Every book that has e.g. "Bestsellers" and "Our Recommendations" will be shown double
* If an admin would delete an author, the books would remain in the database, but cannot be ordered anymore -> Future feature because of time reasons -> If an author gets deleted, all the books written by them should also be deleted. The same issue applies to categories, but most books do have more than just one category
* The styling of the notifications from the Newsletter page are aligned wrongly on big displays - pictures can be found [here](readme/assets/images/features/msg/newsletter_success_bg.PNG) and [here](readme/assets/images/features/msg/newsletter_error_bg.PNG) 

[Back to top](<#table-of-content>)

# Deployment

## Deployment To Heroku

The project was deployed to [Heroku](https://www.heroku.com). Given that this is the fifth project to deploy, I will not go over the steps on creating a project in detail, since the steps have been the same as for all django projects. For information on how to create a project, go to the readme of my [PP4](https://github.com/Mienjung97/PROject-GOLFblog). 

To create a project, these are the steps:

1. Create a workspace with the [Code Institute Full Template](https://github.com/Code-Institute-Org/ci-full-template)

2. Install Django via console commands

3. Add the packages to the "requirements.txt" file 

4. Create the project

5. Create the first app

6. Add the app to the "INSTALLED_APPS" in the settings.py file

7. Run the server and retireve your local url

8. Add the local url to the "ALLOWED_HOSTS" area in the settings.py file

9. Run the initial migrations

Now, the project can be deployed to Heroku:

1. Create a Database from [CI](https://dbs.ci-dbs.net/)

2. Add your database information (see step 6, excluding the COLLECTSTATIC) to your env.py file and add the following code in the settings.py file:

<details><summary><b>Heroku Deployment - Step 2</b></summary>

![Heroku Deployment Step 2](readme/assets/images/deployment/database_settings_setup.PNG)
</details><br />

3. Prepare your project for deployment

* Install *gunicorn*
* Install *psycopg2*
* Add the packages to the "requirements.txt" file 
* Migrate all changes
* *If* the project already has more apps, models and fixtures, also load the fixtures via *python3 manage.py loaddata "fixture name"*

<details><summary><b>Heroku Deployment - Step 3</b></summary>

![Heroku Deployment Step 3](readme/assets/images/deployment/my_install_2.PNG)

![Heroku Deployment Step 3](readme/assets/images/deployment/my_install_1.PNG)
</details><br />

* Create a "Procfile" and add "web: gunicorn 'project name':application" in it
* Change *Debug* in the settings.py file to *False*
* Add "'.herokuapp.com'" to the "ALLOWED_HOSTS" area in the settings.py file
* Commit the changes to Github

4. Create a new heroku app

<details><summary><b>Heroku Deployment - Step 4</b></summary>

![Heroku Deployment Step 4](readme/assets/images/deployment/new_heroku.PNG)

![Heroku Deployment Step 4](readme/assets/images/deployment/new_app_heroku.PNG)
</details><br />

5. Connect your Github repository to your new Heroku app

<details><summary><b>Heroku Deployment - Step 5</b></summary>

![Heroku Deployment Step 5](readme/assets/images/deployment/deploy_github_connect.PNG)
</details><br />

6. Add your secret key, *DISABLE_COLLECTSTATIC = 1* and your newly created DATABASE_URL to the Heroku Config Vars

<details><summary><b>Heroku Deployment - Step 6</b></summary>

![Heroku Deployment Step 6](readme/assets/images/deployment/add_database_config_vars.PNG)
</details><br />

7. Make your first manual deploy

<details><summary><b>Heroku Deployment - Step 7</b></summary>

![Heroku Deployment Step 7](readme/assets/images/deployment/manual_deploy.PNG)
</details><br />

Now, the basics of your project have been deployed to Heroku. In my case, I continued with my project until I had stripe, AWS, all fixtures and all working models ready. 

The next step to complete the deployment is to create an AWS account and an S3 bucket. To create an account, you have to visit the [AWS website](https://aws.amazon.com/de/free/?gclid=CjwKCAiAudG5BhAREiwAWMlSjMCbGTv1ldd3uQuVgb76W5cnlECZ_byfnH2YGXwSWeKzQEnCoj3jYxoC2ukQAvD_BwE&trk=3f93bdb7-cca2-4053-94a7-a03fb33c9dfa&sc_channel=ps&ef_id=CjwKCAiAudG5BhAREiwAWMlSjMCbGTv1ldd3uQuVgb76W5cnlECZ_byfnH2YGXwSWeKzQEnCoj3jYxoC2ukQAvD_BwE:G:s&s_kwcid=AL!4422!3!696248420329!e!!g!!aws!19579657820!148952141007&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all) and follow the instructions to create the free tier account.

The best summary on how to do create the bucket and user group was provided by the Code Institute tutor Oisin with the following tutorials:

* [Create an AWS S3 Bucket](https://docs.google.com/document/d/1bqvCFiCW_JV9sllNZrN5uUJpIiusHICTk4TIk3oUWHY/edit?tab=t.0#heading=h.jypp4mbtvx4q)
* [Create an AWS Group and User](https://docs.google.com/document/d/1z6L8KKiTi3QU5rMbHXhA3QR9jQIG7wLqnScUDpe238E/edit?tab=t.0#heading=h.1ixuny26uvc)

# Credits

## Content

* This Readme file has been taken from my PP4 "[ROject GOLFblog](https://github.com/Mienjung97/PROject-GOLFblog). The readme for my previous project was taken from [Marcus Erikssons PP4](https://github.com/worldofmarcus/project-portfolio-4/blob/main/README.md#existing-features) and modified by me to fit my project.
    * *Marcus Erikssons*: "Template for read.me provided by Code Institute (*with some additional changes that my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/))* suggested."

* My project **Books and Giggles** has started almost as a copy of the example project *Boutique ADO* and has been edited in most areas ever since, but especially the **Category**, **Checkout** and **Shopping bag** models, as well as the JS code has been almost unaltered.

* I used some help from various more YouTube tutorials and w3schools tutorials.

* [MY PP4](https://github.com/Mienjung97/PROject-GOLFblog) helped me with implementing code for my **About** page and multiple other frontend functions.

* For the deployment I used the newly supplied google documents from Oisin (CI Tutor) for creating the AWS accound and setting up the S3 bucket

* All pictrures on the webpage were gathered from multiple webpages. A list of all the references are found [here](readme/text-files)

## Technical

* Many different posts on [Stackoverflow](https://stackoverflow.com/) have helped me understand Django and its functionality better, as well as it helped me fix bugs while coding

* The [Bootstrap](https://getbootstrap.com/) documentation helped me a lot with the styling of my page

* The AI tool [perplexity](https://www.perplexity.ai/) was used a lot for debugging and helping to understand my mistakes. No code was written by AI, the tool was just used in case of bugs and missing understanding on how a feature works

* The *Boutique ADO* code along project from Code Institute has been a valuable source for both starting the project as well as for setting up new apps, models, urls and views even if it created quite some issues along the way since it is pretty outdated and created validation problems


## Media

Main page picture: Foto von <a href="https://unsplash.com/de/@claybanks?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Clay Banks</a> auf <a href="https://unsplash.com/de/fotos/interieur-der-bibliothek-z_DkoUqgx6M?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  

Picture for Favicon: Foto von <a href="https://unsplash.com/de/@chrislawton?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Chris Lawton</a> auf <a href="https://unsplash.com/de/fotos/stapel-von-sechs-braunen-gebundenen-buchern-9T346Ij4kGk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  

"Bookstore" JSON for product fixtures was taken from: https://www.kaggle.com/datasets/bishop36/bookstore, but heavily modified and just used as a base for my products.

Picture for "default" image: Foto von <a href="https://unsplash.com/de/@blazphoto?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Blaz Photo</a> auf <a href="https://unsplash.com/de/fotos/person-mit-buch-die-auf-brauner-oberflache-sitzt-zMRLZh40kms?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  


# Acknowledgements

* I have to thank my dear partner for being so patient since there is not a lot of free time and yet she fully supports me on a daily basis

* I am also thankful for my co-student [Marceillo](https://github.com/Marceillo) and [Jan](https://github.com/yanidruffy), who I worked closely together, and who helped me with questions, gave their input and in times of question.

* A big thank you goes out to the Tutors who have helped me along my fourth protfolio project

* I would like to thank my mentor [Alshat Garg](https://in.linkedin.com/in/akshatnitd) for giving me the right pointers in the first meeting and my second mentor [Jubril Akolade](https://www.codementor.io/@jubrillionaire) for helping me finish the project and giving me very valuable advice.


*Sebastian Kefer, 04.09.2024*

[Back to top](<#table-of-content>)