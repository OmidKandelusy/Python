# include the required modules and packages
import cmath

class DFT:
    def __init__(self, fs, N):
        self.fs = fs
        self.N = N

    def dft(self, x: list):
        if len(x) <= 0:
            return -1
        input_x = []
        for n in range(self.N):
            if n < len(x):
                input_x.append(x[n])
            else:
                input_x.append(0)

        # dft sequence output list
        summer = []
        dft_seq = []
        for k in range(0, self.N):
            summer.clear()
            for n in range(0, self.N):
                to_add = input_x[n] * cmath.exp(-1j * 2 * cmath.pi * k * n / self.N)
                summer.append(to_add)
            dft_seq.append(sum(summer))

        # dft frequency bins list
        base_bin = 1 / self.N
        freq_axis = []
        for w in range(0, self.N):
            freq_axis.append(base_bin * w)

        return freq_axis, dft_seq
    

    def physical_freq_axis(self, raw_f_axis):
        freq_axis = [f * self.fs for f in raw_f_axis]
        if self.N % 2 == 0:
            positive_bins = freq_axis[0: self.N//2]
            negative_bins = [-f for f in freq_axis[self.N//2:]]
            negative_bins = negative_bins[::-1]
            negative_bins = [x + (self.fs//2) for x in negative_bins]

        else:
            positive_bins = freq_axis[0: (self.N-1)//2]
            negative_bins = [-f for f in freq_axis[(self.N-1)//2:]]
        return negative_bins + positive_bins
    
    def physical_dft_shift(self, raw_dft_seq):
        if self.N % 2 == 0:
            positive_sequence = raw_dft_seq[0: self.N//2]
            negative_sequence = raw_dft_seq[self.N//2:]
        else:
            positive_sequence = raw_dft_seq[0:(self.N-1)//2]
            negative_sequence = raw_dft_seq[(self.N-1)//2:]

        return negative_sequence + positive_sequence


        


    