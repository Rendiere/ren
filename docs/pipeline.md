# Pipeline

## Model Transformer

This transformer allows you to use a model as a feature transformer and feed the outputs of one (or more) model(s) to another. 

```python
import pandas as pd
import ren
import sklearn

# TODO

```



## Column Selector

A transformer to select one or more columns from a DataFrame. Useful for when you want to perform transformations to a subset of features in a pipeline. 


```python
>>> import pandas as pd
>>> from ren.pipeline import ColumnExtractor

>>> df = pd.DataFrame({'a': [1,1,1,], 'b': [2,2,2]})

>>> ColumnExtractor(['a']).fit_transform(df)
   a
0  1
1  1
2  1
```


