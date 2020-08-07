---
title: Exploring colour blind and colour weak plotting options in ggplot2
author: Tanya Strydom
date: '2020-07-03'
slug: exploring-colour-blind-and-colour-weak-plotting-options-in-ggplot2
categories:
  - R
tags:
  - dataVis
  - coding
  - R
subtitle: ''
summary: 'After reading an interesting blog post from Chartable I thought why not try and implement some of their suggestions using ggplot.'
authors: []
lastmod: ''
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
---

<div style="text-align: justify">


On my 'over breakfast' Twitter scroll I cam across [this](https://blog.datawrapper.de/colorblindness-part1/) interesting series of blogposts on the Chartable blog (hosted by Datawrapper) that discusses how we can make our plots and visuals more friendly for colour blind and colour weak readers. They raised some interesting points and options to use and I thought it would be a 'constructive' way to spend my Friday trying to implement these ideas in R, specifically using `ggplot2`.

In the [second](https://blog.datawrapper.de/colorblindness-part2/) blogpost they have a long discussion about different ways to make your figures more inclusive (I highly recommend reading the full article - it has some awesome visuals as well) and along with the standard recommendation to **avoid green** and trying to go with **complimentary colours such as blue and orange** some other points they raised that I thought were interesting include:

* **Playing with the lightness of your colours**
  + Even if you end up using non-ideal colours you can use darker and lighter shades to offset the similarity
* **Using fewer colours**
  + Maybe only use colour to highlight differences or pull out the main points of the figure
* **Play with shapes and patterns**
  + This can include using symbols (such as ticks and crosses) to emphasise a point or show different groups in scatterplots, or use patterns for line plots or even for fill colours on geom-type plots

So at first glance most of these options seem very do-able and easy to integrate into the `ggplot2` workflow, with the exception of specifying patterns for fills of geom objects (think barplots) but I came across the `ggpattern` package which solves that problem with what seems to be a huge degree of customisability - see the package website [here](https://coolbutuseless.github.io/package/ggpattern/). At time of writing this package isn't available on CRAN yet but can be downloaded and installed via GitHub.

With that out of the way let's get to the actual plotting. Also I thought this would be a good opportunity to play with the `penguins` dataset that was [recently released](https://towardsdatascience.com/penguins-dataset-overview-iris-alternative-9453bb8c8d95) as an `iris` alternative.

# Playing with lightness

This is theoretically a very simple example to execute as we can just specify our colour choices to be of varying shades. For this example I decided to plot body mass vs. flipper length for the different penguin species as well as for males and females. I used [Adobe Color][https://color.adobe.com/create/color-wheel] to pick my colours but that just personal preference.


```r
library(ggplot2)
library(dplyr)
```

```
## 
## Attaching package: 'dplyr'
```

```
## The following objects are masked from 'package:stats':
## 
##     filter, lag
```

```
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
```

```r
library(palmerpenguins)

#import data
penguins <- penguins %>%
  #removing NAs for ease
  na.omit()

#specify colours manually
AdeMale <- "#1C1DAD"
AdeFem <- "#A0A0FA"
ChiMale <- "#AD400B"
ChiFem <- "#FA9966"
GenMale <- "#445748"
GenFem <- "#6AD674"

#create plot
P1 <- ggplot() +
  geom_point(data = penguins,
             aes(x = body_mass_g,
                 y = flipper_length_mm,
                 #make new grouping variable with the species sex combos
                 colour = paste(penguins$species,
                                penguins$sex)),
             #for simplicity removing legend
             show.legend = FALSE) +
  #set colours
  scale_colour_manual(values = c(AdeMale,
                                 AdeFem,
                                 ChiMale,
                                 ChiFem,
                                 GenMale,
                                 GenFem)) +
  theme_bw()
```

{{< figure library="true" src="points.jpg" title="" lightbox="true" >}}

So we can see that using the different shades of the same colour for the different sexes works really well - although arguably there is some issue distinguishing between the species so lets add some shapes...

# Adding shapes


```r
P2 <- ggplot() +
  geom_point(data = penguins,
             aes(x = body_mass_g,
                 y = flipper_length_mm,
                 #make new grouping variable with the species sex combos
                 colour = paste(penguins$species,
                                penguins$sex),
                 #specify grouping var for shape
                 shape = species),
             #for simplicity removing legend
             show.legend = FALSE) +
  #set colours
  scale_colour_manual(values = c(AdeMale,
                                 AdeFem,
                                 ChiMale,
                                 ChiFem,
                                 GenMale,
                                 GenFem)) +
  theme_bw()
```

{{< figure library="true" src="Symbols.jpg" title="" lightbox="true" >}}

**Nice!** As we can see just adding one line to our code can make all the difference.

# Playing with patterns

This is where it gets fun - time to play with a new package. If we want to call patterns for our geoms instead of using the standard `geom_*` function from `ggplot2` we will be using the `geom_*_pattern` function from the `ggpattern` package. But first we can have a look at our original colour palette using a standard boxplot - let's stick to flipper length.



{{< figure library="true" src="box.jpg" title="" lightbox="true" >}}

Here we can see how the different shades pop out really nicely - arguably we can still distinguish between the Chinstraps and the Gentoos but I think we can play with the aesthetics a bit more and make the plot pretty - not just functional!


```r
#To download package from GitHub
#remotes::install_github("coolbutuseless/ggpattern")
library(ggpattern)

#Summarised the dataset for plotting

P4 <- ggplot() +
  geom_col_pattern(data = penguins_summary,
                   aes(y = flipper_length_mm,
                       x = species,
                       group = sex,
                       #make new grouping variable with the species sex combos
                       fill = paste(penguins_summary$species,
                                    penguins_summary$sex),
                       #specify pattern type
                       pattern = sex),
                   #specify the fill for the pattern
                   pattern_fill = "black",
                   #specify box colour
                   colour  = 'black',
                   #for simplicity removing legend
                   show.legend = FALSE,
                   position = "dodge") +
  #set colours
  scale_fill_manual(values = c(AdeMale,
                               AdeFem,
                               ChiMale,
                               ChiFem,
                               GenMale,
                               GenFem)) +
  theme_bw()
```

{{< figure library="true" src="pattern_box.jpg" title="" lightbox="true" >}}

**Neat!** We can see that the patterns add a new 'level' to our plots and if you look at the syntax of the ggpatterns functions we see that it mirrors that of ggplot - it just has a few more `_pattern` thrown in! This package allows a large degree of freedom with regards to what and how you want your patterns to look like. You can even import images or make your own patterns. Combine this with the somewhat intuitive syntax (if you're comfortable with ggplot) it is something I can see myself trying to use more often when making figures.

🐾
Tanya

</div>

## Footnote {.appendix}
If you want a better look at all of the code feel free to have a peek on GitHub [<svg style="height:0.8em;top:.04em;position:relative;" viewBox="0 0 496 512"><path d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/></svg>](https://github.com/TanyaS08/TanyaDoesScience/blob/master/_posts/2020-06-26-exploring-colourblind-and-colourweak-plotting-options-in-ggplot2/exploring-colourblind-and-colourweak-plotting-options-in-ggplot2.Rmd)
