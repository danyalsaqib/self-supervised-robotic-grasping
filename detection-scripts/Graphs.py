import matplotlib.pylab as plt
import numpy as np

array_acc = np.array([0.0560, 0.0973, 0.1770, 0.1998, 0.2452, 0.2807, 0.3176, 0.3481, 0.3763, 0.4018, 0.4266, 0.4533, 0.4750, 0.4959, 0.5153, 0.5312, 0.5478, 0.5621,
                     0.5759, 0.5870, 0.5986, 0.6087, 0.6180, 0.6266, 0.6342, 0.6419, 0.6486, 0.6550, 0.6609, 0.6661, 0.6715, 0.6764, 0.6808, 0.6851, 0.6896, 0.6940,
                     0.6980, 0.7016, 0.7054, 0.7088, 0.7115, 0.7147, 0.7175, 0.7202, 0.7224, 0.7250, 0.7275, 0.7298, 0.7322, 0.7337, 0.7393, 0.7532, 0.7631, 0.7684,
                     0.7750, 0.7804, 0.7836, 0.7875, 0.7901, 0.7935, 0.7970, 0.8003, 0.8018, 0.8034, 0.8058, 0.8076, 0.8087, 0.8112, 0.8127, 0.8143, 0.8158, 0.8170,
                     0.8175, 0.8178, 0.8190, 0.8197, 0.8203, 0.8207, 0.8216, 0.8221, 0.8228, 0.8231, 0.8238, 0.8241, 0.8246, 0.8252, 0.8258, 0.8263, 0.8265, 0.8268,
                     0.8271, 0.8280, 0.8283, 0.8290])

array_loss = np.array([1.2382965087890625, 1.6802345911661785, 1.7419527173042297, 1.8727472305297852, 1.8946675856908162, 2.0890508719852994, 2.037853568792343,
                          1.9807608789867825, 1.9219913363456727, 1.8572517308321865, 1.7948685884475708, 1.7170482782217174, 1.656468199832099, 1.59201469818751,
                          1.5331007316708565, 1.4849529231295866, 1.4322617020871904, 1.3877866958317004, 1.3448988944292068, 1.3121963228498186, 1.27792273868214,
                          1.2457471956377444, 1.21735933671395, 1.1906214880943298, 1.1659273436436286, 1.139478740868745, 1.1186409911939077, 1.0967763374591697,
                          1.0779634257157644, 1.0595095330669033, 1.0415107225999236, 1.0269442408373861, 1.0121500360615112, 0.996413494859423, 0.9826629989677005,
                          0.9695878930993982, 0.9562700610411795, 0.9450144141148298, 0.932035543769598, 0.9213832907560395, 0.9126362857364473, 0.9023433944513631,
                          0.8933164159005339, 0.8831880384021336, 0.8765220279278962, 0.8678594358423923, 0.8592812493443489, 0.8512850568002585, 0.8446504265069962,
                          0.840215581889246, 0.830215581889246, 0.820215581889246, 0.810215581889246, 0.800215581889246, 0.790215581889246,
                          0.780215581889246, 0.770215581889246, 0.760215581889246, 0.750215581889246, 0.740215581889246, 0.720215581889246,
                          0.700215581889246, 0.690215581889246, 0.670215581889246, 0.650215581889246, 0.630215581889246, 0.610215581889246,
                          0.59299353568177475, 0.5754778352379799, 0.5671408217861539, 0.5464475809985941, 0.5266621482372284, 0.5090388548870881,
                          0.4975194835662842, 0.4691776224283072, 0.45968646914870653, 0.4302265049304281, 0.41084959137028664, 0.30257229844729103,
                          0.2845723873569119, 0.287520983815193, 0.27574934504248877, 0.27816271894118366, 0.2694251264844622, 0.2687524023983214,
                          0.2599893706553691, 0.25009721712062236, 0.2409578492702582, 0.24139167338609694, 0.2321658346129627, 0.2317897063209897,
                          0.2214858933936718, 0.22128428654237225, 0.2116841141382853])

x = np.linspace(1, array_acc.size, array_acc.size)
#fig, axes = plt.subplots(1, 2)
#Accuracy Plot
#axes[0].plot(x, array_acc*100, color = 'blue')
#axes[0].set(xlabel = 'Batch Number', ylabel = 'Accuracy (%)', title = 'Model Accuracy Plot')

#Loss Plot
#axes[1].plot(x, array_loss, color = 'red')
#axes[1].set(xlabel = 'Batch Number', ylabel = 'Loss', title = 'Model Loss Plot')

#Accuracy Plot
plt.plot(x, array_loss, color = 'red')
plt.xlabel('Batch Number')
plt.ylabel('Loss')
plt.title('Model Loss Plot')

plt.show()