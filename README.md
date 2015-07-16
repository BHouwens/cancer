# Cancer Predictor

Simple classification test to see how well malignant breast cancer could be predicted given criteria of the cancerous growth. It uses `sklearn` and its `RandomForestClassifier`, with an accuracy of around 0.99 using the defaults. I might try writing something by hand for this at a later stage, but for now it's just a simple test.

Running this will output the accuracy of the classifier.

## Data

Data comes from the UCI archives, which you can find [here](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Original)). Acknowledgements:

   1. O. L. Mangasarian and W. H. Wolberg: "Cancer diagnosis via linear 
      programming", SIAM News, Volume 23, Number 5, September 1990, pp 1 & 18.

   2. William H. Wolberg and O.L. Mangasarian: "Multisurface method of 
      pattern separation for medical diagnosis applied to breast cytology", 
      Proceedings of the National Academy of Sciences, U.S.A., Volume 87, 
      December 1990, pp 9193-9196.

   3. O. L. Mangasarian, R. Setiono, and W.H. Wolberg: "Pattern recognition 
      via linear programming: Theory and application to medical diagnosis", 
      in: "Large-scale numerical optimization", Thomas F. Coleman and Yuying
      Li, editors, SIAM Publications, Philadelphia 1990, pp 22-30.

   4. K. P. Bennett & O. L. Mangasarian: "Robust linear programming 
      discrimination of two linearly inseparable sets", Optimization Methods
      and Software 1, 1992, 23-34 (Gordon & Breach Science Publishers).