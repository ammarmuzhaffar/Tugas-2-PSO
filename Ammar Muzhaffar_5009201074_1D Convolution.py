# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:07:02 2023

@author: ASUS
"""
def convolution_1d(signal, kernel, mode='full'):
    signal_length = len(signal)
    kernel_length = len(kernel)

    if mode == 'valid':
        result_length = max(signal_length - kernel_length + 1, 0)
    elif mode == 'same':
        result_length = signal_length
    elif mode == 'full':
        result_length = signal_length + kernel_length - 1
    else:
        raise ValueError("Invalid mode. Choose from 'valid', 'same', or 'full'.")
    result = [0] * result_length
    kernel = kernel[::-1]

    for i in range(result_length):
        result[i] = sum(signal[i - j] * kernel[j] if i - j >= 0 and i - j < signal_length else 0 for j in range(kernel_length))

    return result


if __name__ == "__main__":
    signal = [2, 2, 3, 4, 4]
    kernel = [0.5, 1, 0.5]

    
    convolved_signal_same = convolution_1d(signal, kernel, mode='same')
    print("Convolution Result (same mode):", convolved_signal_same)
    convolved_signal_valid = convolution_1d(signal, kernel, mode='valid')
    print("Convolution Result (valid mode):", convolved_signal_valid)
    convolved_signal_full = convolution_1d(signal, kernel, mode='full')
    print("Convolution Result (full mode):", convolved_signal_full)
    print("Naive Implementation of Convolution")
    print("Name:Ammar Muzhaffar")
    print("NRP:5009201074")

