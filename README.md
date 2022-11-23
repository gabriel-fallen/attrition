# I'm sick of my job!

That's the project name, and **not** how I feel! 😅


The project is a showcase of a simple end-to-end data-driven Web app. As such it consists of two parts.


## ML-model building

The `Learning` folder captures the model building process.

To train (and evaluate) a model I employed the [Orange](https://orangedatamining.com) toolbox. It provides built-in access
to the employee attrition **synthetic** dataset (due to IBM), a range of different ML models and data munging utilities,
and an easy way to evaluate results (model accuracy in particular).

Model training and evaluation showed that good ol' Logistic Regression delivers the best results. Thus the next step was
to train it on the whole dataset (instead of n-folds scheme) and save the final model in a file (for future use in a Web app).
The whole process is captured in the `workflow.ows` file.

`load-predict.ows` file simply loads the same model back in order to manually double-check that it works
after serialization-deserialization roundtrip. 😊 `load-predict.ipynb` essentially does the same but this time completely
_programmatically_ from Python.


## Web application

That's what `App` folder contains.

The Web application is intentionally extremely simple. In essense it consists of just two files: `main.py` contains the back-end part
and `index.html` (in the `templates` folder) contains the whole front-end.

Back-end is a straightforward Flask application who's main job is parsing JSON data from a POST request, loading the serialized model,
feeding the data to the model in order to obtain prediction, and finally returning said predictions as another JSON string.

Front-end is truely a Single-Page Application: it contains little more than an HTML form to collect the data from a user, a `fetch` call
to send it to the back-end, and a couple of functions to connect the first and the second. 😊


I hope such minimalistic application provides an uncluttered learning resource for aspiring Data Scientist and Web Developers. 🧑‍🎓
