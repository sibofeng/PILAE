import src.row_PILAE as rp
import src.tools as tools
import src.Hog as hg
import time
import csv
from sklearn.preprocessing import StandardScaler

X_train, y_train = tools.load_fashionMNIST()
X_test, y_test = tools.load_fashionMNIST(kind='t10k')

num = 4
X_train, X_test = hg.load_hog("../data/fashion_mnist/fashion_mnist", num)
X_train *= 100
X_test *= 100

# X_train /= 255
# X_test /= 255

# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.fit_transform(X_test)

t1 = time.time()
pilae = rp.row_PILAE(k=1.5, alpha=0.8, beta=0.95, activeFunc='sig')
pilae.fit(X_train, layer=3)
pilae.predict(X_train, y_train, X_test, y_test)
t2 = time.time()
cost_time = t2 - t1
print("Total cost time: %.2f" %cost_time)
# write into .csv file
with open("../log/mnist_info.csv", 'at+') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["map", "dimesion", "layer", "time", "train_acc", "test_acc", "k", "alpha", "beta", "acf"])
    writer.writerow([num, X_train[1], pilae.layer, cost_time, pilae.train_acc, pilae.test_acc, pilae.k, pilae.alpha, pilae.beta, pilae.acFunc])