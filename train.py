import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn import preprocessing
from sklearn import svm
from sklearn.externals import joblib
from sklearn import feature_extraction
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
from scipy import sparse

def generate_features(args, df_train, df_test, min_word_ct = 1,):
    tfidfVect = feature_extraction.text.TfidfVectorizer(
                tokenizer=lambda text: tokenize(text, **args), 
                lowercase=False,  min_df = min_word_ct)

    X_train =  tfidfVect.fit_transform(df_train["all_text"])
    X_test = tfidfVect.transform(df_test["all_text"])
     
    #scale to mean 0 and unit variance (allows to compare magnitudes of coefficients)
    scaler = preprocessing.StandardScaler(with_mean=False)
    X_train = sparse.csr_matrix(scaler.fit_transform(X_train.toarray()))
    X_test = sparse.csr_matrix(scaler.transform(X_test.toarray()))
    
    vocab = tfidfVect.vocabulary_
    
    return X_train, X_test, vocab

def train_model(df_train, df_test, args, min_word_ct, alg = "log_reg",
                param_grid = { "C": np.logspace(-3, 0, 4), "penalty" : ["l1"]}, 
                print_conf = False):

    #generate features
    X_train, X_test, vocab = generate_features(args, df_train, df_test, min_word_ct)
    inv_vocab = {v: k for k, v in vocab.items()}
    print("Number of features: {}".format( X_train.shape[1]))
    
    #specify algorithm 
    if alg == "log_reg":
        estimator = linear_model.LogisticRegression(solver = "saga", class_weight="balanced", multi_class = "ovr", max_iter=500)
    elif alg == "svm":
        estimator = svm.LinearSVC(class_weight="balanced", dual=False, multi_class = "ovr", max_iter=500)
 
    #Determine best hyperparameter using 5-fold cross-validation
    cv = model_selection.StratifiedKFold(n_splits=5, shuffle=True)
    model = model_selection.GridSearchCV(estimator, param_grid, cv=cv, scoring="f1_weighted", n_jobs=-1)
    model.fit(X_train, df_train["label"])
    print ("Best mean CV weighted f1-score is {} at parameters {}".format(round(model.best_score_, 3), model.best_params_))
    
    #For each class, print largest coefficients
    coeff = model.best_estimator_.coef_
    print ("Top coefficients")
    df_coeff = pd.DataFrame()
    for j, l in enumerate(np.unique(df_train["label"])):
        coeff_l = coeff[j]
        sorted_indices = np.argsort(np.abs(coeff_l))
        nonzero_c = np.sum([0 if c==0 else 1 for c in coeff_l])
        df_coeff[l] = [inv_vocab[i] + " " + str( round(coeff_l[i], 2)) for i in sorted_indices[::-1][:10]]
    print (df_coeff)
    print ("\nNon-zero coefficients: {} out of {}".format(nonzero_c, coeff.shape[0]*coeff.shape[1]))
    
    #Evaluate the model on the test set
    print ("\nEvaluation scores on test set: ")
    preds = model.predict(X_test)
    print (metrics.classification_report(df_test["label"], preds, target_names = np.unique(df_test["label"])))
    
    if print_conf == True:
        conf = metrics.confusion_matrix(df_test["label"], preds)
        df_conf = pd.DataFrame(conf, index = np.unique(df_test["label"]), columns =  np.unique(df_test["label"]))
        plt.figure(figsize = (10,7))
        sns.heatmap(df_conf.astype(int), annot=True)
    
    return model, preds

# TODO : me ;)
for col in ["Word", "Subtitle", "Author", "Publication"]:
    df[col] = df[col].fillna("")
    df["all_text"] += " "  + df[col]

df_train = pd.read_csv("words_train.csv")
df_test = pd.read_csv("words_test.csv")
print ("Number of articles: {}".format(len(df_train)))
    
args = {"stem": False, "n_grams":1}
model1, preds1 = train_model(df_train, df_test, args, min_word_ct = 10,  print_conf=True)
print "done"