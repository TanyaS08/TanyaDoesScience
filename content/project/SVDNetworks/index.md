---
date: "2020-10-06T00:00:00Z"
external_link: ""
image:
  caption:
  focal_point: Smart
slides:
summary: Ecological networks are very complex - who would've thought!.
tags:
- MachineLearning
- EcologicalNetworks
- SingularValueDecomposition
title: The complexity of ecological networks using SVD entropy
url_code: "https://github.com/PoisotLab/ms_svd_networks"
url_DOI: ""
url_slides: ""
url_video: ""
authors: ['admin', 'Giulio V. Dalla Riva', 'Timothée Poisot','PoisotLab']
lastmod: '2020-10-30'
---

As a quick primer: generally in ecology we have struggled to define the complexity of ecological networks. Many measures have been proposed, with these usually focusing on the *structural* complexity of the network as opposed to using the *'physical'* complexity of the network. Here we used SVD entropy (based off of information theory) as well as the relative rank deficiency to quantify complexity.

When we use the SVD entropy of a network we are looking at the information that is contained within the interaction matrix of the system - broadly how much information is contained with each species and the interaction strategy it has adopted. Many other attempts at trying to quantify the complexity of ecological networks look more at the structure i.e. the behaviour of the interaction network.

Interestingly we found that ecological networks are very complex - in theory SVD entropy can take a value from 0 - 1 yet all of our networks were above 0.8

{{< figure library="true" src="SVD.png" title="" lightbox="true" >}}

The long and the short of it is that we argue that using an information based approach to quantifying the complexity of a network is a more 'correct' approach than those that focus on structure. If we unify this definition it will hopefully allow us to uncover more general patterns or relationship with complexity - e.g. the argument that complexity begets stability.
