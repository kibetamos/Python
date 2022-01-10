# Beautiful, isn’t it? The KNN algorithm finds the three
# closest houses with respect to house size and averages the
# predicted house price as the average of the k=3 nearest
# neighbors. Thus, the result is $32,500.

## Dependencies
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
## Data (House Size (square meters) / House Price ($))
X = np.array([[35, 30000], [45, 45000], [40, 50000],
              [35, 35000], [25, 32500], [40, 40000]])
## One-liner
KNN = KNeighborsRegressor(n_neighbors=3).fit(X[:,0].reshape(-1,1), X[:,1])
## Result & puzzle
res = KNN.predict([[30]])
print(res)

