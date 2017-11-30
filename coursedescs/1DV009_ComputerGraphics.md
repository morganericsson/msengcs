---
Name:       Computer Graphics
PrelCode:   1DV009
HEC:        5
Year:       3
Period:     1
Examiner1:  Andreas Kerren
Examiner2:  Ilir Jusufi
Status:     FirstDraft
Mandatory:  Yes
Subject:    ComputerScience
Type:       Regular
PreReq:     1MA001;1MA002;1MA006;1DV003;1DV006
---

# [%PrelCode] - [%Name] ([%HEC] hec)

## Prerequisites

* Java programming and corresponding data structures, Advanced → 1DV003
* Vector geometry/calculus, Use → 1MA006 ???
* Linear algebra (matrix calculus), Use → 1MA001, 1MA002
* Algorithms, Advanced → 1DV006

## Learning outcomes

After completing the course the student is expected to:

1. Knowledge and understanding
    1. Characterize all aspects of the computer graphics pipeline, i.e., the various steps and algorithms that occur from a geometric 3D object specification to the rendering of a corresponding 2D image on a raster graphics display
    2. Define and explain different types of object representations
    3. Define and explain the most important models and algorithms for viewing and local illumination

2. Skills and abilities
    1. Perform and implement rasterization algorithms for basic output primitives
    2. Perform and implement geometric, camera, projection, and viewport transformations
    3. Implement basic 2D/3D graphics solutions by using OpenGL

3. Judgement and approach
    1. Reflect upon the properties of different algorithms and models and pick those suitable for the problem to be solved
    2. Reason about the impact that choices, e.g., specific lightening/shading or color representations, have on the output quality

## Course contents

This course offers an introduction into the most important theoretical and practical aspects of computer graphics. Knowledge in computer graphics is not only needed for creating synthetic computer-generated images, but also for GPU computing. We provide foundations such as illumination or color models as well as discuss basic techniques and algorithms used in 2D and 3D graphics.

* Definition of the field of computer graphics and its scope
* Overview of display and interaction device technologies
* 2D output primitives and their rasterization
* Filling algorithms and antialiasing
* 3D object representations
* Geometric transformations
* Camera, projection and viewport transformations
* Visibility and clipping algorithms
* Color models
* Lighting and shading, especially local illumination
* OpenGL

## Types of Instruction

The types of instruction for this course encompass traditional lectures for teaching the majority of the course content. OpenGL is not explicitly given by lectures: students have to gain knowledge about this programming library by self studies (textbook, open online tutorials). In addition, the content is exercised and deepened in context of theoretical and practical lab assignments. All assignments are carried out individually or in fixed groups of maximal two students.

## Modules

* Theoretical assignments, 2.5 credits
* Programming assignments, 2.5 credits

## Examination

The learning outcomes of this course are assessed with the help of 3 theoretical assignments (TA) to evaluate knowledge and understanding of the computer graphics concepts teached in the lectures. These theoretical assignments also contain higher level questions in order to assess if the students are able to critically reflect upon the different approaches and what impact these may have on the final synthetic computer-generated images.
In addition, 3 programming assignments (PA) are used to mainly evaluate the students’ skills in algorithm implementation and graphics development in OpenGL. We only use programming libraries that are freely available. Any standard laptop or desktop computer with an onboard graphics chip and/or dedicated graphics card is sufficient for the programming tasks.

## Grading

The course is assessed with an A-F grading. The two modules are separately evaluated and graded. Each of the 3 TAs and 3 PAs in the two modules must be passed individually. If one of the modules is failed, then final course grade is F. If both are passed, the final course grade is an A-F grade based on the combination of the points received for the two modules, and both them are equally weighted. In more detail, total grade points = TA points / 2 + PA points / 2. To pass a module or the entire course, the student needs at least 50% of the points, otherwise the course is failed. The grading table is provided in the following:

| Final Grade (A-F) | Grading Points (%) |
|-------------------|--------------------|
|  A                |  >= 90             |
|  B                |  >= 80             |
|  C                |  >= 70             |
|  D                |  >= 60             |
|  E                |  >= 50             |

In order to relate the learning outcomes to the two assessment types and individual assignments, we provide the following table:

| Learning Outcome | Assessment Type | TA1 | TA2 | TA3 | PA1 | PA2 | PA3 |
| ---------------- | --------------- | --- | --- | --- | --- | --- | --- |
| 1.1              | TA + PA         |**X**|**X**|     |**X**|     |     |
| 1.2              | TA              |     |**X**|     |     |     |     |
| 1.3              | TA              |     |     |**X**|     |     |     |
| 2.1              | TA + PA         |**X**|     |     |**X**|     |     |
| 2.2              | TA + PA         |     |**X**|     |     |**X**|     |
| 2.3              | PA              |     |     |     |**X**|**X**|**X**|
| 3.1              | PA              |     |     |     |     |     |**X**|
| 3.2              | TA              |     |     |**X**|     |     |     |

Late work will not be accepted without prior approval by the instructor. Reasons for accepted delays may be proven health conditions, no-fault hardships, etc.

## Course Literature

* Donald D. Hearn, M. Pauline Baker, and Warren Carithers. Computer Graphics with OpenGL, 4th Ed., Pearson, 2010.
    * Estimated reading: 450 / 812 pages
* DV, Distributed slides.
    * Estimated reading: 310 / 310 pages

## Overlap

100% with 1DV800.
