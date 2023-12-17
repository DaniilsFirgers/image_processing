# Hāra vilkņu pārveidošana ir grūti īstenojama uz reāla attēla, tāpēc es izmantosiu vienkāršu signālu.

def haar_wavelet_transform(signal, level):

    # The scale factor is used to adjust the amplitude of the signal
    scale_factor = .5**(1/2)

    # Both low and high filters help to separate different frequency components of the signal
    # We will aplly filter to all adjacent values in the signal

    # Used to extract the low-frequency components or approximation coefficients
    # Each value in the original signal is multiplied by 1
    # Extracts LL subband
    low_pass_f = [1,  1]

    # Used to extract high-frequency components or detail coefficients
    # First value is multiplied by 1, second by -1
    # Extracts LH, HL, HH subbands
    high_pass_f = [1, -1]

    # Length of the filter
    # We need it to know how many adjacent values we need to multiply by the filter
    filter_len = len(low_pass_f)

    # Create a copy of the signal
    signal_copy = signal

    # Length of the signal
    signal_len = len(signal_copy)

    # Initialise the array for the output (all zeros)
    output = [0] * signal_len

    # We extend the the orginal signal by two zeros
    # Now sequence is of power of 2, which is a good tehcnique for the wavelet transform
    signal_copy = signal_copy + [0, 0]

    # We will apply the filter to the signal level times
    for i in range(level):

        # We initialize the output array with zeros (length of the signal)
        output[0:signal_len] = [0] * signal_len
        # We divide the signal into two parts

        # First part is approximation (low frequency components), second is detail ()
        # Represents the length of the approximation coefficients at the current level
        split_len = signal_len // 2

        # Iterate over split signal
        for j in range(split_len):
            # Iterate over filter
            for k in range(filter_len):
                # Update j element of the output array.
                # Signal_copy[2*j + k] refers to the original signal value.
                # 2*j is used to ensure we're working with adjacent pairs of values in the original signal
                # k is used to access the appropriate filter coefficient.
                # low_pass_f[k] represents the k-th coefficient of the low-pass filter
                output[j] += signal_copy[2*j + k] * \
                    low_pass_f[k] * scale_factor

                # Updates the j + split_len-th element of the output array
                # high_pass_f[k] represents the k-th coefficient of the high-pass filter.
                output[j+split_len] += signal_copy[2*j + k] * \
                    high_pass_f[k] * scale_factor
                
            output = [round(value, 2) for value in output]

        # updates the length of the signal (signal_len) to be equal to split_len
        signal_len = split_len

        # This line copies the content of output back into signal_copy. The copy is limited to the first signal_len elements
        # Signal_copy is a copy of the original signal. After each iteration of the transform, it's updated to contain the transformed coefficients
        # Output contains the newly computed coefficients for the current level
        signal_copy[0:signal_len] = output[0:signal_len]

    return output


def main():
    signal = [56, 40, 8, 24, 48, 48, 40, 16]

    # Base level
    print("Level 0")
    print(signal)

    # Level 1 where we apply the filter once
    print("Level 1")
    print(haar_wavelet_transform(signal, 1))

    # Level 2 where we apply the filter twice
    print("Level 2")
    print(haar_wavelet_transform(signal, 2))

    # Level 3 where we apply the filter three times
    print("Level 3")
    print(haar_wavelet_transform(signal, 3))


if __name__ == "__main__":
    main()
