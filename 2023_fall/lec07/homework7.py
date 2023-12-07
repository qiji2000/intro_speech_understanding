import numpy as np

def voiced_excitation(duration, F0, Fs):
    '''
    Create voiced speeech excitation.
    
    @param:
    duration (scalar) - length of the excitation, in samples
    F0 (scalar) - pitch frequency, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    excitation (np.ndarray) - the excitation signal, such that
      excitation[n] = -1 if n is an integer multiple of int(np.round(Fs/F0))
      excitation[n] = 0 otherwise
    '''
    excitation = np.zeros(duration) 
    period = int(np.round(Fs / F0))
    
    for n in range(duration):
        if n % period == 0:
            excitation[n] = -1
    return excitation

def resonator(x, F, BW, Fs):
    '''
    Generate the output of a resonator.
    
    @param:
    x (np.ndarray(N)) - the excitation signal
    F (scalar) - resonant frequency, in Hertz
    BW (scalar) - resonant bandwidth, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    y (np.ndarray(N)) - resonant output
    '''
    y = np.zeros(len(x)) 
    w0 = 2 * np.pi * F / Fs
    alpha = np.sin(w0) * np.sinh((np.log(2) / 2) * BW * w0 / np.sin(w0))
    beta = np.sqrt(1 - alpha**2)

    for n in range(2, len(x)):
        y[n] = alpha * x[n] - alpha * x[n-1] + beta * y[n-1] - alpha * beta * y[n-2]

    return y

def synthesize_vowel(duration,F0,F1,F2,F3,F4,BW1,BW2,BW3,BW4,Fs):
    '''
    Synthesize a vowel.
    
    @param:
    duration (scalar) - duration in samples
    F0 (scalar) - pitch frequency in Hertz
    F1 (scalar) - first formant frequency in Hertz
    F2 (scalar) - second formant frequency in Hertz
    F3 (scalar) - third formant frequency in Hertz
    F4 (scalar) - fourth formant frequency in Hertz
    BW1 (scalar) - first formant bandwidth in Hertz
    BW2 (scalar) - second formant bandwidth in Hertz
    BW3 (scalar) - third formant bandwidth in Hertz
    BW4 (scalar) - fourth formant bandwidth in Hertz
    Fs (scalar) - sampling frequency in samples/second
    
    @returns:
    speech (np.ndarray(samples)) - synthesized vowel
    '''
     speech = np.zeros(duration)
    
    # Generate pitch using a sinusoidal waveform
    t = np.arange(0, duration) / Fs
    pitch = 0.5 * np.sin(2 * np.pi * F0 * t)
    
    # Generate formants using resonators
    formant1 = resonator(pitch, F1, BW1, Fs)
    formant2 = resonator(pitch, F2, BW2, Fs)
    formant3 = resonator(pitch, F3, BW3, Fs)
    formant4 = resonator(pitch, F4, BW4, Fs)
    
    speech = formant1 + formant2 + formant3 + formant4
    return speech
    
