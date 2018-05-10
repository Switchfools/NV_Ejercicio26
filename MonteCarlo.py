import numpy as np
import matplotlib.pylab as plt
velocidades=np.random.uniform(35,45,int(1E8))
alp=0.4
N=150
angulos=np.random.uniform(0,np.pi/2,int(1E8))
g=9.8
plt.hist(velocidades,bins=N,alpha=alp,normed=1,label=' Inicial')
distancias=((velocidades**2)*np.sin(2*angulos))/g
arriveData=np.array([61.0-5.0,61.0+5.0,115.0-5.0,115.0+5.0,31.0-5.0,31.0+5.0,177.0-5.0,177.0+5.0])

index=np.logical_and(distancias>arriveData[0], distancias<arriveData[1])
vel2=velocidades[index]
plt.hist(vel2,bins=N,alpha=alp,normed=1,label='1ra observación')
ang2=np.random.uniform(0,np.pi/2,len(vel2))
dist2=((vel2**2)*np.sin(2*ang2))/g
index2=np.logical_and(dist2>arriveData[2], dist2<arriveData[3])
vel3=vel2[index2]
plt.hist(vel3,bins=N,alpha=alp,normed=1,label='2da observación')
ang3=np.random.uniform(0,np.pi/2,len(vel3))
dist3=((vel3**2)*np.sin(2*ang3))/g
index3=np.logical_and(dist3>arriveData[4], dist3<arriveData[5])
vel4=vel3[index3]
plt.hist(vel4,bins=N,alpha=alp,normed=1,label='3ra observación')
ang4=np.random.uniform(0,np.pi/2,len(vel4))
dist4=((vel4**2)*np.sin(2*ang4))/g
index4=np.logical_and(dist4>arriveData[6], dist4<arriveData[7])
vel5=vel4[index4]
plt.hist(vel5,bins=N,alpha=alp,normed=1,label='4ta observación')
plt.xlabel('velocidades')
plt.ylabel('probabilidad')
plt.title('histograma distribución velocidades')
plt.legend()

plt.savefig('histograma.png')
