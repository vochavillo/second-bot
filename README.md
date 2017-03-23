# second-bot
I was recently encouraged to reach out to people to PolicyLink, beginning with any Stanford alum or affiliate. The number of staff people at the organization was large enough to justify writing a web scraping script for this.

The code is pretty straightforward.

I used BeautifulSoup to get the html code of the main staff page. Because the staff page does not include the bios but rather includes hyperlinks that lead to people's individual bios, I needed to scrape the main staff page for the hyperlinks. And for each hyperlink that contained the string 'staff', which signaled that the link is indeed the url for the a staff person's bio, I again used the BeautifulSoup package to scrape the individual staff bio page for the text bio. After doing some quick research, it seemed like common practice in the organization for bios to include staff people's alma maters, where they attended for undergrad, masters, etc. So once I scraped for each person's bio in text form, it was just a matter of converting all the text to lower case and then doing a quick search for 'stanford.'

One minor issue was that some of the there were some 'a' link elements with no 'href' attribute. Not realizing this, I kept getting an error. But the fix called for the simple inclusion of a conditional statement that checked to see that the 'a' link element was not empty.

The result? Only one person at PolicyLink is a Stanford affiliate, and she's not even an alum but someone who worked at the Stanford Haas Center for Public Service. What would have been more helpful --and more fun because that would imply writing another method or two-- would be the provision of email addresses.

Given that there was at least one alum on identified as being a Stanford affiliate, the final product was three print lines: a header notifying the presence of a Stanford affiliate at the organization, the affiliate's name and the URL to that person's bio. Accordingly, if there were no Stanford affiliates, a single line would have been printed with the message that no affiliate worked at the organization.
