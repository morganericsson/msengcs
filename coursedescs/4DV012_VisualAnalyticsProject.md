---
Name:       Visual analytics project
PrelCode:   4DV012
HEC:        10
Year:       5
Period:     1-2
Examiner1:  Andreas Kerren
Examiner2:  Ilir Jusufi
Status:     FirstDraft
Mandatory:  Yes
Subject:    ComputerScience
Type:       Project
PreReq:     1DV003;1DV005;1DV006;1DV009;4DV006;1MA002;1MA004.
---

# [%PrelCode] - [%Name] ([%HEC] hec)

## Prerequisites

* Computer graphics with emphasis on 2D, Advanced → 1DV009
* Information visualization, Basic → 4DV010  ???? (is given in parallel, same with InfoVis 2)
* Machine learning, Advanced → 4DV006
* Programming (at least one, e.g., Java or JavaScript or Python), Advanced → 1DV001, 1DV003

## Learning outcomes

After completing the course the student is expected to:

1. Knowledge and understanding
    1. Characterize the role of interactive visualization both in the presentation of results and in the process of data exploration supported by data-analysis algorithms
    2. Identify characteristics of state-of-the-art Visual Analytics (VA) systems

2. Skills and abilities
    1. Plan a VA development project by mapping analytical requirements to a software solution that involves the combination of interactive visualization and data-analysis algorithms
    2. Execute the project plan by applying previously learned skills from required courses in a project-like environment and combining them with state-of-the-art VA tools and libraries

3. Judgement and approach
    1. Reflect on the types of questions and analytical processes supported by different combinations of visualization techniques and data-analysis algorithms
    2. Evaluate whether a proposed VA solution reaches its analytical goals efficiently and effectively

## Course contents

This course offers the students the opportunity to consolidate and apply knowledge and skills obtained in previous courses of their studies by the development of an interactive Visual Analytics (VA) application. Visual analytics systems bring data analysis closer to end-users by effectively combining interactive visualization and complex algorithms, guided by the underlying analytical processes inherent to the data and the application at hand. By following the course’s modules (described in more details below) the students will be introduced to visual analytics theoretical aspects and tools, create the conceptual design of a VA project of their choice, implement their designs, and present their results.

## Types of instruction

The types of instruction for this course encompass different categories, described as follows. Traditional lectures are used for teaching fundamental concepts, complemented with more practical tutorial sessions for the introduction of specific programming libraries. The project-related activities will mainly consist of self studies and group activities which will be regularly accompanied by the responsible for the course.

## Modules

### M1: Introduction to visual analytics – theory and practice, 3 credits

The course starts with an introduction of VA from both the theoretical and practical perspectives with the following activities:
* Lecture(s) on the theoretical background of VA and analytical processes
* Analysis of selected examples of state-of-the-art VA systems
* Tutorial(s) on state-of-the-art tools and libraries used for the development of VA systems, such as D3 [1], yFiles [2], and Bokeh [3]

[1] https://d3js.org/

[2] https://www.yworks.com/

[3] https://bokeh.pydata.org/

### M2: Conceptual design of the project, 3 credits

The main goal of the students during M2 is to use the knowledge obtained in M1 to design (conceptually, at first) an interactive VA application that can potentially answer at least one interesting question/thesis from a selected data set, combining one (or more) visualization techniques and one (or more) data analysis algorithms into an analytical process. The data set will be selected from those available in open data repositories. The final product of M2 is a written report that explains how the system should be implemented and the rationale behind the design choices of the project.

### M3: Implementation of the project, 4 credits

Finally, in M3 the students will implement the design proposed in M2 by using selected programming languages and graphical/visualization libraries.


## Examination

Due to the different approaches and goals of each of this course’s modules, the examinations will occur in specific ways as described below. Whenever applicable, we only require the use of programming libraries that are freely available. Any standard laptop or desktop computer with a onboard graphics chip and/or dedicated graphics card is sufficient for the programming tasks.

**M1:** The student’s progress in this module will be assessed with one theoretical and one practical assignment. The theoretical assignment (TA) is designed to evaluate knowledge and understanding of the VA-related concepts teached in the initial lectures, and also if the students are able to critically reflect upon the different existing approaches and what impact these may have on their analytical goals for the finally implemented system. The practical assignment (PA) is designed to evaluate the students’ skills in the implementation of simple data-analysis algorithms and visualization techniques, which is an important basic requirement for the successful continuation of the course.

**M2:** This module’s examination revolves mainly around the assessment of the final conceptual design report. The assessment will be carried out both during the module, at specific checkpoints, and at the end of the module. At each checkpoint, the students will report on the progress of the written report and receive feedback for its improvement. At the end of the module the students will submit, present and defend their design (PR-1), which will be graded. The main assessment criteria for the conceptual design are
* the value of the designed question/thesis to be analyzed in the data set,
* correct choice of analysis and visualization techniques to answer the question/thesis,
* suitable design of an analytical process involving the chosen techniques, and
* feasibility of the system’s architecture to implement the proposed analytical process.

**M3:** Similarly to the examination of the previous module, the assessment of M3 will be carried out both during the module, at specific checkpoints, and at the end. At each checkpoint, the students will report on the progress of the implementation and receive feedback for its improvement. At the end of the module, the students will submit and present their project (PR-2), which will be graded. The main assessment criteria for the implementation are as follows:
* Effectiveness of the system in supporting the analytical process to answer the question/thesis proposed during M2. The final software must at least implement the design’s core techniques and show promising initial results.
* Quality of project deliverables, especially the documentation of the source code and the system’s usage.
* Ability of the student to reflect and critically analyze the development process by comparing the initial design from M2 and the final result.

## Grading

The VA project course is assessed with an A-F grading. The three modules are separately evaluated and graded. Each of the assignments in the three modules (cf. TA, PA, PR-1, PR-2) must be passed individually, i.e., *grade(Assignment) ≥ 50%* in order to pass it. The grades for each module are calculated as follows:
* *grade(M1) = 0.5 * grade(TA) + 0.5 * grade(PA)*
* *grade(M2) = grade(PR-1)*
* *grade(M3) = grade(PR-2)*

If one of the modules is failed, i.e., *grade(M) < 50%*, then the final course grade is F. If all modules are passed, the final course grade is an A-F grade based on the weighted sum of the points received for the three modules, as follows: *grade(Course) = 0.3 * grade(M1) + 0.3 * grade(M2) + 0.4 * grade(M3)*. If *grade(Course) ≥ 50%*, then the student passes the course, otherwise the course is failed. The grading table is provided in the following:

| Final Grade (A-F) | Grading Points (%) |
|-------------------|--------------------|
|  A                |  >= 90             |
|  B                |  >= 80             |
|  C                |  >= 70             |
|  D                |  >= 60             |
|  E                |  >= 50             |

In order to relate the learning outcomes to the two assessment types and individual assignments, we provide the following table:

| Learning Outcome | Assessment Type | TA  | PA  | PR-1 | PR-2 |
| ---------------- | --------------- | --- | --- | ---- | ---- |
| 1.1              | TA + PR         |**X**|     |**X** |      |
| 1.2              | TA + PR         |**X**|     |**X** |      |
| 2.1              | PR              |     |     |**X** |**X** |
| 2.2              | PA + PR         |     |**X**|      |**X** |
| 3.1              | PR              |     |     |**X** |**X** |
| 3.2              | TA + PR         |**X**|     |      |**X** |

Late work will not be accepted without prior approval by the instructor. Reasons for accepted delays may be proven health conditions, no-fault hardships, etc.

## Course literature

* Daniel Keim, Jörn Kohlhammer, Geoffrey Ellis, and Florian Mansmann. Mastering the Information Age: Solving Problems with Visual Analytics. Eurographics, 2010.
    * Estimated reading: 60 / 167 pages
* Tamara Munzner. Visualization Analysis and Design. CRC Press, 2014.
    * Estimated reading: 100 / 428 pages
* Helen C. Purchase. Experimental Human-Computer Interaction: A Practical Guide with Visual Examples. Cambridge University Press, 2012.
    * Estimated reading: 80 / 241 pages
* DV, Distributed slides.
    * Estimated reading: 50 / 50 pages


## Overlap

None.
