#!/usr/bin/env python
# coding: utf-8

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline
from collections import defaultdict

signal_fig_size = (10,4)
fourier_fig_size = signal_fig_size
# fourier_fig_size = (18,4)

################################################################################
# Pulso rectangular de duración Ta (segundos) centrado en ventana de Td 
# (segundos) tomando muestras a fs (muestras por segundo).
################################################################################
def pulsoRect(Td, fs, Ta):
    # Número de muestra en ventana de Td (segundos) a fs (muestras por segundo)
    N = int(Td*fs) # Truncamiento
    N_pulso = int(Ta*fs)    
    tiempo = np.arange(-Td/2, Td/2, 1/fs)
    muestras = np.concatenate((np.zeros(int(N/2-N_pulso/2)), np.ones(int(N_pulso)), np.zeros(int(N/2-N_pulso/2))))
    if Td == Ta:
        muestras = np.ones(len(tiempo))
    return muestras, tiempo

################################################################################
# Escalón
################################################################################
def escalon(Td, fs):
    # Número de muestra en ventana de Td (segundos) a fs (muestras por segundo)
    N = int(Td*fs) # Truncamiento
    tiempo = np.arange(-Td/2, Td/2, 1/fs)
    #     m1 = np.zeros(N/2)
    #     m2 = np.ones(N-N/2)
    muestras = np.concatenate((np.zeros(int(N/2)), np.ones(int(N-N/2))))             
    return muestras, tiempo


################################################################################
# Coseno
################################################################################
def cos(Td, fs, fc, phase=0):
    tiempo = np.arange(-Td/2, Td/2, 1/fs)        
    m = np.cos(2*np.pi*fc*tiempo + phase)    
    return m, tiempo
    

################################################################################
# Seno cardinal
################################################################################
def sinc(Td, fs, W):
    N = int(Td*fs) #trunca
    tiempo = np.arange(-Td/2, Td/2, 1/fs)    
    muestras = np.sinc(2*W*tiempo)    
    return muestras, tiempo


################################################################################
# Retardo (y[n] = x[n-M]).
# Se repite el valor en los bordes.
################################################################################
def retardo(x,M):
    if M > 0:
        y = np.concatenate( (x[0]*np.ones(M), x[0:-M]) )
    elif M < 0:
        y = np.concatenate( (x[-M:], x[-1]*np.ones(-M)) )

    return y


################################################################################
# Calcular la Transformada de Fourier (FFT)
################################################################################
def TFourier(m, fs, zeros=0):
    vector = np.concatenate((m, np.zeros(zeros)))
    fft = np.fft.fft(vector)
    fft = np.fft.fftshift(fft)    
    N = len(fft)
    freq = (fs/N)*np.arange(-N/2, N/2) # Vector de frecuencias    
    return fft, freq


################################################################################
# Calcular la Inversa de la Transformada de Fourier (FFT)
################################################################################
def iTFourier(dft, fs):
    ifft = np.fft.ifft(dft)
    #ifft = np.fft.fftshift(ifft)    
    Td = float(len(dft))/fs
    tiempo = np.arange(-Td/2, Td/2, 1/fs) # Vector de tiempos
    return ifft, tiempo
    

################################################################################
# Calcular la convolución entre dos señales
################################################################################
def convolution(m_1, m_2, Td, fs):
    convolution = np.convolve(m_1,m_2,'same')
    tiempo = np.arange(-Td/2, Td/2, 1/fs)    
    return convolution, tiempo


################################################################################
# Enventanar una señal con una ventana
################################################################################
def recortar_y_enventanar(m, M, ventana):
    N = len(m)
    if ventana == 'rectangular':
        mvent = signal.windows.boxcar(2*M+1)
    elif ventana == 'hann':
        mvent = signal.windows.hann(2*M+1)
    elif ventana == 'hamming':
        mvent = signal.windows.hamming(2*M+1)
    elif ventana == 'blackman':
        mvent = signal.windows.blackman(2*M+1)
    elif ventana == 'bartlett':
        mvent = signal.windows.bartlett(2*M+1)
    vtrim = np.concatenate((np.zeros(int(N/2-M)),mvent,np.zeros(int(N/2-M-1))))    
    return m * vtrim
    

################################################################################
# Gaficar señal en el tiempo
################################################################################
def plot_signal(t, y, titulo="Signal"):
    plt.figure(figsize=signal_fig_size)
    markerline, stemlines, baseline = plt.stem(t*1000, y, '-')
    plt.setp(baseline, color='black', linewidth=0)
    plt.setp(markerline, markersize=4, color='black')
    plt.setp(stemlines, linewidth=1, color='gray')
    plt.title(titulo)
    plt.xlabel("t (mseg)")
    plt.grid(color='gray', linestyle='dotted')
    plt.show()
    
    
################################################################################
# Graficar la Transformada de Fourier
################################################################################
def plot_TF(f, h, muestras=False, semilogy=False):
    plt.figure(figsize=fourier_fig_size)
    
    plt.subplot(1,2,1)
    if muestras:
        if semilogy:
            plt.semilogy(f, abs(h), f, abs(h), 'r.')
        else:
            plt.plot(f, abs(h), f, abs(h), 'r.')
        plt.title("Módulo de la Transformada de Fourier\n(con muestras FFT)")
    else:
        if semilogy:
            plt.semilogy(f, abs(h))
        else:
            plt.plot(f, abs(h))
        plt.title("Módulo de la Transformada de Fourier")
    plt.grid(color='gray', linestyle='dotted')
    plt.xlabel("f (Hz)")
    
    plt.subplot(1,2,2)
    if muestras:
        plt.plot(f, np.angle(h), f, np.angle(h), 'r.')
    else:
        plt.plot(f, np.angle(h))
    plt.grid(color='gray', linestyle='dotted')
    plt.title("Fase de la Transformada de Fourier")
    plt.xlabel("f (Hz)")
    
    plt.show()
    

################################################################################ 
# Graficar el plano-Z dados los polos y los ceros.
################################################################################
def zplane(z, p, filename=None):
    plt.figure(figsize=signal_fig_size)
    ax = plt.subplot(1,1,1)
    
    # Add unit circle and zero axes    
    unit_circle = patches.Circle((0,0), radius=1, fill=False, color='black', ls='dashed', alpha=0.5)
    ax.add_patch(unit_circle)
    axvline(0, color='0.7')
    axhline(0, color='0.7')    
    
    # Plot the poles and set marker properties
    poles = plt.plot(p.real, p.imag, 'rx', markersize=7)
    
    # Plot the zeros and set marker properties
    zeros = plt.plot(z.real, z.imag,  'go', markersize=7)
    # , color='none', markeredgecolor=poles[0].get_color())
    
    # Scale axes to fit
    r = 1.5 * np.amax(np.concatenate((abs(z), abs(p), [1])))
    plt.axis('scaled')
    plt.axis([-r, r, -r, r])
    plt.title("Diagrama de polos y ceros")

