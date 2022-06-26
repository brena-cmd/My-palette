from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
import io
from pathlib import Path

def get(uploaded_image, n_cluster):
    #salvar imagem do streamlit
    with open(uploaded_image.name,"wb") as f:
         f.write(uploaded_image.getbuffer())
              
    # Abre uma imagem
    image = Image.open(uploaded_image.name)
    image.thumbnail((128,128), Image.Resampling.LANCZOS)


    # Transformar os pixels dela em linhas de uma matriz
    N,M = image.size
    X = (np.asarray(image).reshape(N*M,3))

    # Aplicar o k-means a estes dados
    model = KMeans(n_clusters=n_cluster).fit(X)
    # Capturar os centros e usar como cores da paleta
    cores = model.cluster_centers_.astype('uint8')[np.newaxis]
    cores_hex = [matplotlib.colors.to_hex(cor/255) for cor in cores[0]]
    Path(uploaded_image.name).unlink()
    return cores, cores_hex
      
def show(cores):
    #exibir paleta de cores
    fig = plt.figure()
    plt.imshow(cores)
    plt.axis('off')
    return fig

def save(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png')
    plt.axis('off')
    return img
