def evaluate(best_processed_path, model):
    """
    Evaluate - on a 10 ##s testing set
    """
    y_pred = model.predict(best_processed_path)
    return y_pred
