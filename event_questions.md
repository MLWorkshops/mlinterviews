# Selected questions and answers

These are some selected Q&A during the live event we held, anonymized for privacy reasons.

## What is the Github link to the repository?

https://github.com/MLWorkshops/mlinterviews

## Where are the setup instructions?

https://github.com/MLWorkshops/mlinterviews#getting-started

## Regarding the number of jars.  Is there ramifications for resampling or is each sample not repeating?


## How can I view the presentation slides?

Presentation slides are located inside the individual directories (e.g. "stats_workshop/Slides.pdf"). They can either be viewed in Github or downloaded from Jupyter notebook to be viewed separately.

## Can you recommend any good, concise resources for understanding statistics?

* This is one of the best books on practical experimentation https://www.amazon.com/Field-Experiments-Design-Analysis-Interpretation/dp/0393979954/

* https://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/

## Any stats YouTube channels or podcasts you love?

* StatQuest
* 3 brown 1 blue
* FiveThirtyEight
* Two Minute Papers
* Data Skeptic
* Journal Club
* Intro to Statistical Learning Book (YouTube videos)
* https://www.oreilly.com/radar/topics/oreilly-data-show-podcast/
* https://thedataexchange.media/author/bglorica/


## I've read about model diagnostics/assumptions for linear models.  But what about logistic models?  I find I get stuck on multiple linear regression a lot when I get down to validating model assumptions and get stuck when dealing with outlier's (t student residuals, cooks distance)… I've read I'm supposed to maybe apply a different normalization or a different type of model (such as robust regression).

Something that helped me was to think of assumptions less as “rules.” It’s not about whether you are “allowed” to use multiple linear regression when residuals look a certain way, but more about what those abnormalities are going to do to the results you’re trying to obtain.



## If the class imbalance is 90:10 what should be done to train a good model? Also, what would be a good way to validate such a model?

* Metrics for class imbalance :
  * AUC ROC
  * AUC PR
* https://towardsdatascience.com/methods-for-dealing-with-imbalanced-data-5b761be45a18


## What other books/resources are helpful for learning statistics and ML?
* https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/
* For treating classical stats and ml topics, a great resource (explains metrics, outliers, many other great topics) I like Nina Zumel’s articles.  https://win-vector.com/author/nzumel/ (even one there on linear vs. logistic regression!)
 

## I work with a lot of classified or PHI data, so code is NOT copy-able. How do I construct a portfolio?

* Little take from my point of view.  It may not be a portfolio necessarily, but having a blog that highlights your technical interests and new things you are learning, can be good.  Same goes for technical videos - e.g. speak at a meetup on a tech topic you care about.  Finally, if you have time, find an interesting problem you want to solve (a very crisp question that you know you can answer with stats or ML or at least explore the data) and create a public place to showcase (blog, GitHub repo, etc.).  passion in technical areas imho shows that growth mindset

* I think doing one or two hackathons or a Kaggle competitions per year is a great way to build a portfolio outside the daily job

## To piggy back on this same theme, in your experience are companies willing to hire does not have a formal background (i.e. Degree) in DS?  Trying to figure out how to be seriously considered for DS roles, when I tend to get pigeonholded based on my previous experience in test and eval

It’s really good to lean/build on your strengths for sure, but yes there is some learning to be done as well.  As having knowledge already in a test/eval type role, maybe you could think about how to unit test data and unit test simple ML models to build on your strengths and experience.  Understand metrics and evaluating ML models and especially beyond how, look at why you would use certain metrics for example, to show maturity in thinking.

## Is there a good tool to help in hyperparameter tuning the number of hidden layers and number of nodes per layer?

As PyTorch uses dynamic graphs it can be a good choice for tuning based on the network architecture itself.  Check out https://pytorch.org/tutorials/beginner/hyperparameter_tuning_tutorial.html (integrates with TensorBoard)
