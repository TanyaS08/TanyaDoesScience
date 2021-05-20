---
date: "2020-10-06T00:00:00Z"
external_link: ""
image:
  caption:
  focal_point: Smart
slides:
summary: Singular Value Decomposition; network complexity; network prediction and possibly some network assembly.
tags:
- MachineLearning
- EcologicalNetworks
- SingularValueDecomposition
- PhD
title: Project Malcom
url_code: ""
url_DOI: ""
url_slides: ""
url_video: ""
authors: ['admin', 'Giulio V. Dalla Riva', 'Timothée Poisot','PoisotLab']
lastmod: '2020-10-30'
---

Ecological networks can be represented by their adjacency matrices, *i.e.*
a matrix for which every entry represents a species pair, and takes either
a value of 1 if there is an interaction between the two species, or 0
when there is none. Singular Value Decomposition ([SVD)
is the factorisation of a matrix $\mathbf{A}$
(where $\mathbf{A}_{m,n} \in\mathbb{B}$, in the context of adjacency matrices) into the form:

$$ \mathbf{U}\cdot\mathbf{\Sigma}\cdot\mathbf{V}^T $$

Where $\mathbf{U}$ is an $m \times m$ orthogonal matrix and
$\mathbf{V}$ an $n \times n$ orthogonal matrix. The columns in these matrices
are, respectively, the left- and right-singular vectors of $\mathbf{A}$.
$\mathbf{\Sigma}$ is a diagonal matrix that contains only non-negative $\sigma$
values. Where $\sigma_{i} = \Sigma{ii}$, and contains the singular values of
$\mathbf{A}$. When the values of $\mathbf{\sigma}$ are arranged in
descending order, the singular values ($\mathbf{\Sigma}$) are
unique. These singular values can broadly be viewed as a measure of
how informative that rank of the matrix is.

We can use SVD and more specifically SVD entropy as a measure of network complexity.
This approach looks at the 'physical complexity' of networks - which is in
contrast to more traditional measures such as connectence and nestedness which
look at the 'behavioural complexity' of networks.

SVD can also be used within the

An additional concept that I want to explore (if there is enough time) is the
relationship between network assembly and constraints on complexity (SVD entropy).
This will be building on a small section of the SVD entropy manuscript  
relating to network assembly and the constraints on complexity.
