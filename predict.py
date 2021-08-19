def job_title_fun(model, vectorizer, string):
    """Predicts job framekwork thing"""
    x = vectorizer.transform([string])
    y = model.predict(x)
    return y