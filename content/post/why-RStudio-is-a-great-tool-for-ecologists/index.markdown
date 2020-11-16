---
title: Why RStudio is a great tool for ecologists
author: Tanya Strydom
date: '2020-11-16'
slug: why-RStudio-is-a-great-tool-for-ecologists
categories:
  - R
tags:
  - coding
  - R
  - OpenScience
subtitle: ''
summary: 'Some thoughts on why RStudio is great and makes reproducibility that little bit easier to attain. In retrospect this turned into a RMarkdown post...'
authors: []
lastmod: ''
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
---
*I'd like to start off with a disclaimer:*

> This isn't a blog post on R being a better or more superior language (I'm a big fan of finding what works for you) but rather more of a discussion around my experience with the RStudio IDE (after having played with some other text editors) and what makes it great for the researchers that are not here to become computer scientists but are here for the natural science.

So it's really no secret that science is starting to 'get with the times' when it comes to open science and reproducibility. One of the big shifts is moving towards using a more code-based workflow when doing analyses. However, that being said I think most students embarking on their adventures in science (and specifically ecology) aren't necessarily interested in becoming the next 'hacker' (although there is some appeal to entertaining the fantasy every time I boot up my text editor of choice for the day) and might find the coding aspect of the research process quite 'scary'. That is (at least in my opinion) where the RStudio environment comes in to be pretty handy...

To start with - some points in favour of using R as a language:
* It is Open Source (which in itself should be enough 😉), allowing for 'community customisation'
  + This also means there is a big 'help' community when you inevitably get stuck...
* R is the current language of choice for most ecologists (*says the `Julia` user*)
  + It's becoming somewhat of an ['industry standard'](http://esajournals.onlinelibrary.wiley.com/doi/abs/10.1002/fee.2179)
* Ecologists have worked on and developed packages to preform many analyses
  + Giving users a very 'complete' library of tools to choose from
  + This makes analyses more accessible to those not mathematically/statistically/coding inclined

Just to make this clear - you can use R without using RStudio but, as I've highlighted, R is the way moving forward and using an IDE that is catered to it just makes sense, it makes for a 'cleaner' user experience, and is one less frustration in the learning process. In a sense RStudio is a 'click-and-play' type system and when you open it R just *works* you don't need to go and install this kernel and find that extension. This means that you can focus on 'driving' the system instead of trying to get it to start.

Okay cool, but so what? What else does RStudio have to offer?

This is where it gets cool - RStudio has all these 'hidden features' that lets you take your work to the 'next level'

### RMarkdown exists

Okay so I know I started this post saying that I don't want to start a 'my thing is cooler than yours' debate but I will go on record saying that I *cannot* stand working in Word and prefer using Markdown (LaTeX is cool but a lot of work...). Enter the oh so amazing [{RMarkdown}](https://bookdown.org/yihui/rmarkdown/) which, without taking up too much of your time, basically lets you embed code chunks (even not-R code) within the document. This means you can have the code (or link to the script) that performs your analyses in the document and everytime you re-render it all the results/outputs will be current. No more needing to re-export those figures/or re-do your tables - just click Run (or knit) and its all there. *Here is where I recommend spending some time with understanding how to produce tables  - [{gt}](https://gt.rstudio.com) is pretty great but there are a lot of options.* It is a bit of a learning curve to get used to working in plain text but when the penny drops you won't want to go back - trust me!

As an additional recommendation - start small here and just write up a small research report - nothing fancy until you get a bit more comfortable with things. Then, 'one day when you're big' (or whenever you feel ready for the challenge) you can write up that manuscript or even your whole [thesis](https://github.com/ismayc/thesisdown) in RMarkdown/RStudio. Don't get me wrong there will be teething problems - references are one of them but the resources are [there](https://bookdown.org/yihui/rmarkdown-cookbook/bibliography.html). Of course collaborative writing is another teething problem - and one that will take some convincing to have happen...

### When you have RMarkdown down the world is your oyster

{RMarkdown} isn't just great for writing up reports/a thesis but it acts as the 'springboard' for a lot of other things including but not limited to:

#### Making presentations

Something I have recently ventured into is making HTML5 presentations (*blog post on the reasoning pending*). {RMarkdown} comes with a 'native' [presentation output](https://bookdown.org/yihui/rmarkdown/presentations.html) format or you can use [{xaringran}](https://github.com/yihui/xaringan) to make presentations - and once again you can embed your R code *right there* for on the fly outputs. Also, because it is a plain text environment you can spend your time focusing on the content as opposed to the layout/design - which you can tweak using a .css type approach (or just actual .css if you like).

#### Creating a website

Maybe not really a part of the research workflow but having a personal website is still a vital part of sharing your research (and marketing yourself I guess...). And what do you know? RMarkdown has got you fam. In this case [{blogdown}](https://bookdown.org/yihui/blogdown/) does the piggy backing.

#### Creating and maintaining a CV

Again the [{vitae}](https://github.com/mitchelloharawild/vitae) uses {RMarkdown} and allows you to produce a truly stunning CV. And since, once again, you can just stick in chunks of code in as needed - for instance automatically/dynamically drawing up your publications list using e.g. [{rorcid}](https://github.com/ropensci/rorcid) to do the data scraping. If you're really nifty (It's a long term plan for me personally) you can even have it automatically re-render and re-publish your CV however often you want, no needing to manually slog through entering new manuscripts - [here](https://github.com/seabbs/cv) is an example. Also just saying I find it way more fun to update my CV now than when it was in the dreaded Word format.

### Concluding remarks

I realised I started this post with 'hey RStudio makes everything easier' and then went on an {RMarkdown} tangent. But I think the thing is RStudio acts as the 'stadium' that hosts and allows us to play with things like {Rmarkdown} all in one place - so it's kind of like when you're watching track and field and you have a whole host of events you can watch **without** needing to leave your seat. It by extension does the 'backend' work for you (well the amazing package developers) - for example how RMarkdown allows you to go from a .Rmd to .md to .PDF file with the click of a button! It does get annoying when you want to get fancy but as I said when you're just getting started with things its nice to have a 'click and play' system in place.

Basically a lot of the packages developed in the R environment allow you to do cool programming things without needing to do a lot of the actual developer side of things (but if you would want to the option to customise is there) with the added bonus that it is Open Source, is the 'native language' of most ecologists, and provides a gateway to doing reproducible, sharable and streamlined science!

Cheers,

Tanya 🐾
